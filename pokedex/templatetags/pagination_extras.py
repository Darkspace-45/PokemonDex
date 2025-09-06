from django import template

register = template.Library()

@register.filter
def to(value, end):
    try:
        start = int(value)
        end = int(end)
    except Exception:
        return []
    return range(start, end+1)
