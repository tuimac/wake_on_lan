from rest_framework import views, status
from rest_framework.response import Response

from .serializers import SearchSerializer
from . import ArpScan

class SearchAPIViews(views.APIView):
    def get(self, request, *args, **kwargs):

