from django import template

register = template.Library()

@register.filter(name='calculate_percentage')
def calculate_percentage(counter, total):
    return counter * (100 / total)
