from django import template

register = template.Library()


@register.filter
def rtruncate(value, length=40):
    if value is not None and isinstance(value, str):
        if len(value) > length:
            return " ..." + value[len(value) - length:len(value)]
    return value
