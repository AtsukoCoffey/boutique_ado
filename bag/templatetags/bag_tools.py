from django import template

# to register this filter, create a variable called register.
register = template.Library()


# this takes in a price and a quantity as parameters
# register filter decorator to register function as a template filter.
# Django doc: custom template tags and filter
@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    return price * quantity
