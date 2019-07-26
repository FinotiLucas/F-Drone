import numpy as np
#importamos a pandas como pd
import pandas as pd

import math, json, os

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

def Criar_Arquivo_Coordenadas():
    
    with open("../settings.json") as setting:
        path = json.load(setting)        

    exists = os.path.isfile(path["Path"] + "/Json/Coordinates.json")
    
    if exists:
        with open(path["Path"] + "/Json/Coordinates.json") as coords:
            data_json = json.load(coords)
        nome = np.array(data_json['Nome'].split(","))
        tipo = np.array(data_json['Tipo'].split(",")) 
        x = np.array(data_json['X'].split(",")).astype(np.float)      
        y = np.array(data_json['Y'].split(",")).astype(np.float)  
        z = np.array(data_json['Z'].split(",")).astype(np.float)  
        X = np.array(data_json['Este'].split(",")).astype(np.float)  
        Y = np.array(data_json['Norte'].split(",") ).astype(np.float)  
        Z = np.array(data_json['Altitude'].split(",")).astype(np.float)  
        
        data = np.empty((len(x), 6),  dtype='O')
        
        for i in range(len(x)):

            data[i][0] = nome[i]
            data[i][1] = x[i]
            data[i][2] = y[i]
            data[i][3] = X[i]
            data[i][4] = Y[i]
            data[i][5] = Z[i]
            
        data = pd.DataFrame(data)

    data.to_csv('resect.txt', sep=' ', header=False, float_format='%.2f', index=False)

def Criar_Arquivo_Pontos():
    
    with open("settings.json") as setting:
        path = json.load(setting)        

    exists1 = os.path.isfile(path["Path"] + "/Json/Coordinates.json")
    exists2 = os.path.isfile(path["Path"] + "/Json/InteriorOrientationData.json")
    
    if exists1 and exists2:
        with open(path["Path"] + "/Json/Coordinates.json") as coords:
            data_json = json.load(coords)
        with open(path["Path"] + "/Json/InteriorOrientationData.json") as cam:
            data_json_2 = json.load(cam)
            
        nome = np.array(data_json['Nome'].split(","))
        tipo = np.array(data_json['Tipo'].split(",")) 
        x = np.array(data_json['X'].split(",")).astype(np.float)      
        y = np.array(data_json['Y'].split(",")).astype(np.float)  
        X = np.array(data_json['Este'].split(",")).astype(np.float)  
        Y = np.array(data_json['Norte'].split(",") ).astype(np.float)  
        Z = np.array(data_json['Altitude'].split(",")).astype(np.float)  
        x0 = np.array(data_json_2['x0'].split(",")).astype(np.float)
        y0 = np.array(data_json_2['y0'].split(",")).astype(np.float)
        f0 = np.array(data_json_2['f'].split(",")).astype(np.float)
        
        
        data = np.empty((len(x), 6),  dtype='O')
        
        for i in range(len(x)):

            data[i][0] = nome[i]
            data[i][1] = x[i]
            data[i][2] = y[i]
            data[i][3] = X[i]
            data[i][4] = Y[i]
            data[i][5] = Z[i]
            
        data = pd.DataFrame(data)

        data.to_csv(path['Path'] + '/Data/resect.txt', sep=' ', header=False, float_format='%.2f', index=False)


def Criar_Arquivo_Camera():
    
    with open("settings.json") as setting:
        path = json.load(setting)        

    exists1 = os.path.isfile(path["Path"] + "/Json/Coordinates.json")
    exists2 = os.path.isfile(path["Path"] + "/Json/InteriorOrientationData.json")
    
    if exists1 and exists2:
        with open(path["Path"] + "/Json/InteriorOrientationData.json") as coords:
            data_json = json.load(coords)
        with open(path["Path"] + "/Json/SpaceResection.json") as cam:
            data_json_2 = json.load(cam)
            
        Omega = 0
        Phi = 0
        Kappa = 0 
        X = np.array([data_json_2['X Estimado']]).astype(np.float)
        Y = np.array([data_json_2['Y Estimado']]).astype(np.float)
        Z = np.array([data_json_2['Z Estimado']]).astype(np.float)
        x0 = np.array(data_json['x0'].split(",")).astype(np.float)
        y0 = np.array(data_json['y0'].split(",")).astype(np.float)
        f = np.array(data_json['f'].split(",")).astype(np.float)
        
        
        data = np.empty((1, 9),  dtype='O')

        data[0][0] = 0
        data[0][1] = 0
        data[0][2] = 0
        data[0][3] = X[0]
        data[0][4] = Y[0]
        data[0][5] = Z[0]
        data[0][6] = x0[0]
        data[0][7] = y0[0]
        data[0][8] = f[0]
            
        data = pd.DataFrame(data)

        data.to_csv(path['Path'] + '/Data/cam.txt', sep=' ', header=False, float_format='%.2f', index=False)
