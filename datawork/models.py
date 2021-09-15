from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=400)
    isbn = models.IntegerField(null=True,unique=True)
    author = models.CharField(max_length=200)
    language = models.CharField(max_length=200)
    no_of_page = models.IntegerField()
    edition = models.IntegerField()
    rent_price = models.FloatField()
    
    
    def __str__(self):
        return self.title

class UserCode(models.Model):
    user_id = models.OneToOneField(User,on_delete=models.CASCADE)
    code = models.IntegerField()

    def __str__(self):
        return self.user_id.username

class Order(models.Model):
   ordered = models.BooleanField(default=False)
   user_id = models.ForeignKey(User,on_delete=models.CASCADE)

   def __str__(self):
       return self.ordered

class OrderItem(models.Model):
    order_id = models.ForeignKey(Order,on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    book_id = models.ForeignKey(Book,on_delete=models.CASCADE)
    qty = models.IntegerField()

    def  __Str__(self):
        return self.order_id

    
    
    
    
    
