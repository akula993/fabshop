from django import template
from shop.models import Category

register = template.Library()


@register.inclusion_tag('shop/menu_tpl.html')
def show_menu(menu_class='category-products'):
    categories = Category.objects.all()
    return {"categories": categories, 'menu_class': menu_class}

