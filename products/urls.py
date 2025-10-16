from django.urls import path
from .views import (
    HomeView,
    ProductsListView,
    ProductDetailView,
    TestTemplateView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,
    ProductUnpublishView
)

app_name = 'products'

urlpatterns = [
    path('', ProductsListView.as_view(), name='list'),
    path('home/', HomeView.as_view(), name='home'),
    path('create/', ProductCreateView.as_view(), name='create'),
    path('<int:product_id>/', ProductDetailView.as_view(), name='detail'),
    path('<int:product_id>/update/', ProductUpdateView.as_view(), name='update'),
    path('<int:product_id>/delete/', ProductDeleteView.as_view(), name='delete'),
    path('<int:product_id>/unpublish/', ProductUnpublishView.as_view(), name='unpublish'),
    path('test/', TestTemplateView.as_view(), name='test'),
]