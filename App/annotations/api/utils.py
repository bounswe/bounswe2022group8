from django.test import TestCase, RequestFactory
from faker import Faker
from .views import annotate

# utils for unit tests
class Utils:
    def __init__(self):
        self.faker = Faker()
        self.factory = RequestFactory()


    def text_annotation(self, creator):
      bodyid = "http://34.125.134.88/body1"
      source = "https://cmpe451-development.s3.amazonaws.com/artitem/artitem-1.png"
      bodytype= "TextualBody"
      bodyvalue = self.faker.pystr(min_chars = 10)
      exact = self.faker.paragraph(nb_sentences=3)
      start = self.faker.pyint()
      end = start + self.faker.pyint()
      data = {
        "id": "#2395b9aa-64f0-46a7-a561-90f67ebb2193",
        "body": [
            {
                "id": bodyid,
                "value": bodyvalue,
                "type": bodytype,
                "creator": {
                  "id": 1,
                  "name": "joseph.blocker"
                }
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
      return response.data

    def image_annotation(self, creator):
      bodyid = "http://34.125.134.88/body1"
      source = "https://cmpe451-development.s3.amazonaws.com/artitem/artitem-1.png"
      bodytype= "TextualBody"
      selectortype = "FragmentSelector"
      bodyvalue = self.faker.pystr(min_chars = 10)
      targetvalue = self.faker.pystr(min_chars = 10)
      data = { 
        "@context": "http://www.w3.org/ns/anno.jsonld",
        "id": "#218d01ff-f077-4cc3-992d-1c81c426e51b",
        "type": "Annotation",
        "creator" : creator, 
        "body": [{
          "id": bodyid,
          "type": bodytype,
          "value": bodyvalue,
          "creator": {
            "id": 1,
            "name": "joseph.blocker"
        }
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
      return response.data

utils = Utils()