import base64
import gzip
import hmac
import json
import logging
import os
import uuid
from datetime import date, datetime, timedelta
from hashlib import sha256
from unittest import mock
from unittest.mock import MagicMock, patch, call
from urllib.parse import urlencode, urlparse

import responses
from celery.exceptions import Retry
from django.conf import settings
from django.contrib.auth.models import User
from django.core.management import call_command
from django.db.models.signals import post_save
from django.test import TestCase, override_settings
from django.urls import reverse
from django.utils import timezone
from go_http.send import LoggingSender
from requests_testadapter import TestAdapter, TestSession
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient
from rest_hooks.models import Hook
from requests import exceptions as requests_exceptions
from seed_services_client.metrics import MetricsApiClient

from seed_message_sender.utils import load_callable

from . import tasks
from .factory import (
    HttpApiSender,
    HttpApiSenderException,
    JunebugApiSender,
    MessageClientFactory,
    WassupApiSenderException,
    WhatsAppApiSender,
    WhatsAppApiSenderException,
)
from .models import (
    AggregateOutbounds,
    ArchivedOutbounds,
    Channel,
    IdentityLookup,
    Inbound,
    Outbound,
    OutboundSendFailure,
)
from .serializers import OutboundArchiveSerializer
from .signals import psh_fire_msg_action_if_new
from .tasks import (
    ConcurrencyLimiter,
    SendMessage,
    fire_metric,
    requeue_failed_tasks,
    send_message,
)
from .views import fire_delivery_hook


class VumiLoggingSender(LoggingSender):
    def send_text(self, *args, **kwargs):
        kwargs.pop("metadata", None)
        return super().send_text(*args, **kwargs)

    def send_image(self, to_addr, content, image_url=None):
        raise HttpApiSenderException("Sending images not available on this channel.")


get_client_original = SendMessage.get_client
SendMessage.get_client = lambda x, y: VumiLoggingSender("go_http.test")


def make_channels():
    vumi_channel = {
        "channel_id": "VUMI_TEXT",
        "channel_type": Channel.VUMI_TYPE,
        "default": False,
        "configuration": {
            "VUMI_CONVERSATION_KEY": "conv-key",
            "VUMI_ACCOUNT_KEY": "account-key",
            "VUMI_ACCOUNT_TOKEN": "account-token",
            "VUMI_API_URL": "http://example.com/",
        },
        "concurrency_limit": 1,
        "message_timeout": 20,
        "message_delay": 10,
    }
    Channel.objects.create(**vumi_channel)

    vumi_channel2 = {
        "channel_id": "VUMI_VOICE",
        "channel_type": Channel.VUMI_TYPE,
        "default": False,
        "configuration": {
            "VUMI_CONVERSATION_KEY": "conv-key",
            "VUMI_ACCOUNT_KEY": "account-key",
            "VUMI_ACCOUNT_TOKEN": "account-token",
            "VUMI_API_URL": "http://example.com/",
        },
        "concurrency_limit": 1,
        "message_timeout": 20,
        "message_delay": 10,
    }
    Channel.objects.create(**vumi_channel2)

    june_channel = {
        "channel_id": "JUNE_VOICE",
        "channel_type": Channel.JUNEBUG_TYPE,
        "default": False,
        "configuration": {
            "JUNEBUG_API_URL": "http://example.com/",
            "JUNEBUG_API_AUTH": ("username", "password"),
            "JUNEBUG_API_FROM": "+4321",
        },
        "concurrency_limit": 1,
        "message_timeout": 120,
        "message_delay": 100,
    }
    Channel.objects.create(**june_channel)

    june_channel2 = {
        "channel_id": "JUNE_TEXT",
        "channel_type": Channel.JUNEBUG_TYPE,
        "default": True,
        "configuration": {
            "JUNEBUG_API_URL": "http://example.com/",
            "JUNEBUG_API_AUTH": ("username", "password"),
            "JUNEBUG_API_FROM": "+4321",
        },
        "concurrency_limit": 0,
        "message_timeout": 0,
        "message_delay": 0,
    }
    Channel.objects.create(**june_channel2)

    june_channel2 = {
        "channel_id": "JUNE_VOICE2",
        "channel_type": Channel.JUNEBUG_TYPE,
        "default": False,
        "configuration": {
            "JUNEBUG_API_URL": "http://example.com/",
            "JUNEBUG_API_AUTH": ("username", "password"),
            "JUNEBUG_API_FROM": "+4321",
        },
        "concurrency_limit": 2,
        "message_timeout": 20,
        "message_delay": 10,
    }
    Channel.objects.create(**june_channel2)

    http_channel_text = {
        "channel_id": "HTTP_API_TEXT",
        "channel_type": Channel.HTTP_API_TYPE,
        "default": False,
        "configuration": {
            "HTTP_API_URL": "http://example.com/",
            "HTTP_API_AUTH": ("username", "password"),
            "HTTP_API_FROM": "+4321",
        },
        "concurrency_limit": 0,
        "message_timeout": 0,
        "message_delay": 0,
    }
    Channel.objects.create(**http_channel_text)

    http_channel_voice = {
        "channel_id": "HTTP_API_VOICE",
        "channel_type": Channel.HTTP_API_TYPE,
        "default": False,
        "configuration": {
            "HTTP_API_URL": "http://example.com/",
            "HTTP_API_AUTH": ("username", "password"),
            "HTTP_API_FROM": "+4321",
        },
        "concurrency_limit": 2,
        "message_timeout": 20,
        "message_delay": 10,
    }
    Channel.objects.create(**http_channel_voice)

    wassup_channel_text = {
        "channel_id": "WASSUP_API",
        "channel_type": Channel.WASSUP_API_TYPE,
        "default": False,
        "configuration": {
            "WASSUP_API_URL": "http://example.com/",
            "WASSUP_API_TOKEN": "http-api-token",
            "WASSUP_API_HSM_UUID": "the-uuid",
            "WASSUP_API_NUMBER": "+4321",
        },
        "concurrency_limit": 0,
        "message_timeout": 0,
        "message_delay": 0,
    }
    Channel.objects.create(**wassup_channel_text)

    wassup_channel_text = {
        "channel_id": "WASSUP_API_NON_HSM",
        "channel_type": Channel.WASSUP_API_TYPE,
        "default": False,
        "configuration": {
            "WASSUP_API_URL": "http://example.com/",
            "WASSUP_API_TOKEN": "http-api-token",
            "WASSUP_API_HSM_UUID": "the-uuid",
            "WASSUP_API_NUMBER": "+4321",
            "WASSUP_API_HSM_DISABLED": True,
        },
        "concurrency_limit": 0,
        "message_timeout": 0,
        "message_delay": 0,
    }
    Channel.objects.create(**wassup_channel_text)

    whatsapp_channel = {
        "channel_id": "WHATSAPP",
        "channel_type": Channel.WHATSAPP_API_TYPE,
        "default": False,
        "configuration": {
            "API_URL": "http://example.com/",
            "API_TOKEN": "http-api-token",
            "HSM_NAMESPACE": "whatsapp:hsm:test",
            "HSM_ELEMENT_NAME": "test",
        },
        "concurrency_limit": 0,
        "message_timeout": 0,
        "message_delay": 0,
    }
    Channel.objects.create(**whatsapp_channel)


class RecordingAdapter(TestAdapter):

    """ Record the request that was handled by the adapter.
    """

    request = None

    def send(self, request, *args, **kw):
        self.request = request
        return super(RecordingAdapter, self).send(request, *args, **kw)


class RecordingHandler(logging.Handler):

    """ Record logs. """

    logs = None

    def emit(self, record):
        if self.logs is None:
            self.logs = []

        self.logs.append(record)


class MockCache(object):
    def __init__(self):
        self.cache_data = {}

    def get(self, key):
        return self.cache_data.get(key, None)

    def get_or_set(self, key, value, expire=0):
        if key not in self.cache_data:
            self.cache_data[key] = value
            return value
        return self.cache_data[key]

    def add(self, key, value, expire=0):
        if key not in self.cache_data:
            self.cache_data[key] = value
            return True
        return False

    def incr(self, key, value=1):
        if key not in self.cache_data:
            raise (ValueError)
        self.cache_data[key] += value

    def decr(self, key, value=1):
        if key not in self.cache_data:
            raise (ValueError)
        self.cache_data[key] -= value


class APITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.adminclient = APIClient()
        self.session = TestSession()


class AuthenticatedAPITestCase(APITestCase):
    def make_outbound(
        self, to_addr="+27820000123", to_identity="0c03d360", channel=None
    ):

        if channel:
            channel = Channel.objects.get(channel_id=channel)

        self._replace_post_save_hooks_outbound()  # don't let fixtures fire
        outbound_message = {
            "to_addr": to_addr,
            "to_identity": to_identity,
            "vumi_message_id": "075a32da-e1e4-4424-be46-1d09b71056fd",
            "content": "Simple outbound message",
            "delivered": False,
            "attempts": 1,
            "metadata": {},
            "channel": channel,
        }
        outbound = Outbound.objects.create(**outbound_message)
        self._restore_post_save_hooks_outbound()  # let tests fire tasks
        return str(outbound.id)

    def make_inbound(self, in_reply_to, from_addr="+27820000020", from_identity=""):
        inbound_message = {
            "message_id": str(uuid.uuid4()),
            "in_reply_to": in_reply_to,
            "to_addr": "+27820000123",
            "from_addr": from_addr,
            "from_identity": from_identity,
            "content": "Call delivered",
            "transport_name": "test_voice",
            "transport_type": "voice",
            "helper_metadata": {},
        }
        inbound = Inbound.objects.create(**inbound_message)
        return str(inbound.id)

    def _replace_get_metric_client(self, session=None):
        return MetricsApiClient(
            url=settings.METRICS_URL, auth=settings.METRICS_AUTH, session=session
        )

    def _restore_get_metric_client(self, session=None):
        return MetricsApiClient(
            url=settings.METRICS_URL, auth=settings.METRICS_AUTH, session=session
        )

    def _replace_post_save_hooks_outbound(self):
        post_save.disconnect(
            psh_fire_msg_action_if_new,
            sender=Outbound,
            dispatch_uid="psh_fire_msg_action_if_new",
        )

    def _restore_post_save_hooks_outbound(self):
        post_save.connect(
            psh_fire_msg_action_if_new,
            sender=Outbound,
            dispatch_uid="psh_fire_msg_action_if_new",
        )

    def check_request(self, request, method, params=None, data=None, headers=None):
        self.assertEqual(request.method, method)
        if params is not None:
            url = urlparse.urlparse(request.url)
            qs = urlparse.parse_qsl(url.query)
            self.assertEqual(dict(qs), params)
        if headers is not None:
            for key, value in headers.items():
                self.assertEqual(request.headers[key], value)
        if data is None:
            self.assertEqual(request.body, None)
        else:
            self.assertEqual(json.loads(request.body), data)

    def _mount_session(self):
        response = [{"name": "foo", "value": 9000, "aggregator": "bar"}]
        adapter = RecordingAdapter(json.dumps(response).encode("utf-8"))
        self.session.mount("http://metrics-url/metrics/", adapter)
        return adapter

    def setUp(self):
        super(AuthenticatedAPITestCase, self).setUp()
        tasks.get_metric_client = self._replace_get_metric_client
        self.adapter = self._mount_session()

        self.username = "testuser"
        self.password = "testpass"
        self.user = User.objects.create_user(
            self.username, "testuser@example.com", self.password
        )
        token = Token.objects.create(user=self.user)
        self.token = token.key
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token)
        self.superuser = User.objects.create_superuser(
            "testsu", "su@example.com", "dummypwd"
        )
        sutoken = Token.objects.create(user=self.superuser)
        self.adminclient.credentials(HTTP_AUTHORIZATION="Token %s" % sutoken)

        self.handler = RecordingHandler()
        logger = logging.getLogger("go_http.test")
        logger.setLevel(logging.INFO)
        logger.addHandler(self.handler)
        make_channels()

    def tearDown(self):
        tasks.get_metric_client = self._restore_get_metric_client

    def check_logs(self, msg):
        if self.handler.logs is None:  # nothing to check
            return False
        if type(self.handler.logs) != list:
            [logs] = self.handler.logs
        else:
            logs = self.handler.logs
        for log in logs:
            logline = log.msg.replace("u'", "'")
            if logline == msg:
                return True
        return False

    def add_identity_search_response(self, msisdn, identity, count=1):
        msisdn = msisdn.replace("+", "%2B")
        results = [
            {
                "id": identity,
                "version": 1,
                "details": {
                    "default_addr_type": "msisdn",
                    "addresses": {"msisdn": {msisdn: {}}},
                },
            }
        ] * count
        response = {"next": None, "previous": None, "results": results}
        qs = "?details__addresses__msisdn=%s" % msisdn
        responses.add(
            responses.GET,
            "%s/identities/search/%s" % (settings.IDENTITY_STORE_URL, qs),  # noqa
            json=response,
            status=200,
            match_querystring=True,
        )

    def add_create_identity_response(self, identity, msisdn):
        # Setup
        identity = {
            "id": identity,
            "version": 1,
            "details": {
                "default_addr_type": "msisdn",
                "addresses": {"msisdn": {msisdn: {}}},
                "risk": "high",
            },
            "communicate_through": None,
            "operator": None,
            "created_at": "2016-04-21T09:11:05.725680Z",
            "created_by": 2,
            "updated_at": "2016-06-15T15:09:05.333526Z",
            "updated_by": 2,
        }
        responses.add(
            responses.POST,
            "%s/identities/" % settings.IDENTITY_STORE_URL,
            json=identity,
            status=201,
        )

    def add_metrics_response(self):
        responses.add(
            responses.POST, "http://metrics-url/metrics/", json={}, status=201
        )


