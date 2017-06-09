from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from rest_framework.views import APIView
from .models import Hear
from .serializers import HearSerializer
from subprocess import Popen, PIPE
import os, sys


lookup_path = "/usr/bin/python2.7 /home/noteacer/TMS/Music/echoprint-server/examples/lookup_API.py"

def get_music_id(file):
    proclist = [cmd, os.path.abspath(file),]
    p = Popen(proclist, stdout=PIPE)
    result = p.communicate()[0]
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
#        a = get_music_id(self.request.file)
        #fl = serializer.data
        self.request.artist = "artistname-23"
        self.request.song = "songname"
        serializer.save(artist=self.request.artist, song=self.request.song)
