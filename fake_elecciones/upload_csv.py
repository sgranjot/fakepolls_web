import pandas as pd
from django.shortcuts import render
from .models import Votacion

def upload(request):
    if request.method == 'POST' and request.FILES['archivo_csv']:
        df = pd.read_csv(request.FILES['archivo_csv'])

        votos_por_partido = df.groupby('PARTIDO')['NUM_VOTOS'].sum()

        for fila in votos_por_partido:
            obj = Votacion.objects.create(
                anio = fila['AÑO'],
                partido = fila['PARTIDO'],
                votos = fila['NUM_VOTOS']
            )
            obj.save()

        return render(request, 'importacion_exitosa.html')

    return render(request, 'importar_datos.html')
