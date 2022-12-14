from .models import *
from rest_framework import serializers

class AnnotationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Annotation
        fields = ['id', 'context', 'body', 'type', 'target', 'url']
    
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['@context'] = rep['context']
        rep['id'] = rep['url'] + "anno" + str(rep['id'])
        rep.pop('context')
        rep.pop('url')
        return rep

class BodySerializer(serializers.ModelSerializer):
    class Meta:
        model = Body
        field = []

class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        field = []

class TargetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        field = []
    
