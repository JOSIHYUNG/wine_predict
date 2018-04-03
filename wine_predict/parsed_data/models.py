from django.db import models

# Create your models here.
class WineData(models.Model):
	name=models.CharField('name',primary_key=True,max_length=150)
	rating=models.IntegerField('rating')
	region=models.CharField('region',max_length=20)
	price=models.IntegerField('price')

	def __str__(self):
		return self.name