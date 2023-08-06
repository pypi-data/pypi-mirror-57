from datetime import timedelta
from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site

try:
    from urlparse import urlunparse
except ImportError:
    from urllib.parse import urlunparse


def make_absolute_url(path):
    # NOTE: We're using the default site as set by
    #       settings.SITE_ID and the Sites framework
    site = get_current_site(None)
    return urlunparse(
        ("https" if settings.USE_SSL else "http", site.domain, path, "", "", "")
    )


def daterange(start_date, end_date):
    """
    Returns the dates between the start and end dates
    """
    for n in range(int((end_date - start_date).days) + 1):
        yield start_date + timedelta(n)
