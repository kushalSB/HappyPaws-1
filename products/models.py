from django.db import models

from django.contrib import admin

<<<<<<< HEAD


# Create your models here.
class Product(models.Model):
    title       = models.CharField(max_length=100)
    description = models.TextField()
    price       = models.FloatField()
    image       = models.ImageField(null=True, blank=True)
    
    def __str__(self):
        return self.title
=======
# Create your models here.
class Category(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    name = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    Categorie = (
        ("New Arrivals", "New Arrivals"),
        ("Pets", "Pets"),
        ("Pet Accessories", "Pet Accessories"),
        ("Pet food", "Pet food"),
        ("Aquariums", "Aquariums")
    )
    id = models.AutoField(auto_created=True, primary_key=True)
    title = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    choice = models.CharField(
        max_length=300, null=True, blank=True, choices=Categorie)

    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null= True, blank=True )
    buy_count = models.IntegerField(default=0, null=True, blank=True)

 

    # def __str__(self):
    #     return self.title
>>>>>>> frontend

    @property
    def imageurl(self):
        try:
<<<<<<< HEAD
            url =self.image.url
=======
            url = self.image.url
>>>>>>> frontend
        except:
            url = ''
        return url

<<<<<<< HEAD
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'price')
=======



class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'price', 'category', 'buy_count')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id' , 'name',)

admin.site.register(Category, CategoryAdmin)
>>>>>>> frontend
admin.site.register(Product, ProductAdmin)