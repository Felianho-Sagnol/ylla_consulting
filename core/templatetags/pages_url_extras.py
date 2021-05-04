
from django import template


from flex.models import (
                About,
                )





register = template.Library()



@register.simple_tag(name="about_page")
def about_page():
    return About.objects.first()
