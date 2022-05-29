from django.urls import path,include
from .views import Home,ProduitList,ProductDetail,ProductCreate
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static

urlpatterns=[
     path('home/',Home.as_view(),name='home'),
     path('products/',ProduitList.as_view(),name='produit'),
     path('products/<int:pk>',ProductDetail.as_view(),name='detailProduit'),
     path('creatproduct/',ProductCreate.as_view(),name='createproduit'),

             ]
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)