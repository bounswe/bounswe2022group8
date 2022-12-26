from .models import *
from rest_framework import serializers

class AnnotationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Annotation
        fields = ['id', 'context', 'body', 'type', 'target', 'creator']
    
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['@context'] = rep['context']
        rep['type'] = str(rep['type'])          # convert Enum to string
        rep['target'] = AnnotationTargetSerializer(instance.target).data
        if(not rep['body']): rep.pop('body')
        else: rep['body'] = AnnotationBodySerializer(instance.body, many=True).data
        rep['id'] = "#" + rep['id']
        rep.pop('context')
        return rep

class AnnotationBodySerializer(serializers.ModelSerializer):
    class Meta:
        model = Body
        fields =  ['value', 'type', 'purpose', 'created', 'modified', 'creator']

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['type'] = str(rep['type'])          # convert Enum to string
        rep['creator'] = CreatorSerializer(instance.creator).data
        #rep['id'] = URL + "body{}".format(rep['id'])
        #rep['purpose'] = str(rep['purpose'])
        return rep

class AnnotationTargetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Target
        fields = ['id', 'source', 'format', 'language', 'type', 'selector']
    
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['type'] = str(rep['type'])          # convert Enum to string
        rep['selector'] = SelectorSerializer(instance.selector).data['selector']
        if(rep['selector'][0]['type'] == SelectorEnum.fragmentselector): rep['selector'] = rep['selector'][0]  # image annotation
        rep['id'] = URL + "{}{}".format(rep['type'].lower(), rep['id'])
        if(not rep['language']): rep.pop('language')
        if(not rep['format']): rep.pop('format')
        return rep

class FragmentSelectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = FragmentSelector
        fields = ['value', 'type', 'conformsTo']
    
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['type'] = str(rep['type'])          # convert Enum to string
        return rep

class TextQuoteSelectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = TextQuoteSelector
        fields = ['exact', 'type']
    
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['type'] = str(rep['type'])          # convert Enum to string
        return rep

class TextPositionSelectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = TextPositionSelector
        fields = ['start', 'end', 'type']
    
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['type'] = str(rep['type'])          # convert Enum to string
        return rep

class SelectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Selector
        fields = ['fragmentSelector', 'textQuoteSelector', 'textPositionSelector']
    
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['fragmentSelector'] = FragmentSelectorSerializer(instance.fragmentSelector).data
        rep['textQuoteSelector'] = TextQuoteSelectorSerializer(instance.textQuoteSelector).data
        rep['textPositionSelector'] = TextPositionSelectorSerializer(instance.textPositionSelector).data
        rep['selector'] = []
        if(instance.fragmentSelector): rep['selector'].append(rep['fragmentSelector'])
        if(instance.textQuoteSelector): rep['selector'].append(rep['textQuoteSelector'])
        if(instance.textPositionSelector): rep['selector'].append(rep['textPositionSelector'])
        rep.pop('fragmentSelector')
        rep.pop('textQuoteSelector')
        rep.pop('textPositionSelector')
        return rep


class CreatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Creator
        fields = ['id', 'name']    