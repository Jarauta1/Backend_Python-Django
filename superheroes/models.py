from django.db import models

# Create your models here.
class SuperHeroe(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=60)
    alias = models.CharField(max_length=60)

    def __str__(self):
        return self.name