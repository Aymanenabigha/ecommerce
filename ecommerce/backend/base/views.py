from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, HttpResponseRedirect
from .models import Product
from .forms import ProductForm
from rest_framework.views import APIView
from rest_framework.response import Response
from  .serializers import ProductSerializer

# Create your views here.
class Home(APIView):
    def get(self,request):
        return render(request,"hello.html",{})
class ProduitList(APIView):
    def get(self,request):
        product= Product.objects.all()
        serializer=ProductSerializer(product,many=True)
        #return render(request,'listProduit.html',{'produits':product})
        return Response(serializer.data)
class ProductDetail(APIView):
    def get(self,request,pk):
        product= Product.objects.get(id=pk)
        serializer = ProductSerializer(product, many=False)
        #return render(request,'productDetail.html',{'produits':product})
        return Response(serializer.data)
class ProductCreate(APIView):
    def get(self, request):
        form=ProductForm()
        return render(request,'productCreate.html',{'form':form})

    def post(self, request):
        # request.FILES au cas ou on aura des images
        form=ProductForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/products/')
        return render(request,'productCreate.html',{'form':form})