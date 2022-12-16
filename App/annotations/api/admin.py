from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Type)
admin.site.register(Motivation)
admin.site.register(Selector)
admin.site.register(Body)
admin.site.register(Target)
admin.site.register(Annotation)