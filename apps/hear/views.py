from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404

from .models import Hear, Melody
from .serializers import HearSerializer

from subprocess import Popen, PIPE, check_output
import os, sys


cmd_p27 = "/usr/bin/python2.7"
cmd_lookup = "/home/noteacer/TMS/Music/echoprint-server/examples/lookup_API.py"

def get_music_id(file):
    if not (file is None):
        res_string = check_output([cmd_p27, cmd_lookup, os.path.abspath(file),])
        result = str(res_string, encoding='utf-8')
        result = result.strip('\n')
        return result
    else:
        return "File error or corruped"

def get_id_melody_by_trid(trid):
    melody = Melody.objects.get(id=0)
    try:        
        melody = Melody.objects.get(track_id=trid)
        return melody
    except ObjectDoesNotExist as e:
        return melody
#        obj = "Doesn't exist"
#        return Response(obj, status=status.HTTP_404_NOT_FOUND)
    

class HearAPIView(viewsets.ModelViewSet):
    """This class defines the create behavior of our hear api """
    queryset = Hear.objects.all()[:1]
    serializer_class = HearSerializer
    parser_classes = (MultiPartParser, FormParser,)
    
    """ Get details of song """
    def post(self, request, format=None):
        mpfile = request.data.get('mpfile')
        if not mpfile:
            return Response("Нет файла, или неправильный формат", status=status.HTTP_400_BAD_REQUEST) 
        
        serializer = HearSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def perform_create(self, serializer):
        fl = self.request.data.get('mpfile')
        mpfile_path = fl.temporary_file_path()
        a = get_music_id(mpfile_path)
        m_id = get_id_melody_by_trid(a)
        self.request.song = m_id 
        self.request.detail = a
        serializer.save(song=self.request.song, detail=self.request.detail)
