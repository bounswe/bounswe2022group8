from django.test import TestCase
from faker import Faker
from .models import *
from .serializers import AnnotationSerializer, AnnotationBodySerializer

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
    "id": "https://cmpe451-development.s3.amazonaws.com/artitem/artitem-1.png"
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

    def test_annotation_serializer(self):
        typeAnnotation = Type.objects.create(type=TypeEnum.annotation)
        typeImage = Type.objects.create(type=TypeEnum.image)
        typeText = Type.objects.create(type=TypeEnum.textualbody)

        purpose = "commenting"
        motivation = create_or_return_motivation(purpose)
        
        body = Body.objects.create(type=typeText, value = "Nice picture", purpose= motivation)

        print(AnnotationBodySerializer(body).data)
        #target = Target.objects.create(type=typeImage)
        """
        target = Target.objects.create(target="http://34.125.134.88/artitems/14", type=typeImage)
        ann = Annotation.objects.create(body=body, type=typeAnnotation, target=target, creator='1')
        expected = {'id': "http://34.125.134.88/anno1", 'body': "nice picture", 'type': TypeEnum.ANNOTATION, 'target': targetText, '@context': 'http://www.w3.org/ns/anno.jsonld'}
        actual = AnnotationSerializer(ann).data
        self.assertEqual(expected, actual)
        
        print(AnnotationSerializer(ann).data)
        """
    
    def tearDown(self):
        pass

