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
CONFORM = "http://www.w3.org/TR/media-frags/"

class TypeEnum(models.TextChoices):
    annotation = 'Annotation'
    image = 'Image'
    text = 'Text'
    dataset = 'Dataset'
    sound = 'Sound'
    vidoe = 'Video'
    textualbody = 'TextualBody'

class MotivationEnum(models.TextChoices):
    assessing = 'assessing'
    bookmarking = 'bookmarking'
    classifying = 'classifying'
    commenting = 'commenting'
    describing = 'describing'
    editing = 'editing'
    highlighting = 'highlighting'
    identifying = 'identifying'
    linking = "linking"
    moderating = "moderating"
    questioning = "questioning"
    replying = "replying"
    tagging = "tagging"

class SelectorEnum(models.TextChoices):
    fragmentselector = "FragmentSelector"
    svgselector = "SvgSelector"
    cssselector = "CssSelector"
    xpathselector = "XPathSelector"
    textquoteselector = "TextQuoteSelector"
    textpositionselector = "TextPositionSelector"
    datapositionselector = "DataPositionSelector"

class Type(models.Model):
    type = models.TextField(unique=True, choices=TypeEnum.choices)

class Motivation(models.Model):
    motivation = models.TextField(unique=True, choices=MotivationEnum.choices)

class FragmentSelector(models.Model):
    value = models.TextField()
    type = SelectorEnum.fragmentselector
    conformsTo = models.TextField(default=CONFORM, blank=True)

class TextQuoteSelector(models.Model):
    exact = models.TextField()
    type = SelectorEnum.textquoteselector

class TextPositionSelector(models.Model):
    start = models.BigIntegerField()
    end = models.BigIntegerField()
    type = SelectorEnum.textpositionselector

class Selector(models.Model):
    fragmentSelector = models.ForeignKey(FragmentSelector, on_delete= models.CASCADE, blank=True, null=True)
    textQuoteSelector = models.ForeignKey(TextQuoteSelector,  on_delete= models.CASCADE, blank=True, null=True)
    textPositionSelector = models.ForeignKey(TextPositionSelector, on_delete= models.CASCADE, blank=True, null=True)
    
class Creator(models.Model):
    id = models.BigIntegerField(primary_key = True)  
    name = models.TextField()
    
"""
"body": "http://34.125.134.88/body<id>"  (id will be stored in the field - serializer will serialize as shown)
"type": "TextualBody",
"value": "Nice picture"
"format": "text/plain"
"created": "2015-10-13T13:00:00Z"
"purpose": "questioning"
"""
class Body(models.Model):
    type = models.ForeignKey(Type, on_delete=models.CASCADE, to_field='type')  # create a type object with "annotation" type
    value = models.TextField()
    format = models.TextField(default=FORMAT)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey(Creator, on_delete=models.CASCADE)
    purpose = models.ForeignKey(Motivation, on_delete=models.CASCADE, to_field='motivation',  blank=True, null=True)

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
    format = models.TextField(blank=True)
    language = ArrayField(models.CharField(max_length=10, blank=True), blank=True, null=True)
    type = models.ForeignKey(Type, on_delete=models.CASCADE, to_field='type', blank=True, null=True)  # create a type object with "annotation" type
    selector = models.ForeignKey(Selector, on_delete=models.CASCADE)

class Annotation(models.Model):  # id is created implicitly
    id = models.TextField(primary_key = True)                    # coming from frontend
    context = models.TextField(default=CONTEXT)
    type = models.ForeignKey(Type, on_delete=models.CASCADE, to_field='type')  # create a type object with "annotation" type
    body = models.ManyToManyField(Body)
    target = models.ForeignKey(Target, on_delete=models.CASCADE, to_field='id')
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