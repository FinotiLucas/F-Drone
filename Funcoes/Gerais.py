import numpy as np
#importamos a pandas como pd
import pandas as pd

import math

def sex_para_rad(angulo):

    """
        Função responsável por converter ângulos no sistema sexagesimal
        para radianos.
    """



    partes = angulo.split('°')
    angulo_grau = partes[0]         # armazena grau
    partes = partes[1].split("\'")
    angulo_minuto = partes[0]       # armazena minuto
    partes = partes[1].split('\"')
    angulo_segundo = partes[0]      # armazena segundo

    angulo_decimal = float(angulo_grau) + float(angulo_minuto)/60 + float(angulo_segundo)/3600      # convertendo para decimal
    angulo_radiano = math.radians(angulo_decimal)

    return angulo_radiano
