import numpy as np
import json

def coordenas_imagemMM(caminho, width, height, column, row):

    with open(caminho) as IO:
        data = json.load(IO)
        
    x0 = float(data['x0'])
    y0 = float(data['y0'])
    K1 = float(data['K1'])
    K2 = float(data['K2'])
    K3 = float(data['K3'])
    P1 = float(data['P1'])
    P2 = float(data['P2'])
    f  = float(data['f'])
    sensor_width = float(data['Tamanho do Sensor'])

    pixel_size = sensor_width / width  # unit: mm/px

    x =  pixel_size * (column - ((width - 1) / 2))
    y = -pixel_size * (row - ((height - 1) / 2))

    x = x - x0
    y = y - y0

    r = np.sqrt(np.power( x , 2) + np.power( y,2))
    
    delta_x = (K1 * np.power(r,2) + K2 * np.power(r,4) + K3 * np.power(r,6)) * x + (P1 * (np.power(r,2) + 2 * np.power(x,2) + 2 * P2 * x * y))
    delta_y = (K1 * np.power(r,2) + K2 * np.power(r,4) + K3 * np.power(r,6)) * y + (P2 * (np.power(r,2) + 2 * np.power(y,2) + 2 * P1 * x * y))

    x = (x - delta_x)
    y = (y - delta_y)
    z = (-f)
        
    f = open("Dados/IOCoordinates.txt","a+")
    f.write("" + str(x) + "," + str(y) + "," + str(z) + "\n")
    f.close()
