from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.

"""
According to the Web Data Annotation Model,
Annotation model must have two properties and three relationships:
@context: property
id: property
type: relationship - an annotation MUST have 1 or more types
body: relationship
target: relationship

If there is only one @context value, then it must be provided as a string.
1) An Annotation must have 1 or more types. One of the types must be "Annotation"
2) Annotation should have 1 or more body but it can be 0 though.
3) Annotation must have 1 or more targets.
"""

# Default values:
TYPE = "Annotation"
CONTEXT = "http://www.w3.org/ns/anno.jsonld"
URL = "http://34.125.134.88/"  # default url

class Body(models.Model):
    body = models.TextField(unique=True)

class TextualBody(models.Model):
    pass

class Type(models.Model):
    type = models.TextField(unique=True)

class Target(models.Model):
    target = models.TextField(unique=True)
    format = models.TextField(blank=True)
    language = ArrayField(models.CharField(max_length=10, blank=True), blank=True, null=True)
    textDirection = models.TextField(blank=True)
    processingLanguage = models.TextField(blank=True)

class Annotation(models.Model):  # id is created implicitly
    context = models.TextField(default=CONTEXT)
    url = models.TextField(default=URL)
    type = models.ForeignKey(Type, on_delete=models.CASCADE, to_field='type', default=TYPE)  # create a type object with "annotation" type
    body = models.ForeignKey(Body, on_delete=models.CASCADE, to_field='body')
    target = models.ForeignKey(Target, on_delete=models.CASCADE, to_field='target')

"""
class TextAnnotation(models.Model):
    @staticmethod
    def context():
        return "http://www.w3.org/ns/anno.jsonld"

    @staticmethod
    def type():
        return "Annotation"

    motivation = models.TextField()
    body = models.ForeignKey('Body', on_delete=models.CASCADE)
    target = models.ForeignKey('Target', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey('user.User', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)


class ImageAnnotation(models.Model):
    @staticmethod
    def context():
        return "http://www.w3.org/ns/anno.jsonld"

    @staticmethod
    def type():
        return "Annotation"

    motivation = models.TextField()
    body = models.ForeignKey('Body', on_delete=models.CASCADE)
    target = models.ForeignKey('ImageTarget', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey('user.User', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)


class Body(models.Model):
    value = models.TextField()

    @staticmethod
    def type():
        return "TextualBody"

    @staticmethod
    def language():
        return "en"

    @staticmethod
    def format():
        return "text/html"

    def __str__(self):
        return str(self.id)


class ImageTarget(models.Model):
    source = models.TextField()
    scope = models.TextField()
    selector = models.ForeignKey('FragmentSelector', on_delete=models.CASCADE)

    @staticmethod
    def type():
        return "Image"

    def __str__(self):
        return str(self.id)


class Target(models.Model):
    source = models.TextField()
    selector = models.ForeignKey('Selector', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)


class FragmentSelector(models.Model):
    value = models.TextField()

    @staticmethod
    def conformsTo():
        return "http://www.w3.org/TR/media-frags/"

    @staticmethod
    def type():
        return "FragmentSelector"

    def __str__(self):
        return str(self.id)


class Selector(models.Model):
    startSelector = models.ForeignKey('StartEndSelector', on_delete=models.CASCADE, related_name='startSelector')
    endSelector = models.ForeignKey('StartEndSelector', on_delete=models.CASCADE, related_name='endSelector')

    @staticmethod
    def type():
        return "RangeSelector"

    def __str__(self):
        return str(self.id)


class StartEndSelector(models.Model):
    value = models.TextField()
    refinedBy = models.ForeignKey('RefinedBy', on_delete=models.CASCADE)

    @staticmethod
    def type():
        return "XPathSelector"

    def __str__(self):
        return str(self.id)


class RefinedBy(models.Model):
    start = models.IntegerField()
    end = models.IntegerField()

    @staticmethod
    def type():
        return "TextPositionSelector"

    def __str__(self):
        return str(self.id)

"""