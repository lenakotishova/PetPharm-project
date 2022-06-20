from django.db import models


class Medicines(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=200)
    updated_at = models.DateTimeField(auto_now=True)
    is_InStock = models.BooleanField()
    pharmacy_id = models.IntegerField()
    amount_in_stock = models.IntegerField()
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')

