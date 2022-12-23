from django.test import TestCase
from faker import Faker
from .models import *
from .serializers import AnnotationSerializer, AnnotationBodySerializer, AnnotationTargetSerializer, FragmentSelectorSerializer, SelectorSerializer

"""
{ 
  "@context": "http://www.w3.org/ns/anno.jsonld",
  "id": "#218d01ff-f077-4cc3-992d-1c81c426e51b",
  "type": "Annotation",
  "creator" : user-id, 
  "body": [{
    "id": "http://34.125.134.88/body1",
    "type": "TextualBody",
    "value": "Nice picture"
  }],
  "target": {
    "source": "http://34.125.134.88/artitems/14"
    "selector": {
      "type": "FragmentSelector",
      "conformsTo": "http://www.w3.org/TR/media-frags/",
      "value": "xywh=pixel:270,120,90,170"
    }
  }
"""
class TestAnnotations(TestCase):
    def setUp(self):
      self.faker = Faker()

    def test_image_annotation_target_serializer(self):
      typeImage = create_or_return_type("image")
      fragmentSelector = FragmentSelector.objects.create(value="xywh=pixel:270,120,90,170")
      selector = Selector.objects.create(fragmentSelector=fragmentSelector)
      target = Target.objects.create(source="http://34.125.134.88/artitems/14", type= typeImage, selector=selector)
      
      expected = {'id': 'http://34.125.134.88/image{}'.format(target.id), 
      'source': 'http://34.125.134.88/artitems/14', 
      'type': 'Image', 
      'selector': {'value': 'xywh=pixel:270,120,90,170', 
                  'type': 'FragmentSelector', 
                  'conformsTo': 'http://www.w3.org/TR/media-frags/'}}
      actual = AnnotationTargetSerializer(target).data
      self.assertEqual(expected, actual)

    def test_body_serializer(self):
      typeText = create_or_return_type("text")
      motivation = create_or_return_motivation("commenting")
      value = self.faker.paragraph(nb_sentences=3)

      body = Body.objects.create(type=typeText, value=value, purpose=motivation)

      actual = AnnotationBodySerializer(body).data
      actual.pop('created')

      expected = {'id': 'http://34.125.134.88/body{}'.format(body.id), 
      'value': value, 
      'type': 'Text', 
      'format': 'text/plain', 
      'purpose': 'Commenting'}
      self.assertEqual(expected, actual)

    def test_fragment_selector_serializer(self):
      fragmentSelector = FragmentSelector.objects.create(value="xywh=pixel:270,120,90,170")
      
      expected = {'value': 'xywh=pixel:270,120,90,170', 
      'type': 'FragmentSelector', 
      'conformsTo': 'http://www.w3.org/TR/media-frags/'}
      actual = FragmentSelectorSerializer(fragmentSelector).data
      self.assertEqual(expected, actual)

    def test_helpers(self):
      type1 = create_or_return_type("image")
      type2 = create_or_return_type("failure")
      motivation1 = create_or_return_motivation("commenting")
      motivation2 = create_or_return_motivation("failure")

      self.assertEqual(type2, -1)
      self.assertEqual(type1.type.value, "Image")
      self.assertEqual(motivation2, -1)
      self.assertEqual(motivation1.motivation.value, "Commenting")   
    
    def tearDown(self):
      pass

