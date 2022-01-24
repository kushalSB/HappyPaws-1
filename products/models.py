from django.db import models

from django.contrib import admin



# Create your models here.
class Product(models.Model):
    title       = models.CharField(max_length=100)
    description = models.TextField()
    price       = models.FloatField()
    image       = models.ImageField(null=True, blank=True)
    
    def __str__(self):
        return self.title

    @property
    def imageurl(self):
        try:
            url =self.image.url
        except:
            url = ''
        return url

class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'price')
admin.site.register(Product, ProductAdmin)