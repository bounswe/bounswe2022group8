from django.test import TestCase
from faker import Faker
from .models import *
from .serializers import AnnotationSerializer, AnnotationBodySerializer, AnnotationTargetSerializer, AnnotationSelectorSerializer

"""
{ 
  "@context": "http://www.w3.org/ns/anno.jsonld",
  "id": "#218d01ff-f077-4cc3-992d-1c81c426e51b",
  "type": "Annotation",
  "creator" : user-id, 
  "body": {
    "id": "http://34.125.134.88/body1",
    "type": "TextualBody",
    "value": "Nice picture"
  },
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

    def test_target_serializer(self):
      selectorType = create_or_return_selectortype("fragmentselector")
      typeImage = create_or_return_type("image")
      selector = Selector.objects.create(value="xywh=pixel:270,120,90,170", type=selectorType)
      target = Target.objects.create(source="http://34.125.134.88/artitems/14", type= typeImage, selector=selector)
      
      self.assertEqual({'id': 'http://34.125.134.88/image{}'.format(target.id), 
      'source': 'http://34.125.134.88/artitems/14', 
      'type': 'Image', 
      'selector': {'value': 'xywh=pixel:270,120,90,170', 
                  'type': 'FragmentSelector', 
                  'conformsTo': 'http://www.w3.org/TR/media-frags/'}}, AnnotationTargetSerializer(target).data)

    def test_body_serializer(self):
      typeText = create_or_return_type("text")
      motivation = create_or_return_motivation("commenting")
      value = self.faker.paragraph(nb_sentences=3)

      body = Body.objects.create(type=typeText, value=value, purpose=motivation)

      data = AnnotationBodySerializer(body).data
      data.pop('created')
      self.assertEqual({'id': 'http://34.125.134.88/body{}'.format(body.id), 
      'value': value, 
      'type': 'Text', 
      'format': 'text/plain', 
      'purpose': 'Commenting'}, data)

    def test_selector_serializer(self):
      selectorType = create_or_return_selectortype("fragmentselector")
      selector = Selector.objects.create(value="xywh=pixel:270,120,90,170", type=selectorType)
      
      self.assertEqual({'value': 'xywh=pixel:270,120,90,170', 
      'type': 'FragmentSelector', 
      'conformsTo': 'http://www.w3.org/TR/media-frags/'}, AnnotationSelectorSerializer(selector).data)

    def test_helpers(self):
      type1 = create_or_return_type("image")
      type2 = create_or_return_type("failure")
      motivation1 = create_or_return_motivation("commenting")
      motivation2 = create_or_return_motivation("failure")
      selectorType1 = create_or_return_selectortype("fragmentselector")
      selectorType2 = create_or_return_selectortype("failure")

      self.assertEqual(type2, -1)
      self.assertEqual(type1.type.value, "Image")
      self.assertEqual(motivation2, -1)
      self.assertEqual(motivation1.motivation.value, "Commenting")
      self.assertEqual(selectorType2, -1)
      self.assertEqual(selectorType1.selectorType.value, "FragmentSelector")

    def test_annotation_without_body(self):
      typeImage = create_or_return_type("image")
      typeAnnotation = create_or_return_type("annotation")
      selectorType = create_or_return_selectortype("fragmentselector")

      selector = Selector.objects.create(value="xywh=pixel:270,120,90,170", type=selectorType)
      target = Target.objects.create(source="http://34.125.134.88/artitems/14", type=typeImage, selector=selector)

      ann = Annotation.objects.create(uuid="#218d01ff-f077-4cc3-992d-1c81c426e51b", type=typeAnnotation, target=target, creator='1')
      expected = {"@context": "http://www.w3.org/ns/anno.jsonld", "id": "#218d01ff-f077-4cc3-992d-1c81c426e51b", "type": "Annotation", "creator" : 1, "target": {"id": "http://34.125.134.88/image{}".format(target.id), "source": "http://34.125.134.88/artitems/14", "type": "Image", "selector": {"type": "FragmentSelector","conformsTo": "http://www.w3.org/TR/media-frags/","value": "xywh=pixel:270,120,90,170"}}}
      actual = AnnotationSerializer(ann).data
     
    
    def tearDown(self):
      pass

