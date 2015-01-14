from django import template
from django.utils import translation
 
register = template.Library()
 
@register.filter
def get_object_translation(obj):
    # get current language
    lang = translation.get_language()
 
    try:
        # returns object with current translation
        for i in obj.translation.all():
            if i.lang == lang:
                return i
    except:
        pass
 
    # returns object without translation
    return obj