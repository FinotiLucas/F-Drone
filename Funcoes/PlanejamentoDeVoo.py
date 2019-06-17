import numpy as np
import json,math

def PlanejamentodeVoo(caminho_json):

    with open(caminho_json) as PV:
        data = json.load(PV)

    area = data['Comprimento Longetudinal'] * data['Comprimento Transversal']

    escala_de_voo = data['Distancia Focal'] / data['Altura de Voo']

    gsd_image =  escala_de_voo * data['GSD']

    gl = data['Numero de Pixels Longetudinais'] * gsd_image

    gt = data['Numero de Pixels Transversais'] * gsd_image

    GL = data['Numero de Pixels Longetudinais'] * data['GSD']

    GT = data['Numero de Pixels Transversais'] * data['GSD']

    b = (gl-(data['Sobreposicao Longetudinal']/100)*gl)

    B = (GL-((data['Sobreposicao Longetudinal']/100)*GL))

    avanco_da_base = data['Sobreposicao Longetudinal']/100

    w = (gt-((data['Sobreposicao Lateral']/100)*gt))

    W = (GT-((data['Sobreposicao Lateral']/100)*GT))

    area_do_modelo_esteroscopico = (GL - B) * GT

    area_incremental_de_cada_modelo_esteroscopico = B * W

    numero_total_de_fotos_esteroscopia = int(area / area_incremental_de_cada_modelo_esteroscopico)

    intervalo_de_tempo_entre_as_exposicoes = B / data['Sobreposicao Lateral']

    numero_de_fotos_por_faixa = int(((data['Comprimento Longetudinal']/B))) + 5

    numero_de_faixas = int((data['Comprimento Transversal'] / W)) + 2

    W_Ajustado = data['Comprimento Transversal'] / numero_de_faixas

    numero_total_de_fotos = numero_de_fotos_por_faixa * numero_de_faixas

    distancia_percorrida_pela_aeronave = ((B * (numero_de_fotos_por_faixa -1) * numero_de_faixas) + (W_Ajustado * ( numero_de_faixas -1)))

    arrastamento_teorico = (data['Tempo de Exposicao'] / data['Sobreposicao Lateral'])

    tempo_de_voo = distancia_percorrida_pela_aeronave / data['Velocidade de Voo']

    duracao_da_bateria_necessaria = (tempo_de_voo * 100) / (data['Duracao da Bateria']* 60)

    AZ_V = (data['Azimute de Voo'] * math.pi) / 180
    AZ_T = (data['Azimute Transversal'] * math.pi )/ 180
    AZ_R = (data['Azimute de Voo'] *  math.pi / 180) - math.pi
    
    
    E = []
    N = []
    E.append(data['Este'])
    N.append(data['Norte']) 
       
    faixa_atual = 1
    for i in range(1, numero_total_de_fotos):

        azimute = 0
        d = 0
            
        if(i % numero_de_fotos_por_faixa == 0):
            faixa_atual += 1
            azimute = AZ_T
            d = W_Ajustado
        
        else:
            d = B
            
            if(faixa_atual % 2 != 0):
                azimute = AZ_V
            
            else:
                azimute = AZ_R
        
        
        E.append( E[i-1] + math.sin(azimute) * d)
        N.append( N[i-1] + math.cos(azimute) * d)
        
    json_coordenadas_E = json.dumps(E)
    json_coordenadas_N = json.dumps(N)

    parametros = {
           
        "Área": area,
        "Escala de voo": escala_de_voo,
        "gsd": gsd_image,
        "gl": gl,
        "gt": gt,
        "GL": GL,
        "GT": GT,
        "b": b,
        "B": B,
        "Avanço da Base": avanco_da_base,
        "w": w,
        "W": W,
        "Área do modelo Esteroscopico": area_do_modelo_esteroscopico,
        "Área incremental de cada modelo Esteroscopico": area_incremental_de_cada_modelo_esteroscopico,
        "Número total de fotos em esteroscopia": numero_total_de_fotos_esteroscopia,
        "Intervalo de eempo entre as exposições": intervalo_de_tempo_entre_as_exposicoes,
        "Número de fotos por faixa": numero_de_fotos_por_faixa,
        "Número de Faixas": numero_de_faixas,
        "W Ajustado": W_Ajustado,
        "Número Total de Fotos": numero_total_de_fotos,
        "Distância total percorrida pela aeronave": distancia_percorrida_pela_aeronave,
        "Arrastamento Teorico": arrastamento_teorico,
        "Tempo total de Voo": tempo_de_voo,
        "Duração necessaria da Bateria": duracao_da_bateria_necessaria,
        "Coordenadas Este": json_coordenadas_E,
        "Coordenadas Norte": json_coordenadas_N
            
    }

    with open("settings.json") as setting:
        path = json.load(setting)

    from jsonmerge import merge
    result = merge(data, parametros)

    with open(path["Path"] + "/Json/FlightPlanning.json", "w") as write_file:
        json.dump(result, write_file)
