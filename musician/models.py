from django.db import models

# Create your models here.
class musician_model(models.Model):
    first_Name = models.CharField(max_length=50)
    last_Name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phone_number = models.CharField(max_length=12)
    instrument_type = models.CharField(max_length=100)


    def __str__(self):
        return f"{self.first_Name} {self.last_Name}"
    