import pandas as pd
import matplotlib.pyplot as plt
import base64
from io import BytesIO

def generar_grafica ():
    df = pd.read_csv('elecciones_generales_2023.csv')

    partidos_principales = ['PSOE', 'PP', 'VOX', 'SUMAR']

    colores_partidos = {'PSOE': 'red',
                        'PP': 'cyan',
                        'VOX': 'green',
                        'SUMAR': 'violet'}

    df_filtrado = df[df['PARTIDO'].isin(partidos_principales)]

    votos_por_partido = df_filtrado.groupby('PARTIDO')['NUM_VOTOS'].sum()

    plt.figure(figsize=(8, 6))
    plt.pie(votos_por_partido, labels=votos_por_partido.index, autopct='%1.1f%%', startangle=140,
            colors=[colores_partidos[partido] for partido in votos_por_partido.index])
    plt.title('Distribución de Votos por Partido en las Elecciones de 2023')
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
