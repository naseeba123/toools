from django.db import models

class tools(models.Model):
	na=models.CharField(max_length=100)
	em=models.CharField(max_length=100)
	pd=models.CharField(max_length=100)
	usertype=models.CharField(max_length=100)
	status=models.CharField(max_length=100)




class product(models.Model):
	pname=models.CharField(max_length=100)
	price=models.CharField(max_length=100)
	t=models.ImageField(upload_to='images')
# Create your models here.
