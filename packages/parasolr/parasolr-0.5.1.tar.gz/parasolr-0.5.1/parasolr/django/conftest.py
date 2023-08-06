from django.conf import settings
from django.test import override_settings
import pytest

from parasolr.django import SolrClient


@pytest.fixture
def empty_solr():
    # pytest solr fixture; updates solr schema
    SolrClient().update.delete_by_query('*:*')
