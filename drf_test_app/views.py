from django.shortcuts import render
from rest_framework import generics
from rest_framework import permissions
from .models import Test
from .serializers import TestSerializer

# Create your views here.


class TestList(generics.ListCreateAPIView):
    """
    get:
    Return a list of all existing Test instances.
    post:
    Create a new Test instance.
    """
    queryset = Test.objects.all()
    serializer_class = TestSerializer


class TestDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    get:
    Return the specified Test instance.
    put:
    Update the specified Test instance.
    delete:
    Delete the specified Test instance.
    """
    queryset = Test.objects.all()
    lookup_url_kwarg = 'test_id'
    serializer_class = TestSerializer

    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
