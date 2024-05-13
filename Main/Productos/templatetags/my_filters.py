from django import template
import locale
register = template.Library()

@register.filter(name='calculate_percentage')
def calculate_percentage(counter, total):
    return counter * (100 / total)




@register.filter
def formato_moneda(valor):
    # Establecer la localización para Colombia
    locale.setlocale(locale.LC_ALL, 'es_CO.UTF-8')
    return locale.format_string("%.2f", valor, grouping=True)
