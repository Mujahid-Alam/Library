from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=400)
    isbn = models.IntegerField(null=True)
    author = models.CharField(max_length=100)
    language = models.CharField(max_length=100)
    no_of_page = models.IntegerField()
    edition = models.IntegerField()
    rent_price = models.FloatField()
    
    
    def __str__(self):
        return self.title


class Order(models.Model):
   ordered = models.BooleanField(default=False)
   user_id = models.ForeignKey(User,on_delete=models.CASCADE)

class OrderItem(models.Model):
    order_id = models.ForeignKey(Order,on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    book_id = models.ForeignKey(Book,on_delete=models.CASCADE)
    qty = models.IntegerField()

    
    
    
    
    
