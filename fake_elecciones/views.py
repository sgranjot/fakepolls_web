from django.shortcuts import render
from django.views import generic
import matplotlib.pyplot as plt
import pandas as pd

from . import generar_grafica


# sin persistencia, desde el .csv
class IndexViewCSV(generic.TemplateView):
    template_name ='fake_elecciones/resultados.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        graphic = generar_grafica.genera_grafica()

        context['graph'] = graphic

        return context

#con persistencia en base de datos mysql
class IndexView(generic.TemplateView):
    template_name = 'fake_elecciones/resultados.html'

