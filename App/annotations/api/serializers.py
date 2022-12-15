from .models import *
from rest_framework import serializers

class AnnotationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Annotation
        fields = ['id', 'context', 'body', 'type', 'target', 'url', 'creator']
    
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['@context'] = rep['context']
        rep['id'] = rep['url'] + "anno" + str(rep['id'])
        rep['type'] = str(rep['type'])          # convert Enum to string
        rep.pop('context')
        rep.pop('url')
        return rep

class AnnotationBodySerializer(serializers.ModelSerializer):
    class Meta:
        model = Body
        fields =  ['body', 'value', 'type', 'format', 'created', 'purpose']

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['type'] = str(rep['type'])          # convert Enum to string
        rep['id'] = URL + "body{}".format(rep['body'])
        rep['purpose'] = str(rep['purpose'])
        rep.pop('body')
        return rep

class AnnotationTargetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        field = ['target', 'source', 'format', 'language', 'type', 'selector']
    
    def to_representation(self, instance):
        pass

class SelectorSerializer(serializers.ModelSerializer):
    pass

