from django.db import models

class BlogPost(models.Model):
  title = models.CharField(max_length=255)
  content = models.CharField(max_length=255)
  pub_date = models.DateField(null=True, default='')
  auther = models.CharField(max_length=50)

class Product(models.Model):
  name = models.CharField(max_length=50)
  description = models.CharField(max_length=100)
  price = models.IntegerField(null=True, default='')




  def __str__(self):
    return f"{self.title} {self.content}"