from django.urls import path
from shop.views import HomeListView, ProductByCategoryView, product_detail

app_name = 'shop'

urlpatterns = [
    path('', HomeListView.as_view(), name='home'),
    # path('<str:slug>/', ProductByCategoryView.as_view(), name='category'),

    path('<int:id>/<slug:slug>/', product_detail, name='detail'),
]
