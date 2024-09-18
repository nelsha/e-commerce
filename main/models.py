import uuid
from django.db import models
from django.core.exceptions import ValidationError

def validate_rating(value):
    if value > 5.0:
        raise ValidationError('Rating cannot be more than 5.0')

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    stock = models.IntegerField()
    category = models.CharField(max_length=50)
    rating = models.DecimalField(max_digits=2, decimal_places=1, validators=[validate_rating])

    def __str__(self):
        return self.name

class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    is_happy = models.BooleanField()