from django import template

register = template.Library()


@register.filter(name='multply')
def multiply(price, quantity):
    return price * quantity
