from django.template import Library

register = Library()


@register.filter
def mod(num,val):
    return num%val == 0

