from django.db import models


# Create your models here.
class Jewellery(models.Model):
	
	img=models.ImageField(max_length=500)
	id1=models.IntegerField()
	name=models.CharField(max_length=20)


	def __str__(self):
		return self.name


class color(models.Model):
	jewellery = models.ForeignKey(Jewellery, on_delete=models.CASCADE)
	color_name=models.CharField(max_length=20)
	color_hex=models.CharField(max_length=20)

	def __str__(self):
		return self.color_name


class dress(models.Model):
	picture = models.ImageField(upload_to = 'pictures')

	class Meta:
		db_table = "dress"