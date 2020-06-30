import numpy as np
import math

def Lb(X, Y):
    Lb1 = np.concatenate((X,Y), axis = None)
    Lb = np.matrix(Lb1)

    return Lb.transpose()


def pesos(tamanho, peso):
    """
        Função responsável imprimir as matrizes na tela
    """
    matriz = []
    lin = tamanho
    col = tamanho

    for i in range(lin):
        linha = []
        for j in range(col):
            if i == j:
                linha.append(1/math.pow(peso,2))
            else:
                linha.append(0)

        matriz.append(linha)

    matriz_pesos = np.matrix(matriz)
    return matriz_pesos


def matriz_A (X, Y):

    temp1 = []
    temp2 = []

    for i in range(len(X)):
        temp1.append([X[i], Y[i], 0, 0, 1, 0])
        temp2.append([0, 0, X[i], Y[i], 0, 1])

    X1 = np.array(temp1)
    Y1 = np.array(temp2)

    A1 = np.zeros((X1.shape[0]+len(X),X1.shape[1]))
    A1[:-len(X),:] = X1
    A1[len(X):, :] = Y1
    A = np.matrix(A1)

    return A

def X(A, tamanho, peso, Lb):

    P = pesos(tamanho, peso)
    L = np.dot(Lb, -1)
    aux0 = np.dot(A.transpose(),P)
    aux1 = np.dot(aux0,A)
    aux2 = np.dot(aux0, L)
    aux3 = np.dot(aux1.I, -1)

    X = np.dot(aux3,aux2)

    return X

def residuos(A, X, Lb):
    res = np.matrix(np.dot(A,X) - Lb)
    return res

def MCV_X(A, tamanho, peso):
    P = pesos(tamanho, peso)

    aux0 = np.dot(A.transpose(),P)
    aux1 = np.dot(aux0,A)
    MCV = np.dot(math.pow(peso,2),aux1.I)

    return MCV


def MCV_Lb(A, tamanho, peso):
    P = pesos(tamanho, peso)

    aux0 = np.dot(A.transpose(),P)
    aux1 = np.dot(aux0,A)
    N = aux1.I
    aux2 = np.dot(math.pow(peso, 2), A)
    aux3 = np.dot(aux2, N.I)
    aux4 = np.dot(aux3, A.transpose())
    MCV = np.matrix(aux4)

    return MCV

def MCV_res(A, tamanho, peso):
    P = pesos(tamanho, peso)

    aux0 = np.dot(A.transpose(),P)
    aux1 = np.dot(aux0,A)
    N = aux1
    aux2 = np.dot(A, N.I)
    aux3 = np.dot(aux2, A.transpose())
    aux4 = np.dot(P.I, -1)
    MCV = np.matrix(np.dot(math.pow(peso,2),aux3 - aux4))

    return MCV
