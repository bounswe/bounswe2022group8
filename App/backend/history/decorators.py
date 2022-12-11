import functools
from django.shortcuts import redirect
from django.http import HttpResponseBadRequest
from .signals import object_viewed_signal
from api.models.artitem import ArtItem

from functools import wraps
from django.contrib import messages
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib.auth.models import AnonymousUser

# def object_viewed_decorator(function, request):

#     if request.user.is_authenticated:
#         # We do not apply the decorator to the function
#         return function
#     else:
#         # We apply the decorator and return the new function
#         return newrelic.agent.function_trace()(function)

def bject_viewed_decorator(view_func):
    print("came there")
    @functools.wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            try:
                instance = view_func.get_object()
            except view_func.model.DoesNotExist:
                instance = None
            object_viewed_signal.send(instance.__class__, instance=instance, request=request)
            print("came here")
            return view_func(request, *args, **kwargs)
        return view_func(request, *args, **kwargs)  
    return wrapper

def auth_test_function(user):
    if user.is_authenticated:
        return True
    return False

def object_viewed_decorator():
    #print("came 1")
    def decorator(view):
        @wraps(view)
        def _wrapped_view(request, *args, **kwargs):
            #print("came 2")
            #print(request.user)
            if(isinstance(request.user, AnonymousUser)):
                #print("what")
                #print(request.user)
                pass
            else:
                #print("came 3")
                #print(kwargs["id"])
                try:
                    artitem = ArtItem.objects.get(pk=kwargs["id"])
                    instance = artitem
                    object_viewed_signal.send(instance.__class__, instance=instance, request=request)
                
                   # instance = view.get_object()
                except view.model.DoesNotExist:
                    instance = None
                #object_viewed_signal.send(instance.__class__, instance=instance, request=request)
                #print("came here")
                return view(request, *args, **kwargs)

            # if not auth_test_function(request.user):
            #     print("came 3")
            #     print(kwargs["id"])
            #     try:
            #         artitem = ArtItem.objects.get(pk=kwargs["id"])
            #         instance = artitem
            #         object_viewed_signal.send(instance.__class__, instance=instance, request=request)
                
            #        # instance = view.get_object()
            #     except view.model.DoesNotExist:
            #         instance = None
            #     #object_viewed_signal.send(instance.__class__, instance=instance, request=request)
            #     print("came here")
            #     return view(request, *args, **kwargs)
            return view(request, *args, **kwargs)

        return _wrapped_view
    return decorator