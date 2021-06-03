from django.db import models

# Create your models here.




class Item(models.Model):
    def __str__(self):
        return self.itemName

    itemName= models.CharField(max_length=200)
    itemDescription= models.CharField(max_length=1000)
    itemPrice= models.IntegerField()
    itemImage= models.CharField(max_length=500, default="https://cdn.dribbble.com/users/1012566/screenshots/4187820/topic-2.jpg")
    

