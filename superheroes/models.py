from django.db import models

# Create your models here.
class SuperHeroe(models.Model)
    # Propiedades
    id = models.BigAutoField(primary_key=True) # ID automática, aumenta 1 en cada superhéroe introducido
    name = models.CharField(max_length=60)
    alias = models.CharField(max_length=60)

    # Métodos mágicoss
    def __str__(self):
        return self.name