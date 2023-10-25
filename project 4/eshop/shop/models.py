from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    GENDER_CHOICES = [
        ('M', 'Men'),
        ('W', 'Women'),
    ]
    
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)
    description = models.TextField(max_length=500, blank=True)
    image = models.ImageField(upload_to='category', blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='M')

    
    class Meta:
        ordering=['name']
        verbose_name='category'
        verbose_name_plural='categories'
        
    def get_url(self):
        return reverse('shop:products_by_category',args=[self.slug])
        
    def __str__(self):
        return  '{}'.format(self.name)

class Product(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    name=models.CharField(max_length=50,unique=True)
    slug=models.SlugField(max_length=50,unique=True)
    description=models.TextField(max_length=500,blank=True)
    price=models.IntegerField()
    image=models.ImageField(upload_to='product',blank=True)
    stock=models.IntegerField()
    available=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    
    
    def get_url(self):
        return reverse('shop:procatdetail',args=[self.category.slug,self.slug])
    
    class Meta:
        ordering=['name']
        verbose_name='product'
        verbose_name_plural='products'
        
    def __str__(self):
        return  '{}'.format(self.name)
    
    
