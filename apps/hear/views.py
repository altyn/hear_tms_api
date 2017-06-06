from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from rest_framework.views import APIView
from .models import Hear
from .serializers import HearSerializer
from subprocess import Popen, PIPE


def pwd_test():
    proc = Popen("pwd", stdout=PIPE, stderr=PIPE, universal_newlines=True)
    result = "No comm"
    exit_code = proc.wait()
    if exit_code != 0:
        for line in proc.stderr:
            result = line
    else:
        for line in proc.stdout:
            result = line
    return result


class HearAPIView(viewsets.ModelViewSet):
    """This class defines the create behavior of our hear api """
    queryset = Hear.objects.all()[:1]
    serializer_class = HearSerializer
    parser_classes = (MultiPartParser, FormParser,)
    
    """ Get details of song """
    def post(self, request, format=None):
        serializer = HearSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def perform_create(self, serializer):
        a = pwd_test()
        self.request.artist = a
        serializer.save(artist=self.request.artist)
