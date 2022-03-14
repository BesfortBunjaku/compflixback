from rest_framework import response
from .serializers import *
from .models import *
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.parsers import JSONParser, FormParser, MultiPartParser
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer, HTMLFormRenderer




class ComponentViewSet(ModelViewSet):
    queryset = Component.objects.all()
    serializer_class = ComponentSerializer
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer, HTMLFormRenderer]
    parser_classes = [MultiPartParser]