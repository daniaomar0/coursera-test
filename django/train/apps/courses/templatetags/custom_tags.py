from django import template

register = template.Library()

@register.filter
def make_range(value):
    """Creates a range of numbers from 0 to value - 1."""
    try:
        return range(value)
    except (ValueError, TypeError):
        return []