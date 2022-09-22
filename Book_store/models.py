from django.db import models

# Create your models here.

class Book_store(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    quantity = models.FloatField()
    price = models.FloatField()
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def get_total_price(self):
        return self.quantity * self.price

    class Meta:
        db_table = 'Book_store'