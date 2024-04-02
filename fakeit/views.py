from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from io import BytesIO
import base64
import matplotlib.pyplot as plt
import numpy as np
# Create your views here.
class IndexView(generic.ListView):
    template_name = "graphic.html"
    context_object_name = "graph"
    def get_queryset(self):

        pos = np.arange(10)+ 2                              #crea un array del 0 al 9 y despues le sunma dos a cada elemento [2,3,4,5,6,7,8,9,10,11]

        fig = plt.figure(figsize=(8, 3))                    #crea una figura de matplotlib (lienzo) de 8 x 3 pulgadas
        ax = fig.add_subplot(111)                           #definimos una gráfica

        ax.barh(pos, np.arange(1, 11), align='center')      #crea un grafico de barras horizontal con los valores del array pos y la altura a partir de un aray de numeros del uno al 11, las barras las posicionamos centradas con respecto a los valores del eje y
        ax.set_yticks(pos)                                  #establece las ubicaciones de las marcas (ticks) en el eje Y del gráfico de barras horizontal.
        ax.set_yticklabels(('#hcsm',                        #etiquetas en las marcas del eje y
            '#ukmedlibs',
            '#ImmunoChat',
            '#HCLDR',
            '#ICTD2015',
            '#hpmglobal',
            '#BRCA',
            '#BCSM',
            '#BTSM',
            '#OTalk',),
            fontsize=15)
        ax.set_xticks([])                                   # Al pasar una lista vacía como argumento a set_xticks(), se eliminan todas las marcas en el eje X del gráfico de barras horizontal
        ax.invert_yaxis()                                   # invierte los valores del eje y

        ax.set_xlabel('Popularity')
        ax.set_ylabel('Hashtags')
        ax.set_title('Hashtags')

        plt.tight_layout()                                  # ajusta automáticamente los parámetros del diseño para que el gráfico se ajuste mejor al área de la figura

        buffer = BytesIO()                                  # crea un objeto BytesIO que opera en datos en memoria en lugar de en archivos físicos en el disco. se utilizará para almacenar temporalmente los datos binarios de la imagen generada por Matplotlib antes de codificarla en base64 y pasarla a través de HTTP para ser mostrada en una página web.
        plt.savefig(buffer, format='png')             # guarda el gráfico actual de Matplotlib en formato PNG en el objeto BytesIO buffer.
        buffer.seek(0)                                      # establece la posición del "puntero de lectura/escritura" en el objeto BytesIO buffer al principio del flujo de datos.
        image_png = buffer.getvalue()                       # lee los datos binarios almacenados en el objeto BytesIO buffer y los asigna a la variable image_png.
        buffer.close()

        graphic = base64.b64encode(image_png)               # codifica los datos binarios de la imagen PNG almacenados en la variable image_png en base64 y los asigna a la variable graphic.
        graphic = graphic.decode('utf-8')                   # decodifica la cadena de bytes graphic utilizando el estándar de codificación UTF-8 y luego la asigna nuevamente a la variable graphic.
        print(graphic)
        return graphic
