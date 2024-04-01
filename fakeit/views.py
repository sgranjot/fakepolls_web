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

        pos = np.arange(10)+ 2

        fig = plt.figure(figsize=(8, 3))
        ax = fig.add_subplot(111)

        ax.barh(pos, np.arange(1, 11), align='center')
        ax.set_yticks(pos)
        ax.set_yticklabels(('#hcsm',
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
        ax.set_xticks([])
        ax.invert_yaxis()

        ax.set_xlabel('Popularity')
        ax.set_ylabel('Hashtags')
        ax.set_title('Hashtags')

        plt.tight_layout()

        buffer = BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        image_png = buffer.getvalue()
        buffer.close()

        graphic = base64.b64encode(image_png)
        graphic = graphic.decode('utf-8')
        print(graphic)
        return graphic
