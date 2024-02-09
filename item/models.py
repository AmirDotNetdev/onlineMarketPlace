from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)


    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name
        
class Item(models.Model):
    Category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length = 255)
    description = models.TextField(max_length = 255, blank = True, null = True)
    price = models.FloatField()
    image = models.ImageField(upload_to='item_image', blank=True, null=True)
    is_sold = models.BooleanField(default = False)
    created_by = models.ForeignKey(User, on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    