from django import template

register = template.Library()

# quantity is either lone integer or a dictionary with quantity by size

@register.simple_tag
def calc_subtotal(price, quantity, size_this_row='none'):
    if isinstance(quantity, dict):
        inner_dict = quantity['items_by_size']
        qty_this_row = inner_dict[size_this_row]
    else:
        qty_this_row = quantity

    return price * qty_this_row
