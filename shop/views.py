from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import Product, Category


class HomeListView(ListView):
    model = Product
    template_name = "shop/home.html"
    context_object_name = 'categorys'
    def get_queryset(self):
        self.category = Category.objects.get(slug=self.kwargs['slug'])
        queryset = Product.objects.filter(category=self.category)
        return queryset
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(HomeListView, self).get_context_data()
        context['title'] = self.category
        return context

class ProductByCategoryView(ListView):
    context_object_name = 'product'
    template_name = 'shop/post_list.html'

def product_detail(request, id, slug):
    """ Страница продукта"""
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    context = {'product': product}
    return render(request, 'shop/detail.html', context)