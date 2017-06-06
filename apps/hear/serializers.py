from rest_framework import serializers
from .models import Hear


class HearSerializer(serializers.ModelSerializer):
    """ Serializer to map the Hear-model instance into json format. """
    class Meta:
        """ Meta class to map serializer's fields with the model fields. """
        model = Hear
        fields = ('id', 'artist', 'song', 'file',)
        read_only_fields = ('id', 'artist', 'song',)
