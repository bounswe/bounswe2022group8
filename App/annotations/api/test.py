from django.test import TestCase
from faker import Faker
from .models import *
from .serializers import AnnotationSerializer


class TestAnnotations(TestCase):
    def setUp(self):
        self.faker = Faker()
        self.type = "Annotation"
        self.url = "http://example.org/"

    def test_annotation_serializer(self):
        body = Body.objects.create(body= self.url + self.faker.word())
        type = Type.objects.create(type=self.type)
        target = Target.objects.create(target= self.url + self.faker.word())

        ann = Annotation.objects.create(body=body, type=type, target=target)
        print(AnnotationSerializer(ann).data)
    
    def tearDown(self):
        pass