class TestWassupMessagesAPI(AuthenticatedAPITestCase):
    @responses.activate
    @patch("message_sender.tests.VumiLoggingSender.send_image")
    def test_create_outbound_image(self, mock_send_image):
        """
        When creating a outbound with a image_url in the metadata, the
        send_image function should be called with the correct parameters.
        """
        mock_send_image.return_value = {"message_id": str(uuid.uuid4())}
        self.add_metrics_response()
        self.add_identity_search_response("+27820000123", "0c03d360")

        post_outbound = {
            "to_addr": "+27820000123",
            "delivered": "false",
            "metadata": {"image_url": "https://foo.com/file.jpg"},
            "channel": "WASSUP_API",
            "content": "Check this image",
        }
        response = self.client.post(
            "/api/v1/outbound/",
            json.dumps(post_outbound),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        mock_send_image.assert_called_with(
            "+27820000123", "Check this image", image_url="https://foo.com/file.jpg"
        )


class TestVumiMessagesAPI(AuthenticatedAPITestCase):
    def test_list_pagination_one_page(self):
        outbound = self.make_outbound()

        response = self.client.get("/api/v1/outbound/")

        body = response.json()
        self.assertEqual(len(body["results"]), 1)
        self.assertEqual(body["results"][0]["id"], outbound)
        self.assertIsNone(body["previous"])
        self.assertIsNone(body["next"])

    def test_list_pagination_two_pages(self):
        outbounds = []
        for i in range(3):
            outbounds.append(self.make_outbound())

        # Test first page
        response = self.client.get("/api/v1/outbound/")

        body = response.json()
        self.assertEqual(len(body["results"]), 2)
        self.assertEqual(body["results"][0]["id"], outbounds[2])
        self.assertEqual(body["results"][1]["id"], outbounds[1])
        self.assertIsNone(body["previous"])
        self.assertIsNotNone(body["next"])

        # Test next page
        response = self.client.get(body["next"])

        body = response.json()
        self.assertEqual(len(body["results"]), 1)
        self.assertEqual(body["results"][0]["id"], outbounds[0])
        self.assertIsNotNone(body["previous"])
        self.assertIsNone(body["next"])

        # Test going back to previous page works
        response = self.client.get(body["previous"])

        body = response.json()
        self.assertEqual(len(body["results"]), 2)
        self.assertEqual(body["results"][0]["id"], outbounds[2])
        self.assertEqual(body["results"][1]["id"], outbounds[1])
        self.assertIsNone(body["previous"])
        self.assertIsNotNone(body["next"])

    @responses.activate
    def test_create_outbound_data(self):
        """
        When creating an outbound message, it should save a new Outbound
        object with the correct specified values.
        """
        self.add_metrics_response()
        self.add_identity_search_response("+27820000123", "0c03d360")

        post_outbound = {
            "to_addr": "+27820000123",
            "vumi_message_id": "075a32da-e1e4-4424-be46-1d09b71056fd",
            "content": "Say something",
            "delivered": False,
            "attempts": 0,
            "metadata": {},
            "resend": True,
        }
        response = self.client.post(
            "/api/v1/outbound/",
            json.dumps(post_outbound),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        d = Outbound.objects.last()
        self.assertIsNotNone(d.id)
        self.assertEqual(d.version, 1)
        self.assertEqual(str(d.to_addr), "+27820000123")
        self.assertEqual(str(d.to_identity), "0c03d360")
        self.assertEqual(d.content, "Say something")
        self.assertEqual(d.delivered, False)
        self.assertEqual(d.attempts, 1)
        self.assertEqual(d.metadata, {})
        self.assertEqual(d.resend, True)

    @responses.activate
    def test_create_outbound_data_simple(self):
        """
        When creating a new outbound message, leaving out the optional fields
        in the request should still create an Outbound object.
        """
        self.add_metrics_response()
        self.add_identity_search_response("+27820000123", "0c03d360")

        post_outbound = {
            "to_addr": "+27820000123",
            "delivered": "false",
            "metadata": {"voice_speech_url": "https://foo.com/file.mp3"},
        }
        response = self.client.post(
            "/api/v1/outbound/",
            json.dumps(post_outbound),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        d = Outbound.objects.last()
        self.assertIsNotNone(d.id)
        self.assertEqual(d.version, 1)
        self.assertEqual(str(d.to_addr), "+27820000123")
        self.assertEqual(str(d.to_identity), "0c03d360")
        self.assertEqual(d.delivered, False)
        self.assertEqual(d.attempts, 1)
        self.assertEqual(d.metadata, {"voice_speech_url": "https://foo.com/file.mp3"})
        self.assertEqual(d.channel, None)

    @responses.activate
    def test_create_outbound_data_new_identity(self):
        """
        When creating a new outbound message, if the identity is not supplied,
        and the identity does not exist in the identity store, a new identity
        should be created on the identity store for that address.
        """
        self.add_metrics_response()
        self.add_identity_search_response("+27820012345", None, 0)
        self.add_create_identity_response("0c03d360123", "+27820012345")

        post_outbound = {
            "to_addr": "+27820012345",
            "delivered": "false",
            "metadata": {"voice_speech_url": "https://foo.com/file.mp3"},
        }
        response = self.client.post(
            "/api/v1/outbound/",
            json.dumps(post_outbound),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        d = Outbound.objects.last()
        self.assertIsNotNone(d.id)
        self.assertEqual(d.version, 1)
        self.assertEqual(str(d.to_addr), "+27820012345")
        self.assertEqual(str(d.to_identity), "0c03d360123")
        self.assertEqual(d.delivered, False)
        self.assertEqual(d.attempts, 1)
        self.assertEqual(d.metadata, {"voice_speech_url": "https://foo.com/file.mp3"})
        self.assertEqual(d.channel, None)

        create_id_post = responses.calls[1]

        self.assertEqual(
            json.loads(create_id_post.request.body),
            {
                "details": {
                    "default_addr_type": "msisdn",
                    "addresses": {"msisdn": {"+27820012345": {"default": True}}},
                }
            },
        )

    @responses.activate
    def test_create_outbound_data_with_channel(self):
        """
        When creating an outbound message, if the channel is specified, then
        that Outbound should have the specified channel.
        """
        self.add_metrics_response()
        self.add_identity_search_response("+27820000123", "0c03d360")

        post_outbound = {
            "to_addr": "+27820000123",
            "delivered": "false",
            "metadata": {"voice_speech_url": "https://foo.com/file.mp3"},
            "channel": "JUNE_TEXT",
        }
        response = self.client.post(
            "/api/v1/outbound/",
            json.dumps(post_outbound),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        d = Outbound.objects.last()
        self.assertIsNotNone(d.id)
        self.assertEqual(d.version, 1)
        self.assertEqual(str(d.to_addr), "+27820000123")
        self.assertEqual(str(d.to_identity), "0c03d360")
        self.assertEqual(d.delivered, False)
        self.assertEqual(d.attempts, 1)
        self.assertEqual(d.metadata, {"voice_speech_url": "https://foo.com/file.mp3"})
        self.assertEqual(d.channel.channel_id, "JUNE_TEXT")

    def test_create_outbound_data_with_channel_unknown(self):

        post_outbound = {
            "to_addr": "+27820000123",
            "delivered": "false",
            "metadata": {"voice_speech_url": "https://foo.com/file.mp3"},
            "channel": "JUNE_VOICE_TEST",
        }
        response = self.client.post(
            "/api/v1/outbound/",
            json.dumps(post_outbound),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_outbound_without_recipient(self):

        post_outbound = {"delivered": "false", "metadata": {}}
        response = self.client.post(
            "/api/v1/outbound/",
            json.dumps(post_outbound),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    @responses.activate
    def test_create_outbound_identity_only(self):
        """
        When only the identity UUID is specified, the resulting created
        Outbound object should have the address that was looked up from the
        identity store on it.
        """
        self.add_metrics_response()

        uid = "test-test-test-test"
        # mock identity address lookup
        responses.add(
            responses.GET,
            "%s/identities/%s/addresses/msisdn?default=True&use_communicate_through=True"
            % (settings.IDENTITY_STORE_URL, uid),  # noqa
            json={
                "next": None,
                "previous": None,
                "results": [{"address": "+26773000000"}],
            },
            status=200,
            content_type="application/json",
            match_querystring=True,
        )

        post_outbound = {"to_identity": uid, "delivered": "false", "metadata": {}}
        response = self.client.post(
            "/api/v1/outbound/",
            json.dumps(post_outbound),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        d = Outbound.objects.last()
        self.assertIsNotNone(d.id)
        self.assertEqual(d.version, 1)
        self.assertEqual(d.to_addr, "+26773000000")
        self.assertEqual(d.to_identity, uid)
        self.assertEqual(d.delivered, False)
        self.assertEqual(d.attempts, 1)
        self.assertEqual(d.metadata, {})
        self.assertEqual(d.channel, None)

    def test_update_outbound_data(self):
        existing = self.make_outbound()
        patch_outbound = {"delivered": "true", "attempts": 2}
        response = self.client.patch(
            "/api/v1/outbound/%s/" % existing,
            json.dumps(patch_outbound),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        d = Outbound.objects.get(pk=existing)
        self.assertEqual(d.version, 1)
        self.assertEqual(str(d.to_addr), "+27820000123")
        self.assertEqual(d.delivered, True)
        self.assertEqual(d.attempts, 2)

    def test_delete_outbound_data(self):
        existing = self.make_outbound()
        response = self.client.delete(
            "/api/v1/outbound/%s/" % existing, content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        d = Outbound.objects.filter(id=existing).count()
        self.assertEqual(d, 0)

    def test_created_at_filter_outbound_exists(self):
        existing = Outbound.objects.get(pk=self.make_outbound())
        response = self.client.get(
            "/api/v1/outbound/?%s"
            % (
                urlencode(
                    {
                        "before": (existing.created_at + timedelta(days=1)).isoformat(),
                        "after": (existing.created_at - timedelta(days=1)).isoformat(),
                    }
                )
            )
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 1)
        self.assertEqual(response.data["results"][0]["id"], str(existing.id))

    def test_created_at_filter_outbound_not_exists(self):
        existing = Outbound.objects.get(pk=self.make_outbound())
        response = self.client.get(
            "/api/v1/outbound/?%s"
            % (
                urlencode(
                    {
                        "before": (existing.created_at - timedelta(days=1)).isoformat(),
                        "after": (existing.created_at + timedelta(days=1)).isoformat(),
                    }
                )
            )
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["results"], [])

    def test_to_addr_filter_outbound(self):
        """
        When filtering on to_addr, only the outbound with the specified to
        address should be returned.
        """
        self.make_outbound(to_addr="+1234")
        self.make_outbound(to_addr="+4321")

        response = self.client.get(
            "/api/v1/outbound/?{}".format(urlencode({"to_addr": "+1234"}))
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 1)

    def test_to_addr_filter_outbound_multiple(self):
        """
        When filtering on to_addr, if multiple values are presented for the
        to address, we should return all outbound messages that match one of
        the to addresses.
        """
        self.make_outbound(to_addr="+1234")
        self.make_outbound(to_addr="+4321")
        self.make_outbound(to_addr="+1111")

        response = self.client.get(
            "/api/v1/outbound/?{}".format(
                urlencode((("to_addr", "+1234"), ("to_addr", "+4321")))
            )
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 2)

    def test_to_identity_filter_outbound(self):
        """
        When filtering on to_identity, only outbound messages with that
        identity id should be returned.
        """
        self.make_outbound(to_identity="1234")
        self.make_outbound(to_identity="4321")

        response = self.client.get(
            "/api/v1/outbound/?{}".format(urlencode((("to_identity", "1234"),)))
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 1)

    def test_to_identity_filter_outbound_multiple(self):
        """
        When filtering on to_identity, if multiple values are presented for the
        identity ID, we should return all outbound messages that match one of
        the identity IDs.
        """
        self.make_outbound(to_identity="1234")
        self.make_outbound(to_identity="4321")
        self.make_outbound(to_identity="1111")

        response = self.client.get(
            "/api/v1/outbound/?{}".format(
                urlencode((("to_identity", "1234"), ("to_identity", "4321")))
            )
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 2)

    def test_created_at_ordering_filter_outbound(self):
        """
        We should be able to order the results of the Outbound list endpoint
        by the created_at timestamp.
        """
        out1 = self.make_outbound()
        out2 = self.make_outbound()

        response = self.client.get(
            "/api/v1/outbound/?{}".format(urlencode({"ordering": "created_at"}))
        )
        self.assertEqual([o["id"] for o in response.data["results"]], [out1, out2])

        response = self.client.get(
            "/api/v1/outbound/?{}".format(urlencode({"ordering": "-created_at"}))
        )
        self.assertEqual([o["id"] for o in response.data["results"]], [out2, out1])

    def test_from_addr_filter_inbound(self):
        """
        When filtering on from_addr, only the inbounds with the specified from
        address should be returned.
        """
        self.make_inbound("1234", from_addr="+1234")
        self.make_inbound("1234", from_addr="+4321")

        response = self.client.get(
            "/api/v1/inbound/?{}".format(urlencode({"from_addr": "+1234"}))
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 1)

    def test_from_addr_filter_inbound_multiple(self):
        """
        When filtering on from_addr, if multiple values are presented for the
        from address, we should return all inbound messages that match one of
        the from addresses.
        """
        self.make_inbound("1234", from_addr="+1234")
        self.make_inbound("1234", from_addr="+4321")
        self.make_inbound("1234", from_addr="+1111")

        response = self.client.get(
            "/api/v1/inbound/?{}".format(
                urlencode((("from_addr", "+1234"), ("from_addr", "+4321")))
            )
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 2)

    def test_from_identity_filter_inbound(self):
        """
        When filtering on from_identity, only the inbounds with the specified
        identity ID should be returned.
        """
        self.make_inbound("1234", from_identity="1234")
        self.make_inbound("1234", from_identity="4321")

        response = self.client.get(
            "/api/v1/inbound/?{}".format(urlencode({"from_identity": "1234"}))
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 1)

    def test_from_identity_filter_inbound_multiple(self):
        """
        When filtering on from_identity, if multiple values are presented for
        the from identity IDs, we should return all inbound messages that match
        one of the from identity IDs.
        """
        self.make_inbound("1234", from_identity="1234")
        self.make_inbound("1234", from_identity="4321")
        self.make_inbound("1234", from_identity="1111")

        response = self.client.get(
            "/api/v1/inbound/?{}".format(
                urlencode((("from_identity", "1234"), ("from_identity", "4321")))
            )
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 2)

    def test_created_at_ordering_filter_inbound(self):
        """
        We should be able to order the results of the Inbound list endpoint
        by the created_at timestamp.
        """
        in1 = self.make_inbound("1234")
        in2 = self.make_inbound("1234")

        response = self.client.get(
            "/api/v1/inbound/?{}".format(urlencode({"ordering": "created_at"}))
        )
        self.assertEqual([i["id"] for i in response.data["results"]], [in1, in2])

        response = self.client.get(
            "/api/v1/inbound/?{}".format(urlencode({"ordering": "-created_at"}))
        )
        self.assertEqual([i["id"] for i in response.data["results"]], [in2, in1])

    @responses.activate
    def test_create_inbound_data_no_limit(self):
        """
        When there is no concurrency limit set, then for inbound messages,
        the concurrency limiter should not decrement.
        """
        self.add_metrics_response()
        self.add_identity_search_response("+27820000020", "0c03d360")

        existing_outbound = self.make_outbound()
        out = Outbound.objects.get(pk=existing_outbound)
        message_id = str(uuid.uuid4())
        post_inbound = {
            "message_id": message_id,
            "in_reply_to": out.vumi_message_id,
            "to_addr": "+27820000123",
            "from_addr": "+27820000020",
            "content": "Call delivered",
            "transport_name": "test_voice",
            "transport_type": "voice",
            "helper_metadata": {},
        }
        with patch.object(ConcurrencyLimiter, "decr_message_count") as mock_method:
            response = self.client.post(
                "/api/v1/inbound/VUMI_TEXT/",
                json.dumps(post_inbound),
                content_type="application/json",
            )
            mock_method.assert_not_called()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        d = Inbound.objects.last()
        self.assertIsNotNone(d.id)
        self.assertEqual(d.message_id, message_id)
        self.assertEqual(d.to_addr, "+27820000123")
        self.assertEqual(d.from_addr, "")
        self.assertEqual(d.from_identity, "0c03d360")
        self.assertEqual(d.content, "Call delivered")
        self.assertEqual(d.transport_name, "test_voice")
        self.assertEqual(d.transport_type, "voice")
        self.assertEqual(d.helper_metadata, {})

    @responses.activate
    def test_create_inbound_data_unknown_msisdn(self):
        """
        When there is an inbound message created, with an msisdn that doesn't
        exist in the identity store, we should create a new identity for that
        address in the identity store.
        """
        self.add_metrics_response()
        self.add_identity_search_response("+27820000020", "0c03d360", 0)
        self.add_create_identity_response("0c03d360", "+27820000020")

        existing_outbound = self.make_outbound()
        out = Outbound.objects.get(pk=existing_outbound)
        message_id = str(uuid.uuid4())
        post_inbound = {
            "message_id": message_id,
            "in_reply_to": out.vumi_message_id,
            "to_addr": "+27820000123",
            "from_addr": "+27820000020",
            "content": "Call delivered",
            "transport_name": "test_voice",
            "transport_type": "voice",
            "helper_metadata": {},
        }
        with patch.object(ConcurrencyLimiter, "decr_message_count") as mock_method:
            response = self.client.post(
                "/api/v1/inbound/VUMI_TEXT/",
                json.dumps(post_inbound),
                content_type="application/json",
            )
            mock_method.assert_not_called()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        d = Inbound.objects.last()
        self.assertIsNotNone(d.id)
        self.assertEqual(d.message_id, message_id)
        self.assertEqual(d.to_addr, "+27820000123")
        self.assertEqual(d.from_addr, "")
        self.assertEqual(d.from_identity, "0c03d360")
        self.assertEqual(d.content, "Call delivered")
        self.assertEqual(d.transport_name, "test_voice")
        self.assertEqual(d.transport_type, "voice")
        self.assertEqual(d.helper_metadata, {})

    @responses.activate
    def test_create_inbound_data_with_channel_vumi(self):
        """
        When we create an inbound message, the specific channel that the
        URL is linked to should be set on the message.
        """
        self.add_metrics_response()
        self.add_identity_search_response("+27820000020", "0c03d360")

        existing_outbound = self.make_outbound()
        out = Outbound.objects.get(pk=existing_outbound)
        out.last_sent_time = out.created_at
        out.save()
        message_id = str(uuid.uuid4())
        post_inbound = {
            "message_id": message_id,
            "in_reply_to": out.vumi_message_id,
            "to_addr": "+27820000123",
            "from_addr": "+27820000020",
            "content": "Call delivered",
            "transport_name": "test_voice",
            "transport_type": "voice",
            "helper_metadata": {},
            "session_event": "close",
        }
        channel = Channel.objects.get(channel_id="VUMI_VOICE")
        with patch.object(ConcurrencyLimiter, "decr_message_count") as mock_method:
            response = self.client.post(
                "/api/v1/inbound/VUMI_VOICE/",
                json.dumps(post_inbound),
                content_type="application/json",
            )
            mock_method.assert_called_once_with(channel, out.created_at)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        d = Inbound.objects.last()
        self.assertIsNotNone(d.id)
        self.assertEqual(d.message_id, message_id)
        self.assertEqual(d.to_addr, "+27820000123")
        self.assertEqual(d.from_addr, "")
        self.assertEqual(d.from_identity, "0c03d360")
        self.assertEqual(d.content, "Call delivered")
        self.assertEqual(d.transport_name, "test_voice")
        self.assertEqual(d.transport_type, "voice")
        self.assertEqual(d.helper_metadata, {"session_event": "close"})

    @responses.activate
    def test_create_inbound_data_with_channel_junebug(self):
        """
        When an inbound message is created from Junebug, it should set the
        channel specified in the URL as the channel on the inbound message.
        """
        self.add_metrics_response()
        self.add_identity_search_response("+27820000020", "0c03d360")

        existing_outbound = self.make_outbound()
        out = Outbound.objects.get(pk=existing_outbound)
        out.last_sent_time = out.created_at
        out.save()
        message_id = str(uuid.uuid4())
        post_inbound = {
            "message_id": message_id,
            "in_reply_to": out.vumi_message_id,
            "to_addr": "+27820000123",
            "from_addr": "+27820000020",
            "content": "Call delivered",
            "transport_name": "test_voice",
            "transport_type": "voice",
            "helper_metadata": {},
            "session_event": "close",
        }
        channel = Channel.objects.get(channel_id="VUMI_VOICE")
        with patch.object(ConcurrencyLimiter, "decr_message_count") as mock_method:
            response = self.client.post(
                "/api/v1/inbound/VUMI_VOICE/",
                json.dumps(post_inbound),
                content_type="application/json",
            )
            mock_method.assert_called_once_with(channel, out.created_at)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        d = Inbound.objects.last()
        self.assertIsNotNone(d.id)
        self.assertEqual(d.message_id, message_id)
        self.assertEqual(d.to_addr, "+27820000123")
        self.assertEqual(d.from_addr, "")
        self.assertEqual(d.from_identity, "0c03d360")
        self.assertEqual(d.content, "Call delivered")
        self.assertEqual(d.transport_name, "test_voice")
        self.assertEqual(d.transport_type, "voice")
        self.assertEqual(d.helper_metadata, {"session_event": "close"})

    @responses.activate
    def test_create_inbound_data_with_channel_whatsapp(self):
        """
        When an inbound message is created from WhatsApp, it should create an Inbound
        with the correct details
        """
        self.add_metrics_response()
        identity_uuid = str(uuid.uuid4())
        self.add_identity_search_response("+27820000000", identity_uuid)

        message_id = str(uuid.uuid4())
        post_inbound = {
            "id": message_id,
            "from": "27820000000",
            "text": {"body": "Test message"},
        }
        response = self.client.post(
            "/api/v1/inbound/WHATSAPP/",
            json.dumps(post_inbound),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        d = Inbound.objects.last()
        self.assertIsNotNone(d.id)
        self.assertEqual(d.message_id, message_id)
        self.assertEqual(d.from_identity, identity_uuid)
        self.assertEqual(d.content, "Test message")

    def test_update_inbound_data(self):
        existing_outbound = self.make_outbound()
        out = Outbound.objects.get(pk=existing_outbound)
        existing = self.make_inbound(out.vumi_message_id)

        patch_inbound = {"content": "Opt out"}
        response = self.client.patch(
            "/api/v1/inbound/%s/" % existing,
            json.dumps(patch_inbound),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        d = Inbound.objects.get(pk=existing)
        self.assertEqual(d.to_addr, "+27820000123")
        self.assertEqual(d.from_addr, "+27820000020")
        self.assertEqual(d.content, "Opt out")
        self.assertEqual(d.transport_name, "test_voice")
        self.assertEqual(d.transport_type, "voice")
        self.assertEqual(d.helper_metadata, {})

    def test_delete_inbound_data(self):
        existing_outbound = self.make_outbound()
        out = Outbound.objects.get(pk=existing_outbound)
        existing = self.make_inbound(out.vumi_message_id)
        response = self.client.delete(
            "/api/v1/inbound/%s/" % existing, content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        d = Inbound.objects.filter(id=existing).count()
        self.assertEqual(d, 0)

    @patch("message_sender.views.fire_delivery_hook")
    def test_event_ack(self, mock_hook):
        existing = self.make_outbound()

        d = Outbound.objects.get(pk=existing)
        ack = {
            "message_type": "event",
            "event_id": "b04ec322fc1c4819bc3f28e6e0c69de6",
            "event_type": "ack",
            "user_message_id": d.vumi_message_id,
            "helper_metadata": {},
            "timestamp": "2015-10-28 16:19:37.485612",
            "sent_message_id": "external-id",
        }
        response = self.client.post(
            "/api/v1/events", json.dumps(ack), content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        d = Outbound.objects.get(pk=existing)
        self.assertEqual(d.delivered, True)
        self.assertEqual(d.attempts, 1)
        self.assertEqual(d.metadata["ack_timestamp"], "2015-10-28 16:19:37.485612")
        self.assertEqual(
            False,
            self.check_logs(
                "Message: 'Simple outbound message' sent to '+27820000123'"
            ),
        )
        mock_hook.assert_called_once_with(d)

    @patch("message_sender.views.fire_delivery_hook")
    def test_event_delivery_report(self, mock_hook):
        existing = self.make_outbound()
        d = Outbound.objects.get(pk=existing)
        dr = {
            "message_type": "event",
            "event_id": "b04ec322fc1c4819bc3f28e6e0c69de6",
            "event_type": "delivery_report",
            "user_message_id": d.vumi_message_id,
            "helper_metadata": {},
            "timestamp": "2015-10-28 16:20:37.485612",
            "sent_message_id": "external-id",
        }
        response = self.client.post(
            "/api/v1/events", json.dumps(dr), content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        d = Outbound.objects.get(pk=existing)
        self.assertEqual(d.delivered, True)
        self.assertEqual(d.attempts, 1)
        self.assertEqual(d.metadata["delivery_timestamp"], "2015-10-28 16:20:37.485612")
        self.assertEqual(
            False,
            self.check_logs(
                "Message: 'Simple outbound message' sent to '+27820000123'"
            ),
        )
        mock_hook.assert_called_once_with(d)

    @responses.activate
    @patch("message_sender.views.fire_delivery_hook")
    def test_event_nack_first(self, mock_hook):
        self.add_metrics_response()
        existing = self.make_outbound()
        d = Outbound.objects.get(pk=existing)
        post_save.connect(
            psh_fire_msg_action_if_new,
            sender=Outbound,
            dispatch_uid="psh_fire_msg_action_if_new",
        )
        nack = {
            "message_type": "event",
            "event_id": "b04ec322fc1c4819bc3f28e6e0c69de6",
            "event_type": "nack",
            "nack_reason": "no answer",
            "user_message_id": d.vumi_message_id,
            "helper_metadata": {},
            "timestamp": "2015-10-28 16:20:37.485612",
            "sent_message_id": "external-id",
        }
        response = self.client.post(
            "/api/v1/events", json.dumps(nack), content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        c = Outbound.objects.get(pk=existing)
        self.assertEqual(c.delivered, False)
        self.assertEqual(c.attempts, 2)
        self.assertEqual(c.metadata["nack_reason"], "no answer")
        self.assertEqual(
            True,
            self.check_logs(
                "Message: 'Simple outbound message' sent to '+27820000123' "
                "[session_event: new]"
            ),
        )
        mock_hook.assert_called_once_with(d)
        # TODO: Bring metrics back
        # self.assertEquals(
        #     True,
        #     self.check_logs("Metric: 'vumimessage.tries' [sum] -> 1"))

    @responses.activate
    def test_event_nack_last(self):
        self.add_metrics_response()
        # Be assured this is last message attempt
        outbound_message = {
            "to_addr": "+27820000123",
            "vumi_message_id": "08b34de7-c6da-4853-a74d-9458533ed169",
            "content": "Simple outbound message",
            "delivered": False,
            "attempts": 3,
            "metadata": {},
        }
        failed = Outbound.objects.create(**outbound_message)
        failed.last_sent_time = failed.created_at
        failed.save()
        post_save.connect(
            psh_fire_msg_action_if_new,
            sender=Outbound,
            dispatch_uid="psh_fire_msg_action_if_new",
        )
        nack = {
            "message_type": "event",
            "event_id": "b04ec322fc1c4819bc3f28e6e0c69de6",
            "event_type": "nack",
            "nack_reason": "no answer",
            "user_message_id": failed.vumi_message_id,
            "helper_metadata": {},
            "timestamp": "2015-10-28 16:20:37.485612",
            "sent_message_id": "external-id",
        }
        response = self.client.post(
            "/api/v1/events", json.dumps(nack), content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        d = Outbound.objects.get(pk=failed.id)
        self.assertEqual(d.delivered, False)
        self.assertEqual(d.attempts, 3)  # not moved on as last attempt passed
        self.assertEqual(d.metadata["nack_reason"], "no answer")
        self.assertEqual(
            False,
            self.check_logs(
                "Message: 'Simple outbound message' sent to '+27820000123'"
                "[session_event: new]"
            ),
        )
        # TODO: Bring metrics back
        # self.assertEquals(
        #     False,
        #     self.check_logs("Metric: 'vumimessage.tries' [sum] -> 1"))
        # self.assertEquals(
        #     True,
        #     self.check_logs("Metric: 'vumimessage.maxretries' [sum] -> 1"))

    @responses.activate
    def test_fire_delivery_hook_max_retries_not_reached(self):
        """
        This should not fire the hook
        """
        Hook.objects.create(
            user=self.user,
            event="outbound.delivery_report",
            target="http://example.com",
        )
        d = Outbound.objects.get(pk=self.make_outbound())
        responses.add(
            responses.POST,
            "http://example.com",
            status=200,
            content_type="application/json",
        )

        fire_delivery_hook(d)

        self.assertEqual(len(responses.calls), 0)

    @responses.activate
    def test_fire_delivery_hook_max_retries_reached(self):
        """
        This should call deliver_hook_wrapper to send data to a web hook
        """
        hook = Hook.objects.create(
            user=self.user,
            event="outbound.delivery_report",
            target="http://example.com",
        )
        d = Outbound.objects.get(pk=self.make_outbound())
        d.attempts = 3
        d.save()
        responses.add(
            responses.POST,
            "http://example.com",
            status=200,
            content_type="application/json",
        )

        fire_delivery_hook(d)

        [r] = responses.calls
        r = json.loads(r.request.body)
        self.assertEqual(
            r["hook"], {"id": hook.id, "event": hook.event, "target": hook.target}
        )
        self.assertEqual(
            r["data"],
            {
                "delivered": False,
                "to_addr": d.to_addr,
                "outbound_id": str(d.id),
                "identity": d.to_identity,
            },
        )

    @responses.activate
    def test_fire_delivery_hook_when_delivered(self):
        """
        This should call deliver_hook_wrapper to send data to a web hook
        """
        hook = Hook.objects.create(
            user=self.user,
            event="outbound.delivery_report",
            target="http://example.com",
        )
        d = Outbound.objects.get(pk=self.make_outbound())
        d.delivered = True
        d.save()
        responses.add(
            responses.POST,
            "http://example.com",
            status=200,
            content_type="application/json",
        )

        fire_delivery_hook(d)

        [r] = responses.calls
        r = json.loads(r.request.body)
        self.assertEqual(
            r["hook"], {"id": hook.id, "event": hook.event, "target": hook.target}
        )
        self.assertEqual(
            r["data"],
            {
                "delivered": True,
                "to_addr": d.to_addr,
                "outbound_id": str(d.id),
                "identity": d.to_identity,
            },
        )


class TestJunebugMessagesAPI(AuthenticatedAPITestCase):
    def test_event_missing_fields(self):
        """
        If there are missing fields in the request, and error response should
        be returned.
        """
        response = self.client.post(
            "/api/v1/events/junebug", json.dumps({}), content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_event_no_message(self):
        """
        If we cannot find the message for the event, and error response should
        be returned.
        """
        ack = {
            "event_type": "submitted",
            "message_id": "bad-message-id",
            "channel-id": "channel-uuid-1234",
            "timestamp": "2015-10-28 16:19:37.485612",
            "event_details": {},
        }
        response = self.client.post(
            "/api/v1/events/junebug", json.dumps(ack), content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    @patch("message_sender.views.fire_delivery_hook")
    def test_event_ack(self, mock_hook):
        """A submitted event should update the message object accordingly."""
        existing = self.make_outbound()

        d = Outbound.objects.get(pk=existing)
        ack = {
            "event_type": "submitted",
            "message_id": d.vumi_message_id,
            "channel-id": "channel-uuid-1234",
            "timestamp": "2015-10-28 16:19:37.485612",
            "event_details": {},
        }

        response = self.client.post(
            "/api/v1/events/junebug", json.dumps(ack), content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        d = Outbound.objects.get(pk=existing)
        self.assertEqual(d.delivered, True)
        self.assertEqual(d.attempts, 1)
        self.assertEqual(d.metadata["ack_timestamp"], "2015-10-28 16:19:37.485612")
        self.assertEqual(
            False,
            self.check_logs(
                "Message: 'Simple outbound message' sent to '+27820000123'"
            ),
        )
        mock_hook.assert_called_once_with(d)

    @responses.activate
    @patch("message_sender.views.fire_delivery_hook")
    def test_event_nack(self, mock_hook):
        """
        A rejected event should retry and update the message object accordingly
        """
        self.add_metrics_response()
        existing = self.make_outbound()
        d = Outbound.objects.get(pk=existing)
        post_save.connect(
            psh_fire_msg_action_if_new,
            sender=Outbound,
            dispatch_uid="psh_fire_msg_action_if_new",
        )
        nack = {
            "event_type": "rejected",
            "message_id": d.vumi_message_id,
            "channel-id": "channel-uuid-1234",
            "timestamp": "2015-10-28 16:19:37.485612",
            "event_details": {"reason": "No answer"},
        }
        response = self.client.post(
            "/api/v1/events/junebug", json.dumps(nack), content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        c = Outbound.objects.get(pk=existing)
        self.assertEqual(c.delivered, False)
        self.assertEqual(c.attempts, 2)
        self.assertEqual(c.metadata["nack_reason"], {"reason": "No answer"})
        self.assertEqual(
            True,
            self.check_logs(
                "Message: 'Simple outbound message' sent to '+27820000123' "
                "[session_event: new]"
            ),
        )
        mock_hook.assert_called_once_with(d)

    @patch("message_sender.views.fire_delivery_hook")
    def test_event_delivery_succeeded(self, mock_hook):
        """A successful delivery should update the message accordingly."""
        existing = self.make_outbound()
        d = Outbound.objects.get(pk=existing)
        dr = {
            "event_type": "delivery_succeeded",
            "message_id": d.vumi_message_id,
            "channel-id": "channel-uuid-1234",
            "timestamp": "2015-10-28 16:19:37.485612",
            "event_details": {},
        }
        response = self.client.post(
            "/api/v1/events/junebug", json.dumps(dr), content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        d = Outbound.objects.get(pk=existing)
        self.assertEqual(d.delivered, True)
        self.assertEqual(d.attempts, 1)
        self.assertEqual(d.metadata["delivery_timestamp"], "2015-10-28 16:19:37.485612")
        self.assertEqual(
            False,
            self.check_logs(
                "Message: 'Simple outbound message' sent to '+27820000123'"
            ),
        )
        mock_hook.assert_called_once_with(d)

    @responses.activate
    @patch("message_sender.views.fire_delivery_hook")
    def test_event_delivery_failed(self, mock_hook):
        """
        A failed delivery should retry and update the message accordingly.
        """
        self.add_metrics_response()
        existing = self.make_outbound()
        d = Outbound.objects.get(pk=existing)
        dr = {
            "event_type": "delivery_failed",
            "message_id": d.vumi_message_id,
            "channel-id": "channel-uuid-1234",
            "timestamp": "2015-10-28 16:19:37.485612",
            "event_details": {},
        }
        response = self.client.post(
            "/api/v1/events/junebug", json.dumps(dr), content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        d = Outbound.objects.get(pk=existing)
        self.assertEqual(d.delivered, False)
        self.assertEqual(d.attempts, 2)
        self.assertEqual(d.metadata["delivery_failed_reason"], {})
        self.assertEqual(
            False,
            self.check_logs(
                "Message: 'Simple outbound message' sent to '+27820000123'"
            ),
        )
        mock_hook.assert_called_once_with(d)

    @responses.activate
    def test_create_inbound_junebug_message(self):
        """
        If Junebug send an inbound message to the inbound endpoint, then a
        new Inbound should be created with the specified parameters.
        """
        self.add_metrics_response()
        existing_outbound = self.make_outbound()
        out = Outbound.objects.get(pk=existing_outbound)
        out.last_sent_time = out.created_at
        out.save()
        message_id = str(uuid.uuid4())
        post_inbound = {
            "message_id": message_id,
            "reply_to": "test_id",
            "to": "0.0.0.0:9001",
            "from": out.to_addr,
            "content": "Call delivered",
            "channel_id": "test_voice",
            "channel_data": {"session_event": "close"},
        }
        self.add_identity_search_response(out.to_addr, "0c03d360")
        response = self.client.post(
            "/api/v1/inbound/",
            json.dumps(post_inbound),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        d = Inbound.objects.last()
        self.assertIsNotNone(d.id)
        self.assertEqual(d.message_id, message_id)
        self.assertEqual(d.to_addr, "0.0.0.0:9001")
        self.assertEqual(d.from_addr, "")
        self.assertEqual(d.from_identity, "0c03d360")
        self.assertEqual(d.content, "Call delivered")
        self.assertEqual(d.transport_name, "test_voice")
        self.assertEqual(d.transport_type, None)
        self.assertEqual(d.helper_metadata, {"session_event": "close"})

    @responses.activate
    def test_create_inbound_junebug_unknown_msisdn(self):
        """
        If Junebug sends a new inbound message to the inbound endpoint, for
        an address that doesn't exist in the identity store, then a new
        identity should be created for that address.
        """
        self.add_metrics_response()
        existing_outbound = self.make_outbound()
        out = Outbound.objects.get(pk=existing_outbound)
        out.last_sent_time = out.created_at
        out.save()
        message_id = str(uuid.uuid4())
        post_inbound = {
            "message_id": message_id,
            "reply_to": "test_id",
            "to": "0.0.0.0:9001",
            "from": out.to_addr,
            "content": "Call delivered",
            "channel_id": "test_voice",
            "channel_data": {"session_event": "close"},
        }
        self.add_identity_search_response(out.to_addr, "0c03d360")
        self.add_create_identity_response("0c03d360", out.to_addr)
        response = self.client.post(
            "/api/v1/inbound/",
            json.dumps(post_inbound),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        d = Inbound.objects.last()
        self.assertIsNotNone(d.id)
        self.assertEqual(d.message_id, message_id)
        self.assertEqual(d.to_addr, "0.0.0.0:9001")
        self.assertEqual(d.from_addr, "")
        self.assertEqual(d.from_identity, "0c03d360")
        self.assertEqual(d.content, "Call delivered")
        self.assertEqual(d.transport_name, "test_voice")
        self.assertEqual(d.transport_type, None)
        self.assertEqual(d.helper_metadata, {"session_event": "close"})


class TestWhatsAppMessagesAPI(AuthenticatedAPITestCase):
    @responses.activate
    def test_whatsapp_custom_hsm(self):
        """
        If we send a message with a template key in the metadata, it should
        send an HSM to the WhatsApp API with the parameters specified in the metadata
        """
        # This client is mocked for all tests, but we don't want it mocked for this test
        mocked_get_client = SendMessage.get_client
        SendMessage.get_client = get_client_original

        responses.add(
            method=responses.POST,
            url="http://example.com/v1/messages",
            json={"messages": [{"id": "message-id"}]},
        )
        self.add_metrics_response()
        response = self.client.post(
            reverse("outbound-list"),
            {
                "to_identity": "identity-uuid",
                "to_addr": "+27820001001",
                "content": "ignore",
                "channel": "WHATSAPP",
                "metadata": {
                    "template": {
                        "name": "sbm",
                        "language": "eng_ZA",
                        "variables": ["variable1", "variable2"],
                    }
                },
            },
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        [call] = list(filter(lambda c: "example.com" in c.request.url, responses.calls))
        request = call.request
        self.assertEqual(request.headers["Authorization"], "Bearer http-api-token")
        self.assertEqual(
            json.loads(request.body),
            {
                "to": "27820001001",
                "type": "hsm",
                "hsm": {
                    "namespace": "whatsapp:hsm:test",
                    "element_name": "sbm",
                    "language": {"policy": "deterministic", "code": "eng_ZA"},
                    "localizable_params": [
                        {"default": "variable1"},
                        {"default": "variable2"},
                    ],
                },
            },
        )
        SendMessage.get_client = mocked_get_client


class TestMetricsAPI(AuthenticatedAPITestCase):
    def test_metrics_read(self):
        # Setup
        # Execute
        response = self.client.get("/api/metrics/", content_type="application/json")
        # Check
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data["metrics_available"],
            [
                "vumimessage.tries.sum",
                "vumimessage.maxretries.sum",
                "vumimessage.obd.tries.sum",
                "message.failures.sum",
                "message.sent.sum",
                "sender.send_message.connection_error.sum",
                "sender.send_message.http_error.400.sum",
                "sender.send_message.http_error.401.sum",
                "sender.send_message.http_error.403.sum",
                "sender.send_message.http_error.404.sum",
                "sender.send_message.http_error.500.sum",
                "sender.send_message.timeout.sum",
            ],
        )

    @responses.activate
    def test_post_metrics(self):
        # Setup
        # deactivate Testsession for this test
        self.session = None
        responses.add(
            responses.POST,
            "http://metrics-url/metrics/",
            json={"foo": "bar"},
            status=200,
            content_type="application/json",
        )
        # Execute
        response = self.client.post("/api/metrics/", content_type="application/json")
        # Check
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["scheduled_metrics_initiated"], True)


class TestMetrics(AuthenticatedAPITestCase):
    @responses.activate
    def test_direct_fire(self):
        """
        When calling the `fire_metric` task, a call should be make to the
        metrics store with the details provided in the task arguments.
        """
        # Setup
        self.add_metrics_response()
        # Execute
        result = fire_metric.apply_async(
            kwargs={"metric_name": "foo.last", "metric_value": 1}
        )
        # Check
        request = responses.calls[-1].request
        self.check_request(request, "POST", data={"foo.last": 1.0})
        self.assertEqual(result.get(), "Fired metric <foo.last> with value <1.0>")


class TestHealthcheckAPI(AuthenticatedAPITestCase):
    def test_healthcheck_read(self):
        # Setup
        # Execute
        response = self.client.get("/api/health/", content_type="application/json")
        # Check
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["up"], True)
        self.assertEqual(response.data["result"]["database"], "Accessible")


class TestUserCreation(AuthenticatedAPITestCase):
    def test_create_user_and_token(self):
        # Setup
        user_request = {"email": "test@example.org"}
        # Execute
        request = self.adminclient.post("/api/v1/user/token/", user_request)
        token = request.json().get("token", None)
        # Check
        self.assertIsNotNone(token, "Could not receive authentication token on post.")
        self.assertEqual(
            request.status_code,
            201,
            "Status code on /api/v1/user/token/ was %s (should be 201)."
            % request.status_code,
        )

    def test_create_user_and_token_fail_nonadmin(self):
        # Setup
        user_request = {"email": "test@example.org"}
        # Execute
        request = self.client.post("/api/v1/user/token/", user_request)
        error = request.json().get("detail", None)
        # Check
        self.assertIsNotNone(error, "Could not receive error on post.")
        self.assertEqual(
            error,
            "You do not have permission to perform this action.",
            "Error message was unexpected: %s." % error,
        )

    def test_create_user_and_token_not_created(self):
        # Setup
        user_request = {"email": "test@example.org"}
        # Execute
        request = self.adminclient.post("/api/v1/user/token/", user_request)
        token = request.json().get("token", None)
        # And again, to get the same token
        request2 = self.adminclient.post("/api/v1/user/token/", user_request)
        token2 = request2.json().get("token", None)

        # Check
        self.assertEqual(
            token, token2, "Tokens are not equal, should be the same as not recreated."
        )

    def test_create_user_new_token_nonadmin(self):
        # Setup
        user_request = {"email": "test@example.org"}
        request = self.adminclient.post("/api/v1/user/token/", user_request)
        token = request.json().get("token", None)
        cleanclient = APIClient()
        cleanclient.credentials(HTTP_AUTHORIZATION="Token %s" % token)
        # Execute
        request = cleanclient.post("/api/v1/user/token/", user_request)
        error = request.json().get("detail", None)
        # Check
        # new user should not be admin
        self.assertIsNotNone(error, "Could not receive error on post.")
        self.assertEqual(
            error,
            "You do not have permission to perform this action.",
            "Error message was unexpected: %s." % error,
        )


class TestFormatter(TestCase):
    @override_settings(VOICE_TO_ADDR_FORMATTER="message_sender.formatters.noop")
    def test_noop(self):
        cb = load_callable(settings.VOICE_TO_ADDR_FORMATTER)
        self.assertEqual(cb("12345"), "12345")

    @override_settings(
        VOICE_TO_ADDR_FORMATTER="message_sender.formatters.vas2nets_voice"
    )
    def test_vas2nets_voice(self):
        cb = load_callable(settings.VOICE_TO_ADDR_FORMATTER)
        self.assertEqual(cb("+23456"), "9056")
        self.assertEqual(cb("23456"), "9056")

    @override_settings(
        VOICE_TO_ADDR_FORMATTER="message_sender.formatters.vas2nets_text"
    )
    def test_vas2nets_text(self):
        cb = load_callable(settings.VOICE_TO_ADDR_FORMATTER)
        self.assertEqual(cb("+23456"), "23456")
        self.assertEqual(cb("23456"), "23456")


class TestFactory(TestCase):
    def setUp(self):
        super(TestFactory, self).setUp()
        make_channels()

    def test_create_junebug_text(self):
        channel = Channel.objects.get(channel_id="JUNE_TEXT")
        message_sender = MessageClientFactory.create(channel)
        self.assertTrue(isinstance(message_sender, JunebugApiSender))
        self.assertEqual(message_sender.api_url, "http://example.com/")
        self.assertEqual(message_sender.auth, ("username", "password"))

    def test_create_junebug_voice(self):
        channel = Channel.objects.get(channel_id="JUNE_VOICE")
        message_sender = MessageClientFactory.create(channel)
        self.assertTrue(isinstance(message_sender, JunebugApiSender))
        self.assertEqual(message_sender.api_url, "http://example.com/")
        self.assertEqual(message_sender.auth, ("username", "password"))

    def test_create_vumi_text(self):
        channel = Channel.objects.get(channel_id="VUMI_TEXT")
        message_sender = MessageClientFactory.create(channel)
        self.assertTrue(isinstance(message_sender, HttpApiSender))
        self.assertEqual(message_sender.api_url, "http://example.com/")
        self.assertEqual(message_sender.account_key, "account-key")
        self.assertEqual(message_sender.conversation_key, "conv-key")
        self.assertEqual(message_sender.conversation_token, "account-token")

    def test_create_vumi_voice(self):
        channel = Channel.objects.get(channel_id="VUMI_VOICE")
        message_sender = MessageClientFactory.create(channel)
        self.assertTrue(isinstance(message_sender, HttpApiSender))
        self.assertEqual(message_sender.api_url, "http://example.com/")
        self.assertEqual(message_sender.account_key, "account-key")
        self.assertEqual(message_sender.conversation_key, "conv-key")
        self.assertEqual(message_sender.conversation_token, "account-token")

    def test_create_http_api_voice(self):
        channel = Channel.objects.get(channel_id="HTTP_API_VOICE")
        message_sender = MessageClientFactory.create(channel)
        self.assertTrue(isinstance(message_sender, HttpApiSender))
        self.assertEqual(message_sender.api_url, "http://example.com/")
        self.assertEqual(message_sender.auth, ("username", "password"))

    def test_create_http_api_text(self):
        channel = Channel.objects.get(channel_id="HTTP_API_TEXT")
        message_sender = MessageClientFactory.create(channel)
        self.assertTrue(isinstance(message_sender, HttpApiSender))
        self.assertEqual(message_sender.api_url, "http://example.com/")
        self.assertEqual(message_sender.auth, ("username", "password"))

    def test_create_whatsapp_api(self):
        channel = Channel.objects.get(channel_id="WHATSAPP")
        message_sender = MessageClientFactory.create(channel)
        self.assertTrue(isinstance(message_sender, WhatsAppApiSender))
        self.assertEqual(message_sender.api_url, "http://example.com/")
        self.assertEqual(message_sender.token, "http-api-token")
        self.assertEqual(message_sender.hsm_namespace, "whatsapp:hsm:test")
        self.assertEqual(message_sender.hsm_element_name, "test")

    def test_create_no_backend_type_specified_default(self):
        """
        If no message backend is specified, it should use the default channel.
        """
        message_sender = MessageClientFactory.create()
        self.assertTrue(isinstance(message_sender, JunebugApiSender))
        self.assertEqual(message_sender.api_url, "http://example.com/")
        self.assertEqual(message_sender.auth, ("username", "password"))


class TestGenericHttpApiSender(TestCase):
    def setUp(self):
        super(TestGenericHttpApiSender, self).setUp()
        make_channels()

    @responses.activate
    def test_send_text(self):
        """
        Using the send_text function should send a request to the api with the
        correct JSON data.
        """
        responses.add(
            responses.POST,
            "http://example.com/",
            json={"result": {"message_id": "message-uuid"}},
            status=200,
            content_type="application/json",
        )

        channel = Channel.objects.get(channel_id="HTTP_API_TEXT")
        message_sender = MessageClientFactory.create(channel)
        res = message_sender.send_text("+1234", "Test", session_event="new")

        self.assertEqual(res["message_id"], "message-uuid")

        [r] = responses.calls
        r = json.loads(r.request.body)
        self.assertEqual(r["to"], "+1234")
        self.assertEqual(r["from"], "+4321")
        self.assertEqual(r["content"], "Test")
        self.assertEqual(r["channel_data"]["session_event"], "new")

    @responses.activate
    def test_send_voice(self):
        """
        Using the send_voice function should send a request to the api with the
        correct JSON data.
        """
        responses.add(
            responses.POST,
            "http://example.com/",
            json={"result": {"message_id": "message-uuid"}},
            status=200,
            content_type="application/json",
        )

        channel = Channel.objects.get(channel_id="HTTP_API_VOICE")
        message_sender = MessageClientFactory.create(channel)
        res = message_sender.send_voice(
            "+1234", "", speech_url="http://sbm.com/test.mp3", session_event="new"
        )

        self.assertEqual(res["message_id"], "message-uuid")

        [r] = responses.calls
        r = json.loads(r.request.body)
        self.assertEqual(r["to"], "+1234")
        self.assertEqual(r["from"], "+4321")
        self.assertEqual(r["content"], "")
        self.assertEqual(r["channel_data"]["session_event"], "new")
        self.assertEqual(
            r["channel_data"]["voice"]["speech_url"], "http://sbm.com/test.mp3"
        )

    @responses.activate
    def test_send_voice_multiple(self):
        """
        Using the send_voice function should send a request to the api with the
        correct JSON data.
        """
        responses.add(
            responses.POST,
            "http://example.com/",
            json={"result": {"message_id": "message-uuid"}},
            status=200,
            content_type="application/json",
        )

        channel = Channel.objects.get(channel_id="HTTP_API_VOICE")
        message_sender = MessageClientFactory.create(channel)
        res = message_sender.send_voice(
            "+1234",
            "",
            speech_url=["http://sbm.com/test1.mp3", "http://sbm.com/test2.mp3"],
            session_event="new",
        )

        self.assertEqual(res["message_id"], "message-uuid")

        [r] = responses.calls
        r = json.loads(r.request.body)
        self.assertEqual(r["to"], "+1234")
        self.assertEqual(r["from"], "+4321")
        self.assertEqual(r["content"], "")
        self.assertEqual(r["channel_data"]["session_event"], "new")
        self.assertEqual(
            r["channel_data"]["voice"]["speech_url"],
            ["http://sbm.com/test1.mp3", "http://sbm.com/test2.mp3"],
        )

    @responses.activate
    def test_send_voice_override_payload(self):
        """
        Using the send_voice function should send a request to the api with the
        correct JSON data based on the override_payload setting in the channel.
        The full path should be stripped if the STRIP_FILEPATH key is present.
        """
        responses.add(
            responses.POST,
            "http://example.com/",
            json={"result": {"message_id": "message-uuid"}},
            status=200,
            content_type="application/json",
        )

        http_channel_override_payload = {
            "channel_id": "HTTP_API_VOICE_OP",
            "channel_type": Channel.HTTP_API_TYPE,
            "default": False,
            "configuration": {
                "HTTP_API_URL": "http://example.com/",
                "HTTP_API_AUTH": ("username", "password"),
                "HTTP_API_FROM": "+4321",
                "OVERRIDE_PAYLOAD": {
                    "mobile_no": "to",
                    "filename": "channel_data.voice.speech_url",
                    "nested_data": {"from_addr": "from", "unknown": "unknown"},
                },
                "STRIP_FILEPATH": "true",
            },
            "concurrency_limit": 2,
            "message_timeout": 20,
            "message_delay": 10,
        }
        channel = Channel.objects.create(**http_channel_override_payload)

        message_sender = MessageClientFactory.create(channel)
        res = message_sender.send_voice(
            "+1234", "", speech_url="http://sbm.com/test.mp3", session_event="new"
        )

        self.assertEqual(res["message_id"], "message-uuid")

        [r] = responses.calls
        r = json.loads(r.request.body)
        self.assertEqual(r["mobile_no"], "+1234")
        self.assertEqual(r["nested_data"]["from_addr"], "+4321")
        self.assertEqual(r["nested_data"]["unknown"], "unknown")
        self.assertEqual(r["filename"], "test.mp3")

    @responses.activate
    def test_send_voice_override_payload_multiple_urls(self):
        """
        Using the send_voice function should send a request to the api with the
        correct JSON data based on the override_payload setting in the channel.
        The full path should be stripped if the STRIP_FILEPATH key is present,
        even if there is a list of urls.
        """
        responses.add(
            responses.POST,
            "http://example.com/",
            json={"result": {"message_id": "message-uuid"}},
            status=200,
            content_type="application/json",
        )

        http_channel_override_payload = {
            "channel_id": "HTTP_API_VOICE_OP",
            "channel_type": Channel.HTTP_API_TYPE,
            "default": False,
            "configuration": {
                "HTTP_API_URL": "http://example.com/",
                "HTTP_API_AUTH": ("username", "password"),
                "HTTP_API_FROM": "+4321",
                "OVERRIDE_PAYLOAD": {
                    "mobile_no": "to",
                    "filename": "channel_data.voice.speech_url",
                    "nested_data": {"from_addr": "from", "unknown": "unknown"},
                },
                "STRIP_FILEPATH": "true",
            },
            "concurrency_limit": 2,
            "message_timeout": 20,
            "message_delay": 10,
        }
        channel = Channel.objects.create(**http_channel_override_payload)

        message_sender = MessageClientFactory.create(channel)
        res = message_sender.send_voice(
            "+1234",
            "",
            speech_url=["http://sbm.com/test1.mp3", "http://sbm.com/test2.mp3"],
            session_event="new",
        )

        self.assertEqual(res["message_id"], "message-uuid")

        [r] = responses.calls
        r = json.loads(r.request.body)
        self.assertEqual(r["mobile_no"], "+1234")
        self.assertEqual(r["nested_data"]["from_addr"], "+4321")
        self.assertEqual(r["nested_data"]["unknown"], "unknown")
        self.assertEqual(r["filename"], ["test1.mp3", "test2.mp3"])

    @responses.activate
    def test_send_voice_strip_filepath_language(self):
        """
        Using the send_voice function should send a request to the api with the
        correct JSON data. The full path should be stripped if the
        STRIP_FILEPATH key is present, even if there is a list of urls. If
        there is a language code present it should not be removed.
        """
        responses.add(
            responses.POST,
            "http://example.com/",
            json={"result": {"message_id": "message-uuid"}},
            status=200,
            content_type="application/json",
        )

        http_channel_override_payload = {
            "channel_id": "HTTP_API_VOICE_OP",
            "channel_type": Channel.HTTP_API_TYPE,
            "default": False,
            "configuration": {
                "HTTP_API_URL": "http://example.com/",
                "HTTP_API_AUTH": ("username", "password"),
                "HTTP_API_FROM": "+4321",
                "STRIP_FILEPATH": "true",
            },
            "concurrency_limit": 2,
            "message_timeout": 20,
            "message_delay": 10,
        }
        channel = Channel.objects.create(**http_channel_override_payload)

        message_sender = MessageClientFactory.create(channel)
        res = message_sender.send_voice(
            "+1234",
            "",
            speech_url=[
                "http://sbm.com/eng_ZA/test1.mp3",
                "http://sbm.com/zul_ZA/nested/test2.mp3",
                "http://sbm.com/test3.mp3",
            ],
            session_event="new",
        )

        self.assertEqual(res["message_id"], "message-uuid")

        [r] = responses.calls
        r = json.loads(r.request.body)
        self.assertEqual(
            r["channel_data"]["voice"]["speech_url"],
            ["eng_ZA/test1.mp3", "zul_ZA/nested/test2.mp3", "test3.mp3"],
        )

    @responses.activate
    def test_send_voice_strip_filepath_unicode(self):
        """
        Using the send_voice function should send a request to the api with the
        correct JSON data. The full path should be stripped if the
        STRIP_FILEPATH key is present, even if it is a unicode.
        """
        responses.add(
            responses.POST,
            "http://example.com/",
            json={"result": {"message_id": "message-uuid"}},
            status=200,
            content_type="application/json",
        )

        http_channel_override_payload = {
            "channel_id": "HTTP_API_VOICE_OP",
            "channel_type": Channel.HTTP_API_TYPE,
            "default": False,
            "configuration": {
                "HTTP_API_URL": "http://example.com/",
                "HTTP_API_AUTH": ("username", "password"),
                "HTTP_API_FROM": "+4321",
                "STRIP_FILEPATH": "true",
            },
            "concurrency_limit": 2,
            "message_timeout": 20,
            "message_delay": 10,
        }
        channel = Channel.objects.create(**http_channel_override_payload)

        message_sender = MessageClientFactory.create(channel)
        res = message_sender.send_voice(
            "+1234", "", speech_url="http://sbm.com/test.mp3", session_event="new"
        )

        self.assertEqual(res["message_id"], "message-uuid")

        [r] = responses.calls
        r = json.loads(r.request.body)
        self.assertEqual(r["channel_data"]["voice"]["speech_url"], "test.mp3")

    def test_fire_metric(self):
        """
        Using the fire_metric function should result in an exception being
        raised, since the generic http api doesn't support metrics sending.
        """
        channel = Channel.objects.get(channel_id="HTTP_API_VOICE")
        message_sender = MessageClientFactory.create(channel)
        self.assertRaises(
            HttpApiSenderException,
            message_sender.fire_metric,
            "foo.bar",
            3.0,
            agg="sum",
        )

    def test_send_image(self):
        """
        Using the send_image function should result in an exception being
        raised, since the generic http api doesn't support image sending.
        """
        channel = Channel.objects.get(channel_id="HTTP_API_VOICE")
        message_sender = MessageClientFactory.create(channel)
        self.assertRaises(
            HttpApiSenderException,
            message_sender.send_image,
            "+1234",
            "Test",
            image_url="http://test.jpg",
        )


class TestJunebugAPISender(TestCase):
    def setUp(self):
        super(TestJunebugAPISender, self).setUp()
        make_channels()

    @responses.activate
    def test_send_text(self):
        """
        Using the send_text function should send a request to Junebug with the
        correct JSON data.
        """
        responses.add(
            responses.POST,
            "http://example.com/",
            json={"result": {"message_id": "message-uuid"}},
            status=200,
            content_type="application/json",
        )

        channel = Channel.objects.get(channel_id="JUNE_TEXT")
        message_sender = MessageClientFactory.create(channel)
        res = message_sender.send_text("+1234", "Test", session_event="resume")

        self.assertEqual(res["message_id"], "message-uuid")

        [r] = responses.calls
        r = json.loads(r.request.body)
        self.assertEqual(r["to"], "+1234")
        self.assertEqual(r["from"], "+4321")
        self.assertEqual(r["content"], "Test")
        self.assertEqual(r["channel_data"]["session_event"], "resume")
        self.assertEqual(r["event_url"], "http://example.com/api/v1/events/junebug")

    @responses.activate
    def test_send_voice(self):
        """
        Using the send_voice function should send a request to Junebug with the
        correct JSON data.
        """
        responses.add(
            responses.POST,
            "http://example.com/",
            json={"result": {"message_id": "message-uuid"}},
            status=200,
            content_type="application/json",
        )

        channel = Channel.objects.get(channel_id="JUNE_VOICE")
        message_sender = MessageClientFactory.create(channel)
        res = message_sender.send_voice(
            "+1234",
            "Test",
            speech_url="http://test.mp3",
            wait_for="#",
            session_event="resume",
        )

        self.assertEqual(res["message_id"], "message-uuid")

        [r] = responses.calls
        r = json.loads(r.request.body)
        self.assertEqual(r["to"], "+1234")
        self.assertEqual(r["from"], "+4321")
        self.assertEqual(r["content"], "Test")
        self.assertEqual(r["channel_data"]["session_event"], "resume")
        self.assertEqual(r["channel_data"]["voice"]["speech_url"], "http://test.mp3")
        self.assertEqual(r["channel_data"]["voice"]["wait_for"], "#")
        self.assertEqual(r["event_url"], "http://example.com/api/v1/events/junebug")

    def test_fire_metric(self):
        """
        Using the fire_metric function should result in an exception being
        raised, since Junebug doesn't support metrics sending.
        """
        channel = Channel.objects.get(channel_id="JUNE_VOICE")
        message_sender = MessageClientFactory.create(channel)
        self.assertRaises(
            HttpApiSenderException,
            message_sender.fire_metric,
            "foo.bar",
            3.0,
            agg="sum",
        )


class TestWassupAPISender(TestCase):
    def setUp(self):
        super(TestWassupAPISender, self).setUp()
        make_channels()

    @responses.activate
    def test_send_text(self):
        """
        Using the send_text function should send a request to wassup with the
        correct JSON data.
        """
        responses.add(
            responses.POST,
            "http://example.com/api/v1/hsms/the-uuid/send/",
            json={"uuid": "message-uuid"},
            status=200,
            content_type="application/json",
        )

        channel = Channel.objects.get(channel_id="WASSUP_API")
        message_sender = MessageClientFactory.create(channel)
        res = message_sender.send_text("+1234", "Test", session_event="resume")

        self.assertEqual(res["message_id"], "message-uuid")

        [r] = responses.calls
        r = json.loads(r.request.body.decode())
        self.assertEqual(r["to_addr"], "+1234")
        self.assertEqual(r["localizable_params"], [{"default": "Test"}])

    @responses.activate
    def test_send_non_hsm_text(self):
        """
        Using the send_text function should send a non hsm request to wassup
        with the correct JSON data.
        """
        responses.add(
            responses.POST,
            "http://example.com/api/v1/messages/",
            json={"uuid": "message-uuid"},
            status=200,
            content_type="application/json",
        )

        channel = Channel.objects.get(channel_id="WASSUP_API_NON_HSM")
        message_sender = MessageClientFactory.create(channel)
        res = message_sender.send_text(
            "+1234", "Test non HSM message", session_event="resume"
        )

        self.assertEqual(res["message_id"], "message-uuid")

        [r] = responses.calls
        r = json.loads(r.request.body.decode())
        self.assertEqual(r["to_addr"], "+1234")
        self.assertEqual(r["number"], "+4321")
        self.assertEqual(r["content"], "Test non HSM message")

    @responses.activate
    def test_send_image(self):
        """
        Using the send_image function should send a request to wassup with the
        correct JSON data.
        """
        responses.add(
            responses.GET,
            "http://test.jpg",
            body="",
            status=200,
            content_type="image/jpeg",
            stream=True,
        )

        responses.add(
            responses.POST,
            "http://example.com/api/v1/messages/",
            json={"uuid": "message-uuid"},
            status=200,
            content_type="application/json",
        )

        channel = Channel.objects.get(channel_id="WASSUP_API")
        message_sender = MessageClientFactory.create(channel)
        res = message_sender.send_image("+1234", "Test", image_url="http://test.jpg")

        self.assertEqual(res["message_id"], "message-uuid")

        [jpg, r] = responses.calls
        body = r.request.body.decode()
        self.assertTrue("+1234" in body)
        self.assertTrue("+4321" in body)
        self.assertTrue("image_attachment" in body)
        self.assertTrue('filename="test.jpg"' in body)
        self.assertTrue("Content-Type: image/jpeg" in body)

    @responses.activate
    def test_send_voice(self):
        """
        Using the send_voice function should send a request to wassup with the
        correct JSON data.
        """

        responses.add(
            responses.GET,
            "http://test.mp3",
            body="",
            status=200,
            content_type="audio/mp3",
            stream=True,
        )

        responses.add(
            responses.POST,
            "http://example.com/api/v1/messages/",
            json={"uuid": "message-uuid"},
            status=200,
            content_type="application/json",
        )

        channel = Channel.objects.get(channel_id="WASSUP_API")
        message_sender = MessageClientFactory.create(channel)
        res = message_sender.send_voice(
            "+1234",
            "Test",
            speech_url="http://test.mp3",
            wait_for="#",
            session_event="resume",
        )

        self.assertEqual(res["message_id"], "message-uuid")

        [mp3, r] = responses.calls
        body = r.request.body.decode()
        self.assertTrue("+1234" in body)
        self.assertTrue("+4321" in body)
        self.assertTrue("audio_attachment" in body)

    def test_fire_metric(self):
        """
        Using the fire_metric function should result in an exception being
        raised, since wassup doesn't support metrics sending.
        """
        channel = Channel.objects.get(channel_id="WASSUP_API")
        message_sender = MessageClientFactory.create(channel)
        self.assertRaises(
            WassupApiSenderException,
            message_sender.fire_metric,
            "foo.bar",
            3.0,
            agg="sum",
        )


class TestWassupEventsApi(AuthenticatedAPITestCase):
    def test_event_missing_fields(self):
        """
        If there are missing fields in the request, and error response should
        be returned.
        """
        response = self.client.post(
            reverse("wassup-events"), json.dumps({}), content_type="application/json"
        )
        self.assertEqual(
            json.loads(response.content.decode()),
            {
                "accepted": False,
                "reason": {
                    "data": ["This field is required."],
                    "hook": ["This field is required."],
                },
            },
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_event_no_message(self):
        """
        If we cannot find the message for the event, and error response should
        be returned.
        """
        event = {
            "hook": {"event": "message.direct_outbound.status"},
            "data": {
                "message_uuid": "bad-message-id",
                "status": "sent",
                "timestamp": "2018-05-04T16:00:18Z",
            },
        }
        response = self.client.post(
            reverse("wassup-events"), json.dumps(event), content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            json.loads(response.content.decode()),
            {"accepted": False, "reason": "Cannot find message for ID bad-message-id"},
        )

    @patch("message_sender.views.fire_delivery_hook")
    def test_event_ack(self, mock_hook):
        """A submitted event should update the message object accordingly."""
        existing = self.make_outbound()

        d = Outbound.objects.get(pk=existing)
        event = {
            "hook": {"event": "message.direct_outbound.status"},
            "data": {
                "message_uuid": d.vumi_message_id,
                "status": "sent",
                "timestamp": "2018-05-04T16:00:18Z",
            },
        }
        response = self.client.post(
            reverse("wassup-events"), json.dumps(event), content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        d = Outbound.objects.get(pk=existing)
        self.assertEqual(d.delivered, True)
        self.assertEqual(d.attempts, 1)
        self.assertEqual(d.metadata["ack_timestamp"], "2018-05-04T16:00:18Z")
        self.assertEqual(
            False,
            self.check_logs(
                "Message: 'Simple outbound message' sent to '+27820000123'"
            ),
        )
        mock_hook.assert_called_once_with(d)

    @responses.activate
    @patch("message_sender.views.fire_delivery_hook")
    def test_event_nack(self, mock_hook):
        """
        A rejected event should retry and update the message object accordingly
        """
        self.add_metrics_response()
        existing = self.make_outbound()
        d = Outbound.objects.get(pk=existing)
        post_save.connect(
            psh_fire_msg_action_if_new,
            sender=Outbound,
            dispatch_uid="psh_fire_msg_action_if_new",
        )
        event = {
            "hook": {"event": "message.direct_outbound.status"},
            "data": {
                "status": "unsent",
                "message_uuid": d.vumi_message_id,
                "timestamp": "2018-05-04T16:00:18Z",
                "description": "stars not aligned",
            },
        }

        response = self.client.post(
            reverse("wassup-events"), json.dumps(event), content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        c = Outbound.objects.get(pk=existing)
        self.assertEqual(c.delivered, False)
        self.assertEqual(c.attempts, 2)
        self.assertEqual(c.metadata["nack_reason"], "stars not aligned")
        self.assertEqual(
            True,
            self.check_logs(
                "Message: 'Simple outbound message' sent to '+27820000123' "
                "[session_event: new]"
            ),
        )
        mock_hook.assert_called_once_with(d)

    @patch("message_sender.views.fire_delivery_hook")
    def test_event_delivery_succeeded(self, mock_hook):
        """A successful delivery should update the message accordingly."""
        existing = self.make_outbound()
        d = Outbound.objects.get(pk=existing)
        event = {
            "hook": {"event": "message.direct_outbound.status"},
            "data": {
                "status": "delivered",
                "message_uuid": d.vumi_message_id,
                "timestamp": "2018-05-04T16:00:18Z",
            },
        }
        response = self.client.post(
            reverse("wassup-events"), json.dumps(event), content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        d = Outbound.objects.get(pk=existing)
        self.assertEqual(d.delivered, True)
        self.assertEqual(d.attempts, 1)
        self.assertEqual(d.metadata["delivery_timestamp"], "2018-05-04T16:00:18Z")
        self.assertEqual(
            False,
            self.check_logs(
                "Message: 'Simple outbound message' sent to '+27820000123'"
            ),
        )
        mock_hook.assert_called_once_with(d)

    @responses.activate
    @patch("message_sender.views.fire_delivery_hook")
    def test_event_delivery_failed(self, mock_hook):
        """
        A failed delivery should retry and update the message accordingly.
        """
        self.add_metrics_response()
        existing = self.make_outbound()
        d = Outbound.objects.get(pk=existing)
        event = {
            "hook": {"event": "message.direct_outbound.status"},
            "data": {
                "message_uuid": d.vumi_message_id,
                "status": "failed",
                "description": "computer said no",
                "timestamp": "2018-05-04T16:00:18Z",
            },
        }

        response = self.client.post(
            reverse("wassup-events"), json.dumps(event), content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        d = Outbound.objects.get(pk=existing)
        self.assertEqual(d.delivered, False)
        self.assertEqual(d.attempts, 2)
        self.assertEqual(d.metadata["delivery_failed_reason"], "computer said no")
        self.assertEqual(
            False,
            self.check_logs(
                "Message: 'Simple outbound message' sent to '+27820000123'"
            ),
        )
        mock_hook.assert_called_once_with(d)

    @responses.activate
    def test_create_inbound_wassup_message(self):
        """
        If wassup send an inbound message to the inbound endpoint, then a
        new Inbound should be created with the specified parameters.
        """
        channel = Channel.objects.get(channel_id="WASSUP_API")

        self.add_metrics_response()
        message_id = str(uuid.uuid4())

        event = {
            "hook": {"event": "message.inbound"},
            "data": {
                "uuid": message_id,
                "content": "the content",
                "in_reply_to": None,
                "metadata": {},
                "from_addr": "+27820000123456789",
                "to_addr": "+27000000000",
            },
        }

        self.add_identity_search_response("+27820000123456789", "0c03d360")
        response = self.client.post(
            reverse("channels-inbound", kwargs={"channel_id": channel.channel_id}),
            json.dumps(event),
            content_type="application/json",
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        d = Inbound.objects.last()
        self.assertIsNotNone(d.id)
        self.assertEqual(d.message_id, message_id)
        self.assertEqual(d.to_addr, "+27000000000")
        self.assertEqual(d.from_identity, "0c03d360")
        self.assertEqual(d.content, "the content")
        self.assertEqual(d.transport_name, "")
        self.assertEqual(d.transport_type, None)
        self.assertEqual(d.helper_metadata, {})

    @responses.activate
    def test_create_inbound_wassup_unknown_msisdn(self):
        """
        If wassup sends a new inbound message to the inbound endpoint, for
        an address that doesn't exist in the identity store, then a new
        identity should be created for that address.
        """
        channel = Channel.objects.get(channel_id="WASSUP_API")

        self.add_metrics_response()
        message_id = str(uuid.uuid4())

        event = {
            "hook": {"event": "message.inbound"},
            "data": {
                "uuid": message_id,
                "content": "the content",
                "in_reply_to": None,
                "metadata": {},
                "from_addr": "+27820000123456789",
                "to_addr": "+27000000000",
            },
        }

        self.add_identity_search_response("+27820000123456789", "0c03d360")
        self.add_create_identity_response("0c03d360", "+27820000123456789")
        response = self.client.post(
            reverse("channels-inbound", kwargs={"channel_id": channel.channel_id}),
            json.dumps(event),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        d = Inbound.objects.last()
        self.assertIsNotNone(d.id)
        self.assertEqual(d.message_id, message_id)
        self.assertEqual(d.to_addr, "+27000000000")
        self.assertEqual(d.from_identity, "0c03d360")
        self.assertEqual(d.content, "the content")
        self.assertEqual(d.transport_name, "")
        self.assertEqual(d.transport_type, None)
        self.assertEqual(d.helper_metadata, {})


class TestConcurrencyLimiter(AuthenticatedAPITestCase):
    def make_outbound(self, to_addr, channel=None):

        if channel:
            channel = Channel.objects.get(channel_id=channel)

        self.add_identity_search_response(to_addr, "098734738")

        self._replace_post_save_hooks_outbound()  # don't let fixtures fire
        outbound_message = {
            "to_addr": to_addr,
            "vumi_message_id": "075a32da-e1e4-4424-be46-1d09b71056fd",
            "content": "Simple outbound message",
            "delivered": False,
            "metadata": {"voice_speech_url": "http://test.com"},
            "channel": channel,
        }
        outbound = Outbound.objects.create(**outbound_message)
        self._restore_post_save_hooks_outbound()  # let tests fire tasks
        return outbound

    def set_cache_entry(self, msg_type, bucket, value):
        key = "%s_messages_at_%s" % (msg_type, bucket)
        self.fake_cache.cache_data[key] = value

    def setUp(self):
        super(TestConcurrencyLimiter, self).setUp()
        self.fake_cache = MockCache()

    @responses.activate
    @patch("time.time", MagicMock(return_value=1479131658.000000))
    @patch("django.core.cache.cache.get")
    @patch("django.core.cache.cache.add")
    @patch("django.core.cache.cache.incr")
    def test_limiter_limit_not_reached(self, mock_incr, mock_add, mock_get):
        """
        Messages under the limit should get sent.
        """
        self.add_metrics_response()
        # Fake cache calls
        mock_incr.side_effect = self.fake_cache.incr
        mock_add.side_effect = self.fake_cache.add
        mock_get.side_effect = self.fake_cache.get

        outbound1 = self.make_outbound(to_addr="+27820000123", channel="JUNE_VOICE2")
        outbound2 = self.make_outbound(to_addr="+27987", channel="JUNE_VOICE2")

        send_message(outbound1.pk)
        send_message(outbound2.pk)

        self.assertTrue(
            self.check_logs(
                "Message: '%s' sent to '%s' [session_event: new] [voice: "
                "{'speech_url': 'http://test.com'}]"
                % (outbound1.content, outbound1.to_addr)
            )
        )
        self.assertTrue(
            self.check_logs(
                "Message: '%s' sent to '%s' [session_event: new] [voice: "
                "{'speech_url': 'http://test.com'}]"
                % (outbound2.content, outbound2.to_addr)
            )
        )
        outbound1.refresh_from_db()
        self.assertIsNotNone(outbound1.last_sent_time)
        outbound2.refresh_from_db()
        self.assertIsNotNone(outbound2.last_sent_time)
        self.assertEqual(len(self.fake_cache.cache_data), 1)
        bucket = 1479131658 // 60  # time() // bucket_size
        self.assertEqual(
            self.fake_cache.cache_data["JUNE_VOICE2_messages_at_%s" % bucket], 2
        )

    @responses.activate
    @patch("time.time", MagicMock(return_value=1479131658.000000))
    @patch("django.core.cache.cache.get")
    @patch("django.core.cache.cache.add")
    @patch("django.core.cache.cache.incr")
    @patch("message_sender.tasks.send_message.retry")
    def test_limiter_limit_reached(self, mock_retry, mock_incr, mock_add, mock_get):
        """
        Messages under the limit should get sent. Messages over the limit
        should get retried
        """
        self.add_metrics_response()
        mock_retry.side_effect = Retry

        # Fake cache calls
        mock_incr.side_effect = self.fake_cache.incr
        mock_add.side_effect = self.fake_cache.add
        mock_get.side_effect = self.fake_cache.get

        outbound1 = self.make_outbound(to_addr="+27820000123", channel="JUNE_VOICE")
        outbound2 = self.make_outbound(to_addr="+27987", channel="JUNE_VOICE")

        send_message(outbound1.pk)
        with self.assertRaises(Retry):
            send_message(outbound2.pk)
        mock_retry.assert_called_with(countdown=100)

        self.assertTrue(
            self.check_logs(
                "Message: '%s' sent to '%s' [session_event: new] [voice: "
                "{'speech_url': 'http://test.com'}]"
                % (outbound1.content, outbound1.to_addr)
            )
        )
        self.assertFalse(
            self.check_logs(
                "Message: '%s' sent to '%s' [session_event: new] "
                "[voice: {'speech_url': 'http://test.com'}]"
                % (outbound2.content, outbound2.to_addr)
            )
        )
        outbound1.refresh_from_db()
        self.assertIsNotNone(outbound1.last_sent_time)
        outbound2.refresh_from_db()
        self.assertIsNone(outbound2.last_sent_time)
        self.assertEqual(len(self.fake_cache.cache_data), 1)
        bucket = 1479131658 // 60  # time() // bucket_size
        self.assertEqual(
            self.fake_cache.cache_data["JUNE_VOICE_messages_at_%s" % bucket], 1
        )

    @patch("time.time", MagicMock(return_value=1479131640.000000))
    @patch("django.core.cache.cache.get")
    def test_limiter_buckets(self, mock_get):
        """
        The correct buckets should count towards the message count.
        """

        # Fake cache calls
        mock_get.side_effect = self.fake_cache.get
        now = 1479131640

        self.set_cache_entry("JUNE_VOICE", (now - 200) // 60, 1)  # Too old
        self.set_cache_entry("JUNE_VOICE", (now - 121) // 60, 10)  # Over delay
        self.set_cache_entry(
            "JUNE_VOICE", (now - 120) // 60, 100
        )  # Within delay # noqa
        self.set_cache_entry("JUNE_VOICE", now // 60, 1000)  # Now
        self.set_cache_entry("JUNE_VOICE", (now + 60) // 60, 10000)  # In future # noqa

        channel = Channel.objects.get(channel_id="JUNE_VOICE")
        count = ConcurrencyLimiter.get_current_message_count(channel)
        self.assertEqual(count, 1100)

    @patch("time.time", MagicMock(return_value=1479131658.000000))
    @patch("django.core.cache.cache.get_or_set")
    @patch("django.core.cache.cache.decr")
    def test_limiter_decr_count(self, mock_decr, mock_get_or_set):
        """
        Events for messages should decrement the counter unless the message is
        too old.
        """

        # Fake cache calls
        mock_get_or_set.side_effect = self.fake_cache.get_or_set
        mock_decr.side_effect = self.fake_cache.decr

        self.set_cache_entry("JUNE_VOICE", 1479131535 // 60, 1)  # Past delay
        self.set_cache_entry("JUNE_VOICE", 1479131588 // 60, 1)  # Within delay
        self.set_cache_entry(
            "JUNE_VOICE", 1479131648 // 60, -0
        )  # Invalid value  # noqa

        channel = Channel.objects.get(channel_id="JUNE_VOICE")

        def get_utc(timestamp):
            return datetime.fromtimestamp(timestamp).replace(
                tzinfo=timezone.now().tzinfo
            )

        ConcurrencyLimiter.decr_message_count(channel, get_utc(1479131535))
        ConcurrencyLimiter.decr_message_count(channel, get_utc(1479131588))
        ConcurrencyLimiter.decr_message_count(channel, get_utc(1479131608))

        self.assertEqual(
            self.fake_cache.cache_data,
            {
                "JUNE_VOICE_messages_at_24652192": 1,
                "JUNE_VOICE_messages_at_24652193": 0,
                "JUNE_VOICE_messages_at_24652194": 0,
            },
        )

    @responses.activate
    def test_event_nack_concurrency_decr(self):
        """
        When receiving a nack, we should decrement the correct concurrency
        limiter for the channel that the nack is for.
        """
        self.add_metrics_response()
        channel = Channel.objects.get(channel_id="VUMI_VOICE")
        outbound_message = {
            "to_addr": "+27820000123",
            "vumi_message_id": "08b34de7-c6da-4853-a74d-9458533ed169",
            "content": "Simple outbound message",
            "channel": channel,
            "delivered": False,
            "attempts": 3,
            "metadata": {},
        }
        failed = Outbound.objects.create(**outbound_message)
        failed.last_sent_time = failed.created_at
        failed.save()
        post_save.connect(
            psh_fire_msg_action_if_new,
            sender=Outbound,
            dispatch_uid="psh_fire_msg_action_if_new",
        )
        nack = {
            "message_type": "event",
            "event_id": "b04ec322fc1c4819bc3f28e6e0c69de6",
            "event_type": "nack",
            "nack_reason": "no answer",
            "user_message_id": failed.vumi_message_id,
            "helper_metadata": {},
            "timestamp": "2015-10-28 16:20:37.485612",
            "sent_message_id": "external-id",
        }

        with patch.object(ConcurrencyLimiter, "decr_message_count") as mock_method:
            response = self.client.post(
                "/api/v1/events", json.dumps(nack), content_type="application/json"
            )
            mock_method.assert_called_once_with(channel, failed.created_at)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        d = Outbound.objects.get(pk=failed.id)
        self.assertEqual(d.delivered, False)
        self.assertEqual(d.attempts, 3)  # not moved on as last attempt passed
        self.assertEqual(d.metadata["nack_reason"], "no answer")
        self.assertEqual(
            False,
            self.check_logs(
                "Message: 'Simple outbound message' sent to '+27820000123'"
                "[session_event: new]"
            ),
        )

    @responses.activate
    @patch("django.core.cache.cache.get_or_set")
    @patch("django.core.cache.cache.decr")
    @patch("message_sender.views.fire_delivery_hook")
    @patch("message_sender.tasks.send_message.delay")
    def test_event_nack_concurrency_decr_junebug(
        self, mock_send_message, mock_hook, mock_get_or_set, mock_decr
    ):
        """
        A rejected event should retry and update the message object accordingly
        as well as decrement the relative concurrency limiter
        """
        self.add_metrics_response()
        # Fake cache calls
        mock_get_or_set.side_effect = self.fake_cache.get_or_set
        mock_decr.side_effect = self.fake_cache.decr

        channel = Channel.objects.get(channel_id="VUMI_VOICE")
        d = self.make_outbound(to_addr="+27820000123", channel=channel.channel_id)
        d.last_sent_time = d.created_at
        d.save()

        post_save.connect(
            psh_fire_msg_action_if_new,
            sender=Outbound,
            dispatch_uid="psh_fire_msg_action_if_new",
        )
        nack = {
            "event_type": "rejected",
            "message_id": d.vumi_message_id,
            "channel-id": "channel-uuid-1234",
            "timestamp": "2015-10-28 16:19:37.485612",
            "event_details": {"reason": "No answer"},
        }
        with patch.object(ConcurrencyLimiter, "decr_message_count") as mock_method:
            response = self.client.post(
                "/api/v1/events/junebug",
                json.dumps(nack),
                content_type="application/json",
            )
            mock_method.assert_called_once_with(channel, d.created_at)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        d.refresh_from_db()
        self.assertEqual(d.delivered, False)
        self.assertEqual(d.attempts, 0)
        self.assertEqual(d.metadata["nack_reason"], {"reason": "No answer"})
        mock_hook.assert_called_once_with(d)

    @responses.activate
    @patch("django.core.cache.cache.get_or_set")
    @patch("django.core.cache.cache.decr")
    @patch("message_sender.views.fire_delivery_hook")
    @patch("message_sender.tasks.send_message.delay")
    def test_event_delivery_failed_concurrency_decr_june(
        self, mock_send_message, mock_hook, mock_get_or_set, mock_decr
    ):
        """
        A failed delivery should retry and update the message accordingly, as
        well as decrement the concurrency limiter.
        """
        self.add_metrics_response()
        # Fake cache calls
        mock_get_or_set.side_effect = self.fake_cache.get_or_set
        mock_decr.side_effect = self.fake_cache.decr

        channel = Channel.objects.get(channel_id="VUMI_VOICE")
        d = self.make_outbound(to_addr="+27820000123", channel=channel.channel_id)
        d.last_sent_time = d.created_at
        d.save()
        dr = {
            "event_type": "delivery_failed",
            "message_id": d.vumi_message_id,
            "channel-id": "channel-uuid-1234",
            "timestamp": "2015-10-28 16:19:37.485612",
            "event_details": {},
        }
        with patch.object(ConcurrencyLimiter, "decr_message_count") as mock_method:
            response = self.client.post(
                "/api/v1/events/junebug",
                json.dumps(dr),
                content_type="application/json",
            )
            mock_method.assert_called_once_with(channel, d.created_at)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        d.refresh_from_db()
        self.assertEqual(d.delivered, False)
        self.assertEqual(d.attempts, 0)
        self.assertEqual(d.metadata["delivery_failed_reason"], {})
        mock_hook.assert_called_once_with(d)


class TestRequeueFailedTasks(AuthenticatedAPITestCase):
    def make_outbound(self, to_addr, channel=None):

        if channel:
            channel = Channel.objects.get(channel_id=channel)

        self.add_identity_search_response(to_addr, "34857985789")

        self._replace_post_save_hooks_outbound()  # don't let fixtures fire
        outbound_message = {
            "to_addr": to_addr,
            "vumi_message_id": "075a32da-e1e4-4424-be46-1d09b71056fd",
            "content": "Simple outbound message",
            "delivered": False,
            "metadata": {"voice_speech_url": "http://test.com"},
            "channel": channel,
        }
        outbound = Outbound.objects.create(**outbound_message)
        self._restore_post_save_hooks_outbound()  # let tests fire tasks
        return outbound

    @responses.activate
    def test_requeue(self):
        """
        When running the `requeue_failed_tasks` task, all the failed tasks
        should be rerun, and all the failure objects for those tasks should
        be removed from the database.
        """
        self.add_metrics_response()
        outbound1 = self.make_outbound(to_addr="+27820000123")
        outbound2 = self.make_outbound(to_addr="+27987")
        OutboundSendFailure.objects.create(
            outbound=outbound1,
            task_id=uuid.uuid4(),
            initiated_at=timezone.now(),
            reason="Error",
        )

        requeue_failed_tasks()

        outbound1.refresh_from_db()
        self.assertIsNotNone(outbound1.last_sent_time)
        outbound2.refresh_from_db()
        self.assertIsNone(outbound2.last_sent_time)
        self.assertEqual(OutboundSendFailure.objects.all().count(), 0)


class TestFailedMsisdnLookUp(TestCase):
    def add_identity_no_address_search_response(self, msisdn, identity, count=0):
        response = {"next": None, "previous": None, "results": []}
        responses.add(
            responses.GET,
            "%s/identities/%s/addresses/msisdn"
            % (settings.IDENTITY_STORE_URL, identity),  # noqa
            json=response,
            status=200,
        )

    @responses.activate
    def test_fire_failed_msisdn_lookup(self):
        """
        trigger a webhook if there is no to_addr in the identity
        """
        send_message = SendMessage()

        new_channel = {
            "channel_id": "NEW_DEFAULT",
            "channel_type": Channel.JUNEBUG_TYPE,
            "default": True,
            "configuration": {
                "JUNEBUG_API_URL": "http://example.com/",
                "JUNEBUG_API_AUTH": ("username", "password"),
                "JUNEBUG_API_FROM": "+4321",
            },
            "concurrency_limit": 0,
            "message_timeout": 0,
            "message_delay": 0,
        }

        Channel.objects.create(**new_channel)
        self.assertEqual(Channel.objects.filter(default=True).count(), 1)
        channel = Channel.objects.get(channel_id="NEW_DEFAULT")

        self.add_identity_no_address_search_response("", "0c03d360")

        outbound = {
            "id": "075a32da-e1e4-4424-be46-1d09b71056fd",
            "to_identity": "0c03d360",
            "to_addr": "",
            "content": "Simple outbound message",
            "delivered": False,
            "metadata": {"voice_speech_url": "https://foo.com/file.mp3"},
            "channel": channel,
        }

        outbound = Outbound.objects.create(**outbound)

        user = User.objects.create_user("test")
        hook = Hook.objects.create(
            event="identity.no_address", target="http://webhook", user=user
        )

        responses.add(method=responses.POST, url="http://webhook", json={}, status=200)

        send_message.run("075a32da-e1e4-4424-be46-1d09b71056fd")

        webhook = responses.calls[-1].request
        self.assertEqual(
            json.loads(webhook.body),
            {"hook": hook.dict(), "data": {"to_identity": "0c03d360"}},
        )


class TestFailedTaskAPI(AuthenticatedAPITestCase):
    def make_outbound(self, to_addr, channel=None):

        if channel:
            channel = Channel.objects.get(channel_id=channel)

        self.add_identity_search_response(to_addr, "34857985789")

        self._replace_post_save_hooks_outbound()  # don't let fixtures fire
        outbound_message = {
            "to_addr": to_addr,
            "vumi_message_id": "075a32da-e1e4-4424-be46-1d09b71056fd",
            "content": "Simple outbound message",
            "delivered": False,
            "metadata": {"voice_speech_url": "http://test.com"},
            "channel": channel,
        }
        outbound = Outbound.objects.create(**outbound_message)
        self._restore_post_save_hooks_outbound()  # let tests fire tasks
        return outbound

    @responses.activate
    def test_failed_tasks_list(self):
        """
        When making a GET requests to the failed tasks endpoint, a paginated
        list of all of the failed tasks should be returned.
        """
        self.add_metrics_response()
        outbound1 = self.make_outbound(to_addr="+27820000123")
        failures = []
        for i in range(3):
            failures.append(
                OutboundSendFailure.objects.create(
                    outbound=outbound1,
                    task_id=uuid.uuid4(),
                    initiated_at=timezone.now(),
                    reason="Error",
                )
            )

        response = self.client.get(
            "/api/v1/failed-tasks/", content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        results = response.data["results"]
        self.assertEqual(len(results), 2)
        self.assertEqual(results[0]["id"], failures[2].id)
        self.assertEqual(results[1]["id"], failures[1].id)
        self.assertIsNotNone(response.data["next"])

        response = self.client.get(
            response.data["next"], content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        results = response.data["results"]
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["id"], failures[0].id)

    @responses.activate
    def test_failed_tasks_requeue(self):
        """
        When making a POST requests to the failed tasks endpoint, all of the
        failed tasks should be rerun, and all of the failure objects should
        be removed from the database.
        """
        self.add_metrics_response()
        outbound1 = self.make_outbound(to_addr="+27820000123")
        OutboundSendFailure.objects.create(
            outbound=outbound1,
            task_id=uuid.uuid4(),
            initiated_at=timezone.now(),
            reason="Error",
        )

        response = self.client.post(
            "/api/v1/failed-tasks/", content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["requeued_failed_tasks"], True)
        self.assertEqual(OutboundSendFailure.objects.all().count(), 0)


class TestOutboundAdmin(AuthenticatedAPITestCase):
    def setUp(self):
        super(TestOutboundAdmin, self).setUp()
        self.adminclient.login(username="testsu", password="dummypwd")

    @patch("message_sender.tasks.send_message.apply_async")
    def test_resend_outbound_only_selected(self, mock_send_message):
        outbound_id = self.make_outbound()
        self.make_outbound()
        data = {"action": "resend_outbound", "_selected_action": [outbound_id]}

        response = self.adminclient.post(
            reverse("admin:message_sender_outbound_changelist"), data, follow=True
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, "Attempting to resend 1 message.")

        mock_send_message.assert_called_once_with(kwargs={"message_id": outbound_id})

    @patch("message_sender.tasks.send_message.apply_async")
    def test_resend_outbound_multiple(self, mock_send_message):
        outbound_id_1 = self.make_outbound()
        outbound_id_2 = self.make_outbound()
        data = {
            "action": "resend_outbound",
            "_selected_action": [outbound_id_1, outbound_id_2],
        }

        response = self.adminclient.post(
            reverse("admin:message_sender_outbound_changelist"), data, follow=True
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, "Attempting to resend 2 messages.")

        mock_send_message.assert_any_call(kwargs={"message_id": outbound_id_1})
        mock_send_message.assert_any_call(kwargs={"message_id": outbound_id_2})


class TestChannels(AuthenticatedAPITestCase):
    def test_channel_default_post_save(self):

        new_channel = {
            "channel_id": "NEW_DEFAULT",
            "channel_type": Channel.JUNEBUG_TYPE,
            "default": True,
            "configuration": {
                "JUNEBUG_API_URL": "http://example.com/",
                "JUNEBUG_API_AUTH": ("username", "password"),
                "JUNEBUG_API_FROM": "+4321",
            },
            "concurrency_limit": 0,
            "message_timeout": 0,
            "message_delay": 0,
        }

        Channel.objects.create(**new_channel)

        self.assertEqual(Channel.objects.filter(default=True).count(), 1)

        channel = Channel.objects.get(channel_id="JUNE_VOICE")
        channel.default = True
        channel.save()

        self.assertEqual(Channel.objects.filter(default=True).count(), 1)


class TestUpdateIdentityCommand(AuthenticatedAPITestCase):
    def make_identity_lookup(self, msisdn="+27820000123", identity="56f6e9506ee3"):
        identity = {"msisdn": msisdn, "identity": identity}
        return IdentityLookup.objects.create(**identity)

    def prepare_data(self):
        self.out1 = self.make_outbound()
        self.out2 = self.make_outbound(to_addr="+274321", to_identity="")
        self.in1 = self.make_inbound("1234", from_addr="+27820000123")
        self.in2 = self.make_inbound("1234", from_addr="+274321")
        self.make_identity_lookup()

    def check_data(self):
        # Outbound with valid msisdn
        out1 = Outbound.objects.get(id=self.out1)
        self.assertEqual(str(out1.to_addr), "")
        self.assertEqual(str(out1.to_identity), "56f6e9506ee3")

        # Outbound msisdn not found
        out2 = Outbound.objects.get(id=self.out2)
        self.assertEqual(str(out2.to_addr), "+274321")
        self.assertEqual(str(out2.to_identity), "")

        # Inbound with valid msisdn
        in1 = Inbound.objects.get(id=self.in1)
        self.assertEqual(str(in1.from_addr), "")
        self.assertEqual(str(in1.from_identity), "56f6e9506ee3")

        # Inbound msisdn not found
        in2 = Inbound.objects.get(id=self.in2)
        self.assertEqual(str(in2.from_addr), "+274321")
        self.assertEqual(str(in2.from_identity), "")

    def test_update_identity_no_argument(self):
        self.prepare_data()
        call_command("update_identity_field")
        self.check_data()

    def test_update_identity_by_id(self):
        self.prepare_data()
        call_command("update_identity_field", "--loop", "ID")
        self.check_data()

    def test_update_identity_by_msg(self):
        self.prepare_data()
        call_command("update_identity_field", "--loop", "MSG")
        self.check_data()

    def test_update_identity_by_sql(self):
        self.prepare_data()
        call_command("update_identity_field", "--loop", "SQL")
        self.check_data()


class TestAggregateOutbounds(AuthenticatedAPITestCase):
    def test_aggregate_outbounds(self):
        """
        The aggregate outbounds task should create new AggregateOutbounds
        objects that represent the current Outbounds
        """
        c1 = Channel.objects.create(channel_id="c1", configuration={})
        c2 = Channel.objects.create(channel_id="c2", configuration={})

        o = self.make_outbound(channel=c1)
        o = Outbound.objects.get(id=o)
        o.created_at = datetime(2017, 1, 1, tzinfo=timezone.utc)
        o.attempts = 2
        o.save()

        o = self.make_outbound(channel=c1)
        o = Outbound.objects.get(id=o)
        o.created_at = datetime(2017, 1, 1, tzinfo=timezone.utc)
        o.save()

        o = self.make_outbound(channel=c2)
        o = Outbound.objects.get(id=o)
        o.created_at = datetime(2017, 1, 1, tzinfo=timezone.utc)
        o.save()

        o = self.make_outbound(channel=c2)
        o = Outbound.objects.get(id=o)
        o.created_at = datetime(2017, 1, 1, tzinfo=timezone.utc)
        o.delivered = True
        o.save()

        o = self.make_outbound(channel=c2)
        o = Outbound.objects.get(id=o)
        o.created_at = datetime(2017, 1, 3, tzinfo=timezone.utc)
        o.save()

        self.assertNumQueries(4, tasks.aggregate_outbounds("2017-01-01", "2017-01-02"))

        agg1 = AggregateOutbounds.objects.get(
            date=date(2017, 1, 1), channel=c1, delivered=False
        )
        self.assertEqual(agg1.total, 2)
        self.assertEqual(agg1.attempts, 3)

        agg2 = AggregateOutbounds.objects.get(
            date=date(2017, 1, 1), channel=c2, delivered=True
        )
        self.assertEqual(agg2.total, 1)
        self.assertEqual(agg2.attempts, 1)

        agg3 = AggregateOutbounds.objects.get(
            date=date(2017, 1, 1), channel=c2, delivered=False
        )
        self.assertEqual(agg3.total, 1)
        self.assertEqual(agg3.attempts, 1)

        self.assertEqual(AggregateOutbounds.objects.count(), 3)

    def test_aggregate_outbounds_replace(self):
        """
        If the task is run a second time, it should replace all aggregates
        with new aggregates.
        """
        c = Channel.objects.create(channel_id="c1", configuration={})

        for i in range(10):
            o = self.make_outbound(channel=c)
            o = Outbound.objects.get(id=o)
            o.created_at = datetime(2017, 1, 1, tzinfo=timezone.utc)
            o.save()

        self.assertNumQueries(2, tasks.aggregate_outbounds("2017-01-01", "2017-01-02"))

        agg = AggregateOutbounds.objects.get(
            date=date(2017, 1, 1), channel=c, delivered=False
        )
        self.assertEqual(agg.total, 10)

        Outbound.objects.all().update(delivered=True)

        self.assertNumQueries(2, tasks.aggregate_outbounds("2017-01-01", "2017-01-02"))

        agg = AggregateOutbounds.objects.get(
            date=date(2017, 1, 1), channel=c, delivered=True
        )
        self.assertEqual(agg.total, 10)
        self.assertEqual(AggregateOutbounds.objects.count(), 1)

    @mock.patch("message_sender.views.aggregate_outbounds")
    def test_view_defaults(self, task):
        """
        Should default to today's date for end, and
        AGGREGATE_OUTBOUND_BACKTRACK days in the past for start
        """
        response = self.client.post(
            "/api/v1/aggregate-outbounds/", content_type="application/json"
        )
        self.assertEqual(response.status_code, 202)
        end = datetime.now().date().isoformat()
        start = (datetime.now() - timedelta(30)).date().isoformat()
        task.delay.assert_called_once_with(start, end)

    @mock.patch("message_sender.views.aggregate_outbounds")
    def test_view(self, task):
        """
        Should fire the task with the provided parameters
        """
        response = self.client.post(
            "/api/v1/aggregate-outbounds/",
            content_type="application/json",
            data=json.dumps({"start": "2017-01-01", "end": "2017-01-03"}),
        )
        self.assertEqual(response.status_code, 202)
        task.delay.assert_called_once_with("2017-01-01", "2017-01-03")


class ArchivedOutboundsTests(AuthenticatedAPITestCase):
    def test_task_filename(self):
        """
        The filename function should return the appropriate filename
        """
        filename = tasks.archive_outbound.filename(datetime(2017, 8, 9).date())
        self.assertEqual(filename, "outbounds-2017-08-09.gz")

    def test_dump_data(self):
        """
        Serializes outbound messages into a gzipped file
        """
        o = self.make_outbound()
        o = Outbound.objects.get(id=o)

        tasks.archive_outbound.dump_data("test.gz", Outbound.objects.all())

        with gzip.open("test.gz") as f:
            [outbound] = map(lambda l: json.loads(l.decode("utf-8")), f)

        outbound.pop("created_at")
        outbound.pop("updated_at")
        self.assertEqual(
            outbound,
            {
                "attempts": o.attempts,
                "call_answered": o.call_answered,
                "channel": o.channel_id,
                "content": o.content,
                "created_by": o.created_by_id,
                "delivered": o.delivered,
                "id": str(o.id),
                "last_sent_time": o.last_sent_time,
                "metadata": o.metadata,
                "resend": o.resend,
                "to_addr": o.to_addr,
                "to_identity": o.to_identity,
                "updated_by": o.updated_by_id,
                "version": o.version,
                "vumi_message_id": o.vumi_message_id,
            },
        )
        os.remove("test.gz")

    def test_create_archived_outbound(self):
        """
        Creates the model with the attached file
        """
        with open("test", "w") as f:
            f.write("test")

        tasks.archive_outbound.create_archived_outbound(
            datetime(2017, 8, 9).date(), "test"
        )

        os.remove("test")

        [archive] = ArchivedOutbounds.objects.all()

        self.assertEqual(archive.date, datetime(2017, 8, 9).date())
        self.assertEqual(archive.archive.read().decode("utf-8"), "test")

    def test_task_skips_already_archived(self):
        """
        If there is already an ArchivedOutbounds for the given date, then the
        task should skip processing that date
        """
        with open("test", "w") as f:
            f.write("test")
        tasks.archive_outbound.create_archived_outbound(
            datetime(2017, 8, 9).date(), "test"
        )
        os.remove("test")

        o = self.make_outbound()
        o = Outbound.objects.get(id=o)
        o.created_at = datetime(2017, 8, 9, tzinfo=timezone.utc)
        o.save()

        tasks.archive_outbound("2017-08-09", "2017-08-09")

        [archive] = ArchivedOutbounds.objects.all()
        self.assertEqual(archive.date, datetime(2017, 8, 9).date())
        self.assertEqual(archive.archive.read().decode("utf-8"), "test")
        self.assertEqual(Outbound.objects.count(), 1)

    def test_task_skips_empty_dates(self):
        """
        If there are no outbounds for the date, then no archive should be
        created
        """
        tasks.archive_outbound("2017-08-09", "2017-08-09")
        self.assertEqual(ArchivedOutbounds.objects.count(), 0)

    def test_task_only_archives_outbounds_for_date(self):
        """
        Only outbounds in the specified date range should be archived
        """
        o = self.make_outbound()
        o = Outbound.objects.get(id=o)
        o.created_at = datetime(2017, 8, 9, tzinfo=timezone.utc)
        o.save()

        o = self.make_outbound()
        o = Outbound.objects.get(id=o)
        o.created_at = datetime(2017, 8, 10, tzinfo=timezone.utc)
        o.save()

        self.assertEqual(Outbound.objects.count(), 2)
        tasks.archive_outbound("2017-08-09", "2017-08-09")
        self.assertEqual(Outbound.objects.count(), 1)

    def test_task_creates_archive(self):
        """
        The task should serialize the appropriate messages into a gzipped file
        """
        o = self.make_outbound()
        o = Outbound.objects.get(id=o)
        o.created_at = datetime(2017, 8, 9, tzinfo=timezone.utc)
        o.save()
        o.refresh_from_db()

        tasks.archive_outbound("2017-08-09", "2017-08-09")

        self.assertEqual(Outbound.objects.count(), 0)
        [archive] = ArchivedOutbounds.objects.all()
        self.assertEqual(archive.date, datetime(2017, 8, 9).date())
        [outbound] = map(
            lambda l: json.loads(l.decode("utf-8")),
            gzip.GzipFile(fileobj=archive.archive),
        )
        self.assertEqual(outbound, OutboundArchiveSerializer(o).data)

    @mock.patch("message_sender.views.archive_outbound")
    def test_view(self, task):
        """
        The view should call the task
        """
        response = self.client.post(
            "/api/v1/archive-outbounds/",
            content_type="application/json",
            data=json.dumps({"start": "2017-01-01", "end": "2017-01-03"}),
        )
        self.assertEqual(response.status_code, 202)
        task.delay.assert_called_once_with("2017-01-01", "2017-01-03")


class TestWhatsAppEventAPI(AuthenticatedAPITestCase):
    def setUp(self):
        self.channel = Channel.objects.create(
            channel_id="test", configuration={"HMAC_SECRET": "testhmac"}
        )
        super().setUp()

    def generate_signature(self, content):
        h = hmac.new(
            self.channel.configuration["HMAC_SECRET"].encode(), content.encode(), sha256
        )
        return base64.b64encode(h.digest()).decode()

    def test_event_missing_fields(self):
        """
        If there are missing fields in the request, and error response should
        be returned, detailing the errors if this was an event and if this was an inbound
        """
        data = {"statuses": [{}], "messages": [{}]}
        response = self.client.post(
            reverse("whatsapp-events", args=[self.channel.channel_id]),
            json.dumps(data),
            content_type="application/json",
            HTTP_X_ENGAGE_HOOK_SIGNATURE=self.generate_signature(json.dumps(data)),
        )
        self.assertEqual(
            json.loads(response.content.decode()),
            {
                "accepted": False,
                "statuses": [
                    {
                        "accepted": False,
                        "id": None,
                        "reason": {
                            "id": ["This field is required."],
                            "status": ["This field is required."],
                            "timestamp": ["This field is required."],
                        },
                    }
                ],
                "messages": [
                    {
                        "accepted": False,
                        "id": None,
                        "reason": {
                            "id": ["This field is required."],
                            "text": ["This field is required."],
                        },
                    }
                ],
            },
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_event_no_message(self):
        """
        If we cannot find the message for the event, an error response should
        be returned.
        """
        event = {
            "statuses": [
                {
                    "id": "bad-message-id",
                    "status": "sent",
                    "timestamp": "2018-05-04T16:00:18Z",
                }
            ]
        }
        response = self.client.post(
            reverse("whatsapp-events", args=[self.channel.channel_id]),
            json.dumps(event),
            content_type="application/json",
            HTTP_X_ENGAGE_HOOK_SIGNATURE=self.generate_signature(json.dumps(event)),
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            json.loads(response.content.decode()),
            {
                "accepted": False,
                "messages": [],
                "statuses": [
                    {
                        "accepted": False,
                        "reason": "Cannot find message for ID bad-message-id",
                        "id": "bad-message-id",
                    }
                ],
            },
        )

    @patch("message_sender.views.fire_delivery_hook")
    def test_event_ack(self, mock_hook):
        """A submitted event should update the message object accordingly."""
        existing = self.make_outbound()

        d = Outbound.objects.get(pk=existing)
        event = {
            "statuses": [
                {
                    "id": d.vumi_message_id,
                    "status": "sent",
                    "timestamp": "2018-05-04T16:00:18Z",
                }
            ]
        }
        response = self.client.post(
            reverse("whatsapp-events", args=[self.channel.channel_id]),
            json.dumps(event),
            content_type="application/json",
            HTTP_X_ENGAGE_HOOK_SIGNATURE=self.generate_signature(json.dumps(event)),
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        d = Outbound.objects.get(pk=existing)
        self.assertEqual(d.delivered, True)
        self.assertEqual(d.attempts, 1)
        self.assertEqual(d.metadata["ack_timestamp"], "2018-05-04T16:00:18Z")
        self.assertEqual(
            False,
            self.check_logs(
                "Message: 'Simple outbound message' sent to '+27820000123'"
            ),
        )
        mock_hook.assert_called_once_with(d)

    @responses.activate
    @patch("message_sender.views.fire_delivery_hook")
    def test_event_nack(self, mock_hook):
        """
        A rejected event should retry and update the message object accordingly
        """
        self.add_metrics_response()
        existing = self.make_outbound()
        d = Outbound.objects.get(pk=existing)
        post_save.connect(
            psh_fire_msg_action_if_new,
            sender=Outbound,
            dispatch_uid="psh_fire_msg_action_if_new",
        )
        event = {
            "statuses": [
                {
                    "id": d.vumi_message_id,
                    "status": "failed",
                    "timestamp": "2018-05-04T16:00:18Z",
                }
            ]
        }

        response = self.client.post(
            reverse("whatsapp-events", args=[self.channel.channel_id]),
            json.dumps(event),
            content_type="application/json",
            HTTP_X_ENGAGE_HOOK_SIGNATURE=self.generate_signature(json.dumps(event)),
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        c = Outbound.objects.get(pk=existing)
        self.assertEqual(c.delivered, False)
        self.assertEqual(c.attempts, 2)
        self.assertEqual(
            True,
            self.check_logs(
                "Message: 'Simple outbound message' sent to '+27820000123' "
                "[session_event: new]"
            ),
        )
        mock_hook.assert_called_once_with(d)

    @patch("message_sender.views.fire_delivery_hook")
    def test_event_delivery_succeeded(self, mock_hook):
        """A successful delivery should update the message accordingly."""
        existing = self.make_outbound()
        d = Outbound.objects.get(pk=existing)
        event = {
            "statuses": [
                {
                    "id": d.vumi_message_id,
                    "status": "delivered",
                    "timestamp": "2018-05-04T16:00:18Z",
                }
            ]
        }
        response = self.client.post(
            reverse("whatsapp-events", args=[self.channel.channel_id]),
            json.dumps(event),
            content_type="application/json",
            HTTP_X_ENGAGE_HOOK_SIGNATURE=self.generate_signature(json.dumps(event)),
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        d = Outbound.objects.get(pk=existing)
        self.assertEqual(d.delivered, True)
        self.assertEqual(d.attempts, 1)
        self.assertEqual(d.metadata["delivery_timestamp"], "2018-05-04T16:00:18Z")
        self.assertEqual(
            False,
            self.check_logs(
                "Message: 'Simple outbound message' sent to '+27820000123'"
            ),
        )
        mock_hook.assert_called_once_with(d)

    def test_missing_channel(self):
        """
        If there's no channel with the specified ID, a 404 response should be returned
        """
        response = self.client.post(
            reverse("whatsapp-events", args=["badchannel"]),
            json.dumps({}),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_missing_hmac_header(self):
        """
        If the signature header is missing, the request should not be allowed
        """
        response = self.client.post(
            reverse("whatsapp-events", args=[self.channel.channel_id]),
            json.dumps({}),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(
            json.loads(response.content),
            {"detail": "X-Engage-Hook-Signature header required"},
        )

    def test_invalid_hmac_header(self):
        """
        If the signature header is invalid, the request should not be allowed
        """
        response = self.client.post(
            reverse("whatsapp-events", args=[self.channel.channel_id]),
            json.dumps({}),
            content_type="application/json",
            HTTP_X_ENGAGE_HOOK_SIGNATURE="bad-signature",
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(
            json.loads(response.content), {"detail": "Invalid hook signature"}
        )

    @responses.activate
    def test_create_inbound(self):
        """
        If an inbound message is sent to the event endpoint, then it should be treated
        as an inbound message.
        """
        responses.add(
            responses.POST, "http://metrics-url/metrics/", json={}, status=201
        )
        identity_uuid = str(uuid.uuid4())
        responses.add(
            responses.GET,
            "{}/identities/search/?details__addresses__msisdn=%2B27820000000".format(
                settings.IDENTITY_STORE_URL
            ),
            json={"results": [{"id": identity_uuid}]},
            status=200,
            match_querystring=True,
        )

        message_id = str(uuid.uuid4())
        post_inbound = {
            "messages": [
                {
                    "id": message_id,
                    "from": "27820000000",
                    "text": {"body": "Test message"},
                }
            ]
        }
        response = self.client.post(
            reverse("whatsapp-events", args=[self.channel.channel_id]),
            json.dumps(post_inbound),
            content_type="application/json",
            HTTP_X_ENGAGE_HOOK_SIGNATURE=self.generate_signature(
                json.dumps(post_inbound)
            ),
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        d = Inbound.objects.last()
        self.assertIsNotNone(d.id)
        self.assertEqual(d.message_id, message_id)
        self.assertEqual(d.from_identity, identity_uuid)
        self.assertEqual(d.content, "Test message")


class TestWhatsAppAPISender(TestCase):
    def test_send_text_to_send_text_message(self):
        """
        send_text should delegate to send_text_message when there is no HSM
        setup.
        """
        sender = WhatsAppApiSender("http://whatsapp", "test-token", None, None, None)
        sender.send_text_message = MagicMock(
            return_value={"messages": [{"id": "message-id"}]}
        )

        sender.send_text("+27820001001", "Test message")

        sender.send_text_message.assert_called_once_with("27820001001", "Test message")

    def test_send_text_to_send_hsm(self):
        """
        send_text should delegate to send_hsm when there are HSM config values.
        """
        sender = WhatsAppApiSender(
            "http://whatsapp", "test-token", "hsm-namespace", "hsm-element-name", "ttl"
        )
        sender.send_hsm = MagicMock(return_value={"messages": [{"id": "message-id"}]})

        sender.send_text("+27820001001", "Test message")

        sender.send_hsm.assert_called_once_with("27820001001", "Test message")

    def test_send_text_to_send_custom_hsm(self):
        """
        send_text should delegate to send_custom_hsm when there is a 'template'
        key inside the message metadata.
        """
        sender = WhatsAppApiSender(
            "http://whatsapp", "test-token", "hsm-namespace", "hsm-element-name", "ttl"
        )
        sender.send_custom_hsm = MagicMock(
            return_value={"messages": [{"id": "message-id"}]}
        )

        sender.send_text(
            "+27820001001",
            "Test message",
            metadata={
                "template": {
                    "name": "sbm",
                    "language": "afr_ZA",
                    "variables": ["variable1", "variable2"],
                }
            },
        )

        sender.send_custom_hsm.assert_called_once_with(
            "27820001001", "sbm", "afr_ZA", ["variable1", "variable2"]
        )

    def test_send_text_unknown_contact(self):
        """
        If the sending fails with a unknown contact error, contact_check should
        be called then the send should be retried.
        """
        sender = WhatsAppApiSender("http://whatsapp", "test-token", None, None, None)
        sender.get_contact = MagicMock(return_value="27820001001")
        sender.send_text_message = MagicMock(
            return_value={
                "errors": [
                    {
                        "code": 1006,
                        "details": "unknown contact",
                        "title": "Resource not found",
                    }
                ],
                "messages": [{"id": "message-id"}],
            }
        )

        sender.send_text("+27820001001", "Test message")
        sender.get_contact.assert_called_with("+27820001001")

        sender.send_text_message.assert_has_calls(
            [call("27820001001", "Test message"), call("27820001001", "Test message")]
        )

    def test_send_image(self):
        """
        send_image should raise an API sender exception as it is not supported
        """
        sender = WhatsAppApiSender("http://whatsapp", "test-token", None, None, None)
        self.assertRaises(
            WhatsAppApiSenderException,
            sender.send_image,
            "+27820001001",
            "Test message",
            "http://example.jpg",
        )

    def test_send_voice(self):
        """
        send_voice should raise an API sender exception as it is not supported
        """
        sender = WhatsAppApiSender("http://whatsapp", "test-token", None, None, None)
        self.assertRaises(
            WhatsAppApiSenderException,
            sender.send_voice,
            "+27820001001",
            "Test message",
            "http://example.mp3",
        )

    def test_fire_metric(self):
        """
        fire_metric should raise an API sender exception as it is not supported
        """
        sender = WhatsAppApiSender("http://whatsapp", "test-token", None, None, None)
        self.assertRaises(
            WhatsAppApiSenderException, sender.fire_metric, "test.metric", 7
        )

    @responses.activate
    def test_get_contact_exists(self):
        """
        get_contact should make the appropriate request to the WhatsApp API, and return
        the contact ID.
        """
        sender = WhatsAppApiSender("http://whatsapp", "test-token", None, None, None)

        responses.add(
            method=responses.POST,
            url="http://whatsapp/v1/contacts",
            json={
                "contacts": [
                    {"input": "+27820001001", "status": "valid", "wa_id": "27820001001"}
                ]
            },
            status=200,
        )

        self.assertEqual(sender.get_contact("+27820001001"), "27820001001")
        request = responses.calls[-1].request
        self.assertEqual(request.headers["Authorization"], "Bearer test-token")
        self.assertEqual(
            json.loads(request.body), {"blocking": "wait", "contacts": ["+27820001001"]}
        )

    @responses.activate
    def test_get_contact_not_exists(self):
        """
        get_contact should make the appropriate request to the WhatsApp API, and trigger
        a webhook if the contact doesn't exist
        """
        sender = WhatsAppApiSender("http://whatsapp", "test-token", None, None, None)

        responses.add(
            method=responses.POST,
            url="http://whatsapp/v1/contacts",
            json={"contacts": [{"input": "+27820001001", "status": "invalid"}]},
            status=200,
        )

        user = User.objects.create_user("testuser")
        hook = Hook.objects.create(
            event="whatsapp.failed_contact_check", target="http://webhook", user=user
        )

        responses.add(method=responses.POST, url="http://webhook", json={}, status=200)

        self.assertEqual(sender.get_contact("+27820001001"), None)

        request = responses.calls[-2].request
        self.assertEqual(request.headers["Authorization"], "Bearer test-token")
        self.assertEqual(
            json.loads(request.body), {"blocking": "wait", "contacts": ["+27820001001"]}
        )

        webhook = responses.calls[-1].request
        self.assertEqual(
            json.loads(webhook.body),
            {"hook": hook.dict(), "data": {"address": "+27820001001"}},
        )

    @responses.activate
    def test_send_hsm(self):
        """
        send_hsm should make the appropriate request to the WhatsApp API
        """
        sender = WhatsAppApiSender(
            "http://whatsapp", "test-token", "hsm-namespace", "hsm-element-name", 604800
        )

        responses.add(
            method=responses.POST,
            url="http://whatsapp/v1/messages",
            json={"messages": [{"id": "message-id"}]},
        )

        sender.send_hsm("27820001001", "Test message")
        request = responses.calls[-1].request
        self.assertEqual(request.headers["Authorization"], "Bearer test-token")
        self.assertEqual(
            json.loads(request.body),
            {
                "to": "27820001001",
                "ttl": 604800,
                "type": "hsm",
                "hsm": {
                    "namespace": "hsm-namespace",
                    "element_name": "hsm-element-name",
                    "localizable_params": [{"default": "Test message"}],
                },
            },
        )

    @responses.activate
    def test_send_custom_hsm(self):
        """
        send_custom_hsm should make the appropriate request to the WhatsApp API
        """
        sender = WhatsAppApiSender(
            "http://whatsapp", "test-token", "hsm-namespace", "hsm-element-name", 604800
        )

        responses.add(
            method=responses.POST,
            url="http://whatsapp/v1/messages",
            json={"messages": [{"id": "message-id"}]},
        )

        sender.send_custom_hsm(
            "27820001001", "sbm", "eng_ZA", ["variable1", "variable2"]
        )
        request = responses.calls[-1].request
        self.assertEqual(request.headers["Authorization"], "Bearer test-token")
        self.assertEqual(
            json.loads(request.body),
            {
                "to": "27820001001",
                "ttl": 604800,
                "type": "hsm",
                "hsm": {
                    "namespace": "hsm-namespace",
                    "element_name": "sbm",
                    "language": {"policy": "deterministic", "code": "eng_ZA"},
                    "localizable_params": [
                        {"default": "variable1"},
                        {"default": "variable2"},
                    ],
                },
            },
        )

    @responses.activate
    def test_send_hsm_unknown_contact(self):
        """
        send_hsm should return the appropriate body when there is a unknown
        contact error returned by the API.
        """
        sender = WhatsAppApiSender(
            "http://whatsapp", "test-token", "hsm-namespace", "hsm-element-name", "ttl"
        )

        responses.add(
            method=responses.POST,
            url="http://whatsapp/v1/messages",
            json={
                "errors": [
                    {
                        "code": 1006,
                        "details": "unknown contact",
                        "title": "Resource not found",
                    }
                ],
                "meta": {"version": "2.19.4", "api_status": "stable"},
            },
            status=404,
        )

        response = sender.send_hsm("27820001001", "Test message")

        self.assertEqual(response["errors"][0]["code"], 1006)
        self.assertEqual(response["errors"][0]["details"], "unknown contact")

    @responses.activate
    def test_send_hsm_http_error(self):
        """
        send_hsm should re-raise the HTTPError if it is not handled
        """
        sender = WhatsAppApiSender(
            "http://whatsapp", "test-token", "hsm-namespace", "hsm-element-name", "ttl"
        )

        responses.add(
            method=responses.POST,
            url="http://whatsapp/v1/messages",
            json={
                "errors": [
                    {
                        "code": 88,
                        "details": "broken flux capacitor",
                        "title": "Resource broken",
                    }
                ],
                "meta": {"version": "2.19.4", "api_status": "stable"},
            },
            status=404,
        )

        self.assertRaises(
            requests_exceptions.HTTPError,
            sender.send_hsm,
            "27820001001",
            "Test message",
        )

    @responses.activate
    def test_send_text_message(self):
        """
        send_text_message should make the appropriate request to the WhatsApp API
        """
        sender = WhatsAppApiSender("http://whatsapp", "test-token", None, None, None)

        responses.add(
            method=responses.POST,
            url="http://whatsapp/v1/messages",
            json={"messages": [{"id": "message-id"}]},
        )

        sender.send_text_message("27820001001", "Test message")
        request = responses.calls[-1].request
        self.assertEqual(request.headers["Authorization"], "Bearer test-token")
        self.assertEqual(
            json.loads(request.body),
            {"to": "27820001001", "text": {"body": "Test message"}},
        )


class CachedTokenAuthenticationTests(TestCase):
    url = reverse("outbound-list")

    def test_auth_required(self):
        """
        Ensure that the view we're testing actually requires token auth
        """
        r = self.client.get(self.url)
        self.assertEqual(r.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_caching_working(self):
        """
        Ensure that the second time we make a request, there's no database hit
        """
        user = User.objects.create_user("test")
        token = Token.objects.create(user=user)

        with self.assertNumQueries(2):
            r = self.client.get(
                self.url, HTTP_AUTHORIZATION="Token {}".format(token.key)
            )
            self.assertEqual(r.status_code, status.HTTP_200_OK)

        with self.assertNumQueries(1):
            r = self.client.get(
                self.url, HTTP_AUTHORIZATION="Token {}".format(token.key)
            )
            self.assertEqual(r.status_code, status.HTTP_200_OK)
