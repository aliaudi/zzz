from django.urls import path
from products import views 
app_name='Myproduct'
urlpatterns = [
    path('home',views.index,name="index"),
    path('<slug:slug>',views.product_detail,name='prodetail')
    ]