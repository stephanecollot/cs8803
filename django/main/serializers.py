#from django.contrib.auth.models import User, Group
from rest_framework import serializers
from document import Document


class DocumentSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Document
    fields = ('id', 'fileName', 'content')