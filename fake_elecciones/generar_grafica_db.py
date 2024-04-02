import pandas as pd
import matplotlib.pyplot as plt
import base64
from io import BytesIO

def generar_grafica(votaciones_list):
    df = pd.DataFrame(list(votaciones_list.values('anio', 'partido', 'votos')))

    votos_por_partido = df.groupby(['partido'])['votos'].sum()

    etiquetas = ['{}: {} votos'.format(partido, votos) for partido, votos in votos_por_partido.items()]

    colores_partidos = {'PSOE': 'red',
                        'PP': 'cyan',
                        'VOX': 'green',
                        'SUMAR': 'violet'}

    plt.figure(figsize=(8, 6))
    plt.pie(votos_por_partido, labels=etiquetas, autopct='%1.1f%%', startangle=140,
            colors = [colores_partidos[partido] for partido in votos_por_partido.index])
    plt.title('Distribución de Votos por Partido en las Elecciones de {}'.format(df.iloc[0]['anio']))
    plt.axis('equal')

    plt.tight_layout()

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()

    graphic = base64.b64encode(image_png)
    graphic = graphic.decode('utf-8')

    return graphic
