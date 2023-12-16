from django.db import models
from musician.models import musician_model
# Create your models here.
class album_model(models.Model):
    album_Name = models.CharField(max_length=100)
    musician = models.ForeignKey(musician_model, on_delete=models.CASCADE)
    album_release_data = models.DateField(auto_now_add=True)

    RATING_CHOICES = [
        ('1', '1 Star'),
        ('2', '2 Stars'),
        ('3', '3 Stars'),
        ('4', '4 Stars'),
        ('5', '5 Stars'),
    ]
    Rating = models.CharField(max_length=1,choices=RATING_CHOICES,default='1',)

    def __str__(self):
        return self.album_Name
