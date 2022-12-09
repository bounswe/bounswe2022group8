from django.db import models

# Create your models here.

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