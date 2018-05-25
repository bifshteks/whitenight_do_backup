from django.db import models
from django.shortcuts import reverse

class Item(models.Model):
    title = models.CharField(max_length=255)
    size = models.CharField(max_length=255)
    weight = models.DecimalField(max_digits=10, decimal_places=2)
    material = models.CharField(max_length=1000)
    price = models.IntegerField()
    img1 = models.FileField(upload_to='', default='')
    img2 = models.FileField(upload_to='', blank=True, null=True)
    img3 = models.FileField(upload_to='', blank=True, null=True)
    img4 = models.FileField(upload_to='', blank=True, null=True)
    description = models.TextField() 

    class Meta():
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return '/catalog/%i/' % self.id

    def get_chet(self):
        return False if self.id % 2 == 0 else True

class Bid(models.Model):
	name = models.CharField(max_length=255)
	phone = models.CharField(max_length=20)
	date = models.CharField(max_length=100)
	time_from = models.CharField(max_length=100)
	time_to = models.CharField(max_length=100)
	details = models.TextField()
	item_name = models.CharField(max_length=255)

	class Meta():
		verbose_name = 'Заказ'
		verbose_name_plural = 'Заказы'

class Callback(models.Model):
	name = models.CharField(max_length=255)
	phone = models.CharField(max_length=20)
	date = models.CharField(max_length=100)
	time_from = models.CharField(max_length=100)
	time_to = models.CharField(max_length=100)
	
	class Meta():
		verbose_name = 'Заказ звонка'
		verbose_name_plural = 'Заказы звонков'

