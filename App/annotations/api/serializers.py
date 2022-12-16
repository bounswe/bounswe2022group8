from .models import *
from rest_framework import serializers

class AnnotationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Annotation
        fields = ['uuid', 'id', 'context', 'body', 'type', 'target', 'creator']
    
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['@context'] = rep['context']
        rep['type'] = str(rep['type'])          # convert Enum to string
        rep['target'] = AnnotationTargetSerializer(instance.target).data
        if(not rep['body']): rep.pop('body')
        else: rep['body'] = AnnotationBodySerializer(instance.body).data
        rep['id'] = rep['uuid'] + "@" + str(rep['id'])  # change the name
        rep.pop('uuid')
        rep.pop('context')
        return rep

class AnnotationBodySerializer(serializers.ModelSerializer):
    class Meta:
        model = Body
        fields =  ['id', 'value', 'type', 'format', 'created', 'purpose']

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['type'] = str(rep['type'])          # convert Enum to string
        rep['id'] = URL + "body{}".format(rep['id'])
        rep['purpose'] = str(rep['purpose'])
        return rep

class AnnotationTargetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Target
        fields = ['id', 'source', 'format', 'language', 'type', 'selector']
    
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['type'] = str(rep['type'])          # convert Enum to string
        rep['selector'] = AnnotationSelectorSerializer(instance.selector).data
        rep['id'] = URL + "{}{}".format(rep['type'].lower(), rep['id'])
        if(not rep['language']): rep.pop('language')
        if(not rep['format']): rep.pop('format')
        return rep

class AnnotationSelectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Selector
        fields = ['value', 'type', 'conformsTo']
    
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['type'] = str(rep['type'])          # convert Enum to string
        return rep

