from django.contrib import admin
from rest_framework.documentation import include_docs_urls
from django.conf.urls import url
from django.urls import path
from .views import TestList
from .views import TestDetail


urlpatterns = [
    url(r'^tests/$', TestList.as_view(), name='test_list'),
    url(r'^tests/(?P<test_id>\d+)/$', TestDetail.as_view(), name='test_detail'),
    url(r'^docs/', include_docs_urls(
        title='Test API',
        description='Test API.',
        public=False
    )),
]
