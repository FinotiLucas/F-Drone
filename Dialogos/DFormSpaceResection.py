from Ferramentas import ler, textos, medidas
from SubJanelas import Tabela
from PyQt5.QtWidgets import (QFileDialog, QPushButton, QDialog, QDialogButtonBox, QFormLayout, QGroupBox, QLabel, QLineEdit, QComboBox, QVBoxLayout)
import json, os, sys
import numpy as np
#from Funcoes import Resseccao
from scipy.optimize import leastsq

class DialogoSpaceResection(QDialog):

    def __init__(self, parent):

        super(DialogoSpaceResection, self).__init__(parent)

        # Comunicador
        self.comunicador = []

        # Pai
        self.pai = parent

        # Título da Janela
        self.titulo = textos.JANELA_RECSSAO_ESPACIAL
        # Geometria da Janela
        self.topo = medidas.topo
        self.esquerda = medidas.esquerda
        self.largura = medidas.dialogo_largura
        self.altura = medidas.dialogo_altura

        # Formulário

        self.le_X = QLineEdit()
        self.le_Y = QLineEdit()
        self.le_Z = QLineEdit()      
        
        self.IniciarDialogoFormNovoProjeto()

    """
        Métodos
    """
    def IniciarDialogoFormNovoProjeto(self):

        # Entradas
        self.form_novo_projeto_gb = QGroupBox("Resseção Espacial")
        layout_form = QFormLayout()
        layout_form.addRow(QLabel(textos.X_RESSECTION), self.le_X)
        layout_form.addRow(QLabel(textos.Y_RESSECTION), self.le_Y)
        layout_form.addRow(QLabel(textos.Z_RESSECTION), self.le_Z)


        self.form_novo_projeto_gb.setLayout(layout_form)

        # Botões
        self.caixa_de_botoes = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.caixa_de_botoes.accepted.connect(self.ok)
        self.caixa_de_botoes.rejected.connect(self.cancelar)

        # Definindo Layout
        self.layout_principal = QVBoxLayout()
        self.layout_principal.addWidget(self.form_novo_projeto_gb)
        self.layout_principal.addWidget(self.caixa_de_botoes)
        self.setLayout(self.layout_principal)

        # Titulo da Janela
        self.setWindowTitle(self.titulo)
        # Geometria da Janela
        self.setGeometry(self.topo, self.esquerda, self.largura, self.altura)
        # Exibindo
        self.show()

    """
        Eventos
    """
    def cancelar(self):
        self.close()

    def ok(self):
        self.comunicador = [
            self.le_X.text(),        
            self.le_Y.text(),
            self.le_Z.text(),
        ]
        self.CriarJson(self.comunicador)
        self.realizar_resseccao()
 
    def CriarJson(self, comunicador):
    
        with open("settings.json") as setting:
            path = json.load(setting)
     
        exists = os.path.isfile("settings.json")
        
        if exists:
                
            data = {
                    "X Estimado":comunicador[0],
                    "Y Estimado":comunicador[1],
                    "Z Estimado":comunicador[2],
                }
            
            with open(path['Path'] + "/Json/SpaceResection.json", "w") as write_file:
                json.dump(data, write_file)
        
        self.close()

    def realizar_resseccao(self):

        
        with open("settings.json") as setting:
            path = json.load(setting)

        OK = False
        exists = os.path.isfile("settings.json")
        exists_1 = os.path.isfile(path['Path'] + '/Data/cam.txt')
        exists_2 = os.path.isfile(path['Path'] + '/Data/resect.txt')
        if exists and exists_1 and exists_2 :
            if len(sys.argv) > 1:
                camera_file = sys.argv[1]
            else:
                camera_file = path['Path'] + '/Data/cam.txt'
            if len(sys.argv) > 2:
                point_file = sys.argv[2]
            else:
                point_file = path['Path'] + '/Data/resect.txt'
            OK = True
        else:
            from Funcoes import Gerais
            Gerais.Criar_Arquivo_Pontos()
            Gerais.Criar_Arquivo_Camera()
            point_file = path['Path'] + '/Data/resect.txt'
            camera_file = path['Path'] + '/Data/cam.txt'
            OK = True
            
        if OK == True:
            self.ini = Resseccao.CollinearityData(camera_file,point_file)
            
