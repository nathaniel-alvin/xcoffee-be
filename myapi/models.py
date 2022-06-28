from django.db import models

# Create your models here.
class Menu(models.Model):

    menu_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60)
    price = models.FloatField(max_length=60)

    def __str__(self):
        return self.name
