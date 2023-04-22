from rest_framework import serializers
from newstv.models import Channel



# Create Serializers
class ChannelSerializer(serializers.HyperlinkedModelSerializer):
    channel_id= serializers.ReadOnlyField()
    class Meta:
        model=Channel
        fields="__all__"