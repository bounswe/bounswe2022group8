from django.test import TestCase, RequestFactory
from faker import Faker
from .models import *
from .serializers import AnnotationSerializer, AnnotationBodySerializer, AnnotationTargetSerializer, FragmentSelectorSerializer, SelectorSerializer
from .views import *
from .utils import utils
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
        print("TestAnnotation:setUp_:begin")
        self.faker = Faker()
        self.factory = RequestFactory()
        # do something
        print("TestAnnotation:setUp_:end")

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

    
    # POST image annotation test
    def test_create_image_annotation(self):
      source = "http://34.125.134.88/artitems/14"
      bodytype= "TextualBody"
      selectortype = "FragmentSelector"
      bodyvalue = self.faker.pystr(min_chars = 10)
      targetvalue = self.faker.pystr(min_chars = 10)
      creator = self.faker.pyint()
      data = { 
        "@context": "http://www.w3.org/ns/anno.jsonld",
        "id": "#218d01ff-f077-4cc3-992d-1c81c426e51b",
        "type": "Annotation",
        "creator" : creator, 
        "body": [{
          "type": bodytype,
          "value": bodyvalue
        }],
        "target": {
          "source": source,
          "selector": {
            "type": selectortype,
            "conformsTo": "http://www.w3.org/TR/media-frags/",
            "value": targetvalue
          }
        }
      }

      request = self.factory.post('annotations/', data, content_type='application/json')
      response = annotate(request) 

      self.assertEqual(response.status_code, 201)
      expected_body = {
        "value": bodyvalue,
        "type": "Text",
        "format": "text/plain",
        "purpose": "Commenting"
      }
      actual_body = response.data['body'][0] # it returns a list
      actual_body.pop('created')
      actual_body.pop('id')

      self.assertEqual(actual_body, expected_body)

      expected_target =  {
        "source": source,
        "type": "Image",
        "selector": {
          "value": targetvalue,
          "type": "FragmentSelector",
          "conformsTo": "http://www.w3.org/TR/media-frags/"
        }
      }
      actual_target = response.data['target']
      actual_target.pop('id')
      self.assertEqual(actual_target, expected_target) 
      self.assertEqual(response.data['creator'], creator)
      self.assertEqual(response.data['@context'], "http://www.w3.org/ns/anno.jsonld")
    
    # POST text annotation test
    def test_create_text_annotation(self):
      source = "https://cmpe451-development.s3.amazonaws.com/artitem/artitem-1.png"
      bodytype= "TextualBody"
      bodyvalue = self.faker.pystr(min_chars = 10)
      creator = self.faker.pyint()
      exact = self.faker.paragraph(nb_sentences=3)
      start = self.faker.pyint()
      end = start + self.faker.pyint()
      data = {
        "id": "#2395b9aa-64f0-46a7-a561-90f67ebb2193",
        "body": [
            {
                "value": bodyvalue,
                "type": bodytype,
            }
        ],
        "type": "Annotation",
        "target": {
            "source": source,
            "selector": [
                {
                    "exact": exact,
                    "type": "TextQuoteSelector"
                },
                {
                    "start": start,
                    "end": end,
                    "type": "TextPositionSelector"
                }
            ]
        },
        "creator": creator,
        "@context": "http://www.w3.org/ns/anno.jsonld"
      }

      request = self.factory.post('annotations/', data, content_type='application/json')
      response = annotate(request) 

      self.assertEqual(response.status_code, 201)
      expected_body = {
        "value": bodyvalue,
        "type": "Text",
        "format": "text/plain",
        "purpose": "Commenting"
      }
      actual_body = response.data['body'][0] # it returns a list
      actual_body.pop('created')
      actual_body.pop('id')

      self.assertEqual(actual_body, expected_body)

      expected_target =  {
        "source": source,
        "type": "Image",
        "selector": [
            {
              "exact": exact,
              "type": "TextQuoteSelector"
          },
          {
              "start": start,
              "end": end,
              "type": "TextPositionSelector"         
          }
        ]
      }
      actual_target = response.data['target']
      actual_target.pop('id')
      self.assertEqual(actual_target, expected_target) 
      self.assertEqual(response.data['creator'], creator)
      self.assertEqual(response.data['@context'], "http://www.w3.org/ns/anno.jsonld")
    
    # PUT edit annotation test
    def test_edit_annotation(self):
      creator = self.faker.pyint()
      img_annotation = utils.image_annotation(creator)

      updbody = self.faker.pystr(min_chars = 10)
      value = self.faker.pystr(min_chars = 10)

      data = { 
        "@context": "http://www.w3.org/ns/anno.jsonld",
        "id": "#218d01ff-f077-4cc3-992d-1c81c426e51b",
        "type": "Annotation",
        "creator" : creator, 
        "body": [{
          "type": "TextualBody",
          "value": updbody
        }],
        "target": {
          "source": img_annotation['target']['source'],
          "selector": {
            "type": "FragmentSelector",
            "conformsTo": "http://www.w3.org/TR/media-frags/",
            "value": value
          }
        }
      }
      request = self.factory.put('annotations/', data, content_type='application/json')
      response = annotate(request) 

      self.assertEqual(response.status_code, 200)
      self.assertEqual(updbody, response.data['body'][0]['value'])
      self.assertEqual(value, response.data['target']['selector']['value'])
  
    def __inc(self, annotationID, annotations):
      return any([annotationID == ann['id'] for ann in annotations])

    # ALL annotations
    def test_get_image_annotations1(self):
      creator = self.faker.pyint()
      img_annotation = utils.image_annotation(creator)

      # get all annotations
      request = self.factory.get('annotations/', content_type='application/json')
      response = annotate(request)
      self.assertEqual(response.status_code, 200)
      self.assertTrue(self.__inc(img_annotation['id'], response.data))

    # ALL image annotations
    def test_get_image_annotations2(self):
      creator = self.faker.pyint()
      img_annotation = utils.image_annotation(creator)
      # get all image annotations
      request = self.factory.get('annotations/image/', content_type='application/json')
      response = get_image_annotations(request)
      self.assertEqual(response.status_code, 200)
      self.assertTrue(self.__inc(img_annotation['id'], response.data))

    # ALL image annotations on an art item
    def test_get_image_annotations3(self):
      creator = self.faker.pyint()
      img_annotation = utils.image_annotation(creator)
      # get all image annotations on an art item
      request = self.factory.get('annotations/image/artitems/', content_type='application/json')
      response = get_image_annotation_by_artitem_id(request, int(img_annotation['target']['source'].split('-')[-1].split('.')[0]))
      self.assertEqual(response.status_code, 200)
      self.assertTrue(self.__inc(img_annotation['id'], response.data))

    # ALL image annotations of a user
    def test_get_image_annotations4(self):
      creator = self.faker.pyint()
      img_annotation = utils.image_annotation(creator)
      # get all image annotations of a user
      request = self.factory.get('annotations/image/users/', content_type='application/json')
      response = get_image_annotation_by_user_id(request, creator)
      self.assertEqual(response.status_code, 200)
      self.assertTrue(self.__inc(img_annotation['id'], response.data))

    # ALL image annotations of a user on an art item
    def test_get_image_annotations5(self):
      creator = self.faker.pyint()
      img_annotation = utils.image_annotation(creator)
      # get all image annotations of a user
      request = self.factory.get('annotations/image/users/artitems', content_type='application/json')
      response = get_image_annotation_by_artitem_user_id(request, creator, int(img_annotation['target']['source'].split('-')[-1].split('.')[0]))
      self.assertEqual(response.status_code, 200)
      self.assertTrue(self.__inc(img_annotation['id'], response.data))


    # ALL annotations
    def test_get_text_annotations1(self):
      creator = self.faker.pyint()
      img_annotation = utils.text_annotation(creator)

      # get all annotations
      request = self.factory.get('annotations/', content_type='application/json')
      response = annotate(request)
      self.assertEqual(response.status_code, 200)
      self.assertTrue(self.__inc(img_annotation['id'], response.data))

    # ALL text annotations
    def test_get_text_annotations2(self):
      creator = self.faker.pyint()
      img_annotation = utils.text_annotation(creator)
      # get all image annotations
      request = self.factory.get('annotations/text/', content_type='application/json')
      response = get_text_annotations(request)
      self.assertEqual(response.status_code, 200)
      self.assertTrue(self.__inc(img_annotation['id'], response.data))

    # ALL text annotations on an art item
    def test_get_text_annotations3(self):
      creator = self.faker.pyint()
      img_annotation = utils.text_annotation(creator)
      # get all text annotations on an art item
      request = self.factory.get('annotations/text/artitems/', content_type='application/json')
      response = get_text_annotations_by_artitem_id(request, int(img_annotation['target']['source'].split('-')[-1].split('.')[0]))
      self.assertEqual(response.status_code, 200)
      self.assertTrue(self.__inc(img_annotation['id'], response.data))

    # ALL text annotations of a user
    def test_get_text_annotations4(self):
      creator = self.faker.pyint()
      img_annotation = utils.text_annotation(creator)
      # get all image annotations of a user
      request = self.factory.get('annotations/text/users/', content_type='application/json')
      response = get_text_annotations_by_userid(request, creator)
      self.assertEqual(response.status_code, 200)
      self.assertTrue(self.__inc(img_annotation['id'], response.data))

    # ALL text annotations of a user on an art item
    def test_get_text_annotations5(self):
      creator = self.faker.pyint()
      img_annotation = utils.text_annotation(creator)
      # get all image annotations of a user
      request = self.factory.get('annotations/text/users/artitems', content_type='application/json')
      response = get_text_annotation_by_artitem_user_id(request, creator, int(img_annotation['target']['source'].split('-')[-1].split('.')[0]))
      self.assertEqual(response.status_code, 200)
      self.assertTrue(self.__inc(img_annotation['id'], response.data))

    # cleaning
    def tearDown(self):
        print("TestAnnotation:setUp_:begin")
        print("TestAnnotation:setUp_:end")

