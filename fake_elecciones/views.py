from django.shortcuts import render
from django.views import generic
import matplotlib.pyplot as plt
import pandas as pd

from .models import Votacion
from . import generar_grafica_csv, generar_grafica_db
from .forms import CSVForm


# sin persistencia, desde el .csv
class IndexViewCSV(generic.TemplateView):
    template_name ='fake_elecciones/resultados.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        graphic = generar_grafica_csv.generar_grafica()

        context['graph'] = graphic

        return context


#con persistencia en base de datos mysql
def upload_csv(request):
    if request.method == 'POST':
        form = CSVForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = form.save(commit=False)
            #csv_file.user = request.user  # Asignar el usuario actual al campo user
            csv_file.save()
            df = pd.read_csv(csv_file.file.path)
            #votos_por_partido = df.groupby(['AÑO', 'PARTIDO'])['NUM_VOTOS'].sum().reset_index()          ESTO ES PARA HACERLO CON TODOS LOS PARTIDOS, MEJOR CON LOS CUATRO PRINCIPALES




            partidos = ['PSOE', 'PP', 'VOX', 'SUMAR']



            df_filtrado = df[df['PARTIDO'].isin(partidos)]

            votos_por_partido = df_filtrado.groupby(['AÑO', 'PARTIDO'])['NUM_VOTOS'].sum().reset_index()




            for index, fila in votos_por_partido.iterrows():
                obj = Votacion.objects.create(
                    anio = fila['AÑO'],
                    partido = fila['PARTIDO'],
                    votos = fila['NUM_VOTOS']
                )
                obj.save()
            return render(request, 'fake_elecciones/importacion_exitosa.html')
    else:
        form = CSVForm()
    return render(request, 'fake_elecciones/upload_csv.html', {'form': form})


class CreateGraphic(generic.TemplateView):
    template_name = 'fake_elecciones/resultados.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        votaciones_list = Votacion.objects.all()

        graphic = generar_grafica_db.generar_grafica(votaciones_list)

        context['graph'] = graphic

        return context

