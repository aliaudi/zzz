from django.db import models
from django.utils.text import slugify
from django.urls import reverse 
# Create your models here.


class Myproduct(models.Model):

    name=models.CharField(max_length=50)
    brande=models.CharField( max_length=50)
    category=models.CharField(max_length=50)
    detail=models.TextField()
    price=models.IntegerField()
    img=models.ImageField(upload_to="imgproduct" )
    slug=models.SlugField(blank=True,null=True)
   
    def save(self,*args,**kwargs) :
        if not self.slug :
            self.slug=slugify(self.name)
        super(Myproduct, self).save(*args,**kwargs)
    def get_absolute_url(self):
        return reverse("Myproduct:prodetail", kwargs={"slug": self.slug})    
    def __str__(self):
        return self.name

   