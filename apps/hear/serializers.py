from rest_framework import serializers
from .models import Hear, Melody


class MelodySerializer(serializers.ModelSerializer):

    class Meta:
        model = Melody
        fields = ('artist', 'song')


class HearSerializer(serializers.ModelSerializer):
    """ Serializer to map the Hear-model instance into json format. """
    mpfile = serializers.FileField()
    song = MelodySerializer(many=False, read_only=True)

    class Meta:
        """ Meta class to map serializer's fields with the model fields. """
        model = Hear
        fields = ('song', 'mpfile',)
        read_only_fields = ('song',)
