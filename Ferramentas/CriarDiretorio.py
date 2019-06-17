import os

def criar_diretorios(caminho):
    os.mkdir(caminho + "/Json")
    os.mkdir(caminho + "/Data")
    os.mkdir(caminho + "/Relatorios")
    os.mkdir(caminho + "/Imagens")
    os.mkdir(caminho + "/Shapefiles")