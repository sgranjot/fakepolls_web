from django.db import models
from django.core.exceptions import ValidationError
import os

class Votacion (models.Model):
    anio = models.CharField(max_length=4)
    partido = models.CharField(max_length=20)
    votos = models.IntegerField()

    def __str__(self):
        return 'Año '+ self.anio + ', ' + self.partido + ': ' + self.votos + ' votos.'


def validate_csv_file_extension(value):
    ext = os.path.splitext(value.name)[1]  # Obtiene la extensión del archivo
    if ext.lower() != '.csv':
        raise ValidationError('El archivo debe ser un archivo CSV.')

class CSVFile(models.Model):
    file = models.FileField(upload_to='uploads/', validators=[validate_csv_file_extension])