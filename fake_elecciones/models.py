from django.db import models

class Votacion (models.Model):
    anio = models.CharField(max_length=4)
    partido = models.CharField(max_length=20)
    votos = models.IntegerField()

    def __str__(self):
        return 'Año '+ self.anio + ', ' + self.partido + ': ' + self.votos + ' votos.'

