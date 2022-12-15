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
FORMAT = "text/plain"
CONTEXT = "http://www.w3.org/ns/anno.jsonld"
URL = "http://34.125.134.88/"  # default url

class TypeEnum(models.TextChoices):
    annotation = 'Annotation'
    image = 'Image'
    text = 'Text'
    dataset = 'Dataset'
    sound = 'Sound'
    vidoe = 'Video'
    textualbody = 'TextualBody'

class MotivationEnum(models.TextChoices):
    assessing = 'Assessing'
    bookmarking = 'Bookmarking'
    classifying = 'Classifying'
    commenting = 'Commenting'
    describing = 'Describing'
    editing = 'Editing'
    highlighting = 'Highlighting'
    identifying = 'Identifying'
    linking = "Linking"
    moderating = "Moderating"
    questioning = "Questioning"
    replying = "Replying"
    tagging = "Tagging"

class SelectorEnum(models.TextChoices):
    fragment = "FragmentSelector"
    svg = "SvgSelector"
    css = "CssSelector"
    xpath = "XPathSelector"
    textquote = "TextQuoteSelector"
    textposition = "TextPositionSelector"
    dataposition = "DataPositionSelector"

class Type(models.Model):
    type = models.TextField(unique=True, choices=TypeEnum.choices)

class Motivation(models.Model):
    motivation = models.TextField(unique=True, choices=MotivationEnum.choices)

class Selector(models.Model):
    value = models.TextField()
    type = models.TextField(unique=True, choices=SelectorEnum.choices)

"""
"body": "http://34.125.134.88/body<id>"  (id will be stored in the field - serializer will serialize as shown)
"type": "TextualBody",
"value": "Nice picture"
"format": "text/plain"
"created": "2015-10-13T13:00:00Z"
"purpose": "questioning"
"""
class Body(models.Model):
    body = models.TextField(primary_key=True)
    type = models.ForeignKey(Type, on_delete=models.CASCADE, to_field='type', default=TypeEnum.textualbody)  # create a type object with "annotation" type
    value = models.TextField()
    format = models.TextField(default=FORMAT)
    created = models.DateTimeField(auto_now=True)
    purpose = models.ForeignKey(Motivation, on_delete=models.CASCADE, to_field='motivation', blank=True, null=True)

"""
"target": "http://34.125.134.88/target<id>"    (id will be stored in the field - serializer will serialize as shown)
"type": "TextualBody",
"source": "http://34.125.134.88/artitems/14",  
"format": "image/png",
"language": ["en"],
"type": "image",
"selector": {
      "type": "FragmentSelector",
      "conformsTo": "http://www.w3.org/TR/media-frags/",
      "value": "xywh=pixel:270,120,90,170"
    }
"""
class Target(models.Model):
    source = models.TextField()
    target = models.TextField(primary_key=True)
    format = models.TextField(blank=True)
    language = ArrayField(models.CharField(max_length=10, blank=True, default="en"), blank=True, null=True)
    type = models.ForeignKey(Type, on_delete=models.CASCADE, to_field='type', default=TypeEnum.image)  # create a type object with "annotation" type
    selector = models.ForeignKey(Selector, on_delete=models.CASCADE)

class Annotation(models.Model):  # id is created implicitly
    context = models.TextField(default=CONTEXT)
    url = models.TextField(default=URL)
    type = models.ForeignKey(Type, on_delete=models.CASCADE, to_field='type', default=TypeEnum.annotation)  # create a type object with "annotation" type
    body = models.ForeignKey(Body, on_delete=models.CASCADE, to_field='body')
    target = models.ForeignKey(Target, on_delete=models.CASCADE, to_field='target')
    creator = models.BigIntegerField()    # id of the creator
    created = models.DateTimeField(auto_now=True)
    modified = models.DateTimeField(auto_now=True)

##### HELPERS

def create_or_return_motivation(motivation):
    try:
        motivationEnum = MotivationEnum[motivation]
        obj = Motivation.objects.filter(motivation=motivationEnum)
        if(obj): return obj[0]
        else: return Motivation.objects.create(motivation=motivationEnum)
    except:
        return -1

def create_or_return_type(type):
    try:
        typeEnum = TypeEnum[type]
        obj = Type.objects.filter(type=typeEnum)
        if(obj): return obj[0]
        else: return Type.objects.create(type=typeEnum)
    except:
        return -1
"""
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