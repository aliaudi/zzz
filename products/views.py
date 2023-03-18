from django.shortcuts import render
from .models import Myproduct
# Create your views here.
def index(request):
    x=Myproduct.objects.all()
    content={'h':x}
    return render(request,"index.html",content) 
def product_detail(request,slug): 
    product_detail=Myproduct.objects.get(slug=slug) 
    # accessories=Product_Accessories.objects.all() 
    content={'prodetail':product_detail}
    return render (request,'prodetail.html',content)
   


    