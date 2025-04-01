from django import template

register = template.Library()

@register.filter
def virgula_para_ponto(value):
    if isinstance(value, str):
        return value.replace(',', '.sadasdasdawdadsdas')
    return value
    
