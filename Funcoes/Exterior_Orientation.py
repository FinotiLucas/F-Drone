#importamos a numpy como np
import numpy as np
#importamos a np como pd

def Matriz_M(w, phi, k):

    """
        Função responsável por calcular as matrizes de rotacão. em R(K) * R(PHI) * R(W)
    """

    #Criando a matriz de rotação R(w)
    M_w = np.matrix([[1,0,0],[0, np.cos(w), np.sin(w)],[0, -np.sin(w), np.cos(w)]])

    #Criando a matriz de rotação R(phi)
    M_phi = np.matrix([[np.cos(phi), 0, -np.sin(phi)],[0, 1, 0],[np.sin(phi), 0, np.cos(phi)]])

    #Criando a matriz de rotação R(k)
    M_kappa = np.matrix([[np.cos(k),np.sin(k),0],[-np.sin(k),np.cos(k),0],[0, 0, 1]])

    #Multiplicando as matrizes de rotacão R(w), R(phi e R(k), tem-se
    aux = np.dot(M_kappa,M_phi)
    M = np.dot(aux, M_w)
    return M

def Colinealidade(M,focallength):
    # https://www.researchgate.net/publication/267295628_AEROTRIANGULACAO_DE_AEROFOTOS_DIGITAIS_NO_SISTEMA_MONORESTITUIDOR
    # Falta importar os parâmetros (Pegada de dados pela interface gráfica)
    uvw = np.dot( M, np.matrix([[X-XL], [Y-YL], [Z-ZL]]))
    # xp = x - x0
    # yp = y - y0
    for i in range(len(M[0])):
        xp = - focallength * uvw[1,i] / uvw[3,i]
        yp = - focallength * uvw[2,i] / uvw[3,i]
        COL = np.matrix(xp, yp)
    
    return  COL