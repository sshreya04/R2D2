from .models import data
from rest_framework import serializers


class DetailSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = data
        fields = ('name','review', 'cast' )


