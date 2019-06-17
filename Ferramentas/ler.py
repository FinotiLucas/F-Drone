import numpy as np
import pandas as pd
import math


def ler_xlsx(caminho, pagina):

    """
        Função responsável por ler uma tabela de entrada de dados padronizada.
    """

    xlsx = pd.ExcelFile(caminho)    # Armazena a referência ao arquivo xml na variável xlsx
    df = pd.read_excel(xlsx, pagina)   # Armazena a referência da página do arquivo xlsx

    # Formatando informações para processamento
    # Exterior Orientation data

    col = df['c'].values

    lin = df['l'].values

    data = [col, lin]

    return data


def ler_txt(caminho):
    f = open(caminho,'r')
    texto = f.readlines()

    x = 0

    while x < len(texto):
        if texto[x] == "\n":
            local = texto.index(texto[x])
            texto.pop(local)
        else:
            texto[x] = texto[x].split(',')
            x += 1

    # Esse for abaixo aqui é só para tirar o "\n" em algumas strings, é opcional.

    for i in texto:
        local = texto.index(i) # Local do i em texto
        for b in i:
            local2 = texto[local].index(b) # Local2 do b em i ( local )
            if "\n" in b:
                texto[local][local2] = b.replace("\n",'') # Substitui o valor de acordo com "local" e "local2"

    lista = np.array(np.float_(texto))    
      
    return lista.transpose()

