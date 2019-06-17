from Ferramentas import ler, textos, medidas
from SubJanelas import Tabela
from PyQt5.QtWidgets import (QFileDialog, QPushButton, QDialog, QDialogButtonBox, QFormLayout, QGroupBox, QLabel, QLineEdit, QComboBox, QVBoxLayout)
import json, os
from Funcoes import IO
from jsonmerge import merge

class DialogoCoordenadas(QDialog):

    def __init__(self, parent):

        super(DialogoCoordenadas, self).__init__(parent)

        # Comunicador
        self.comunicador = []

        # Pai
        self.pai = parent

        # Título da Janela
        self.titulo = textos.JANELA_ORIENTACAO_INTERIOR
        # Geometria da Janela
        self.topo = medidas.topo
        self.esquerda = medidas.esquerda
        self.largura = medidas.dialogo_largura
        self.altura = medidas.dialogo_altura

        # Formulário
        self.le_X = QLineEdit()
        self.le_Y = QLineEdit()


        self.IniciarDialogoFormNovoProjeto()

    """
        Métodos
    """
    def IniciarDialogoFormNovoProjeto(self):

        # Entradas
        self.form_novo_projeto_gb = QGroupBox("Coordenada dos pontos no terreno")
        layout_form = QFormLayout()
        layout_form.addRow(QLabel(textos.X_TERRENO), self.le_X)
        layout_form.addRow(QLabel(textos.Y_TERRENO), self.le_Y)


        self.form_novo_projeto_gb.setLayout(layout_form)

        # Botões
        self.caixa_de_botoes = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.caixa_de_botoes.accepted.connect(self.ok)
        self.caixa_de_botoes.rejected.connect(self.cancelar)
        self.accepted.connect(lambda: self.IO(self.column, self.row, self.width, self.height))

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
        
        self.x = IO.coordenas_imagemMM("Json/InteriorOrientationData.json", self.width, self.height, self.column, self.row)

        self.comunicador = [
            self.x[0],
            self.x[1],
            self.x[2],
            float(self.le_X.text()),        
            float(self.le_Y.text()),
        ]
        self.CriarJson(self.comunicador)


    def IO(self, column, row, width, height):
        
        self.column = column
        self.row = row
        self.width = width
        self.height = height
        
         
    def CriarJson(self, comunicador):
        

        exists = os.path.isfile("Json/Coords.json")
        
        if exists:
            
            with open("Json/Coords.json") as IO:
                data = json.load(IO)
                
            data['X'] = str(data['X']) + str(",") + str(comunicador[0])
            data['Y'] = str(data['Y']) + str(",") +  str(comunicador[1])
            data['Z'] = str(data['Z']) + str(",") +  str(comunicador[2])
            data['Este'] = str(data['Este']) + str(",") +  str(comunicador[3])
            data['Norte'] =  str(data['Norte']) + str(",") +  str(comunicador[4])
            
            with open("Json/Coords.json", "w+") as write_file:
                json.dump(data, write_file)
        
        else:
            
            data1 = {
                "X":comunicador[0],
                "Y":comunicador[1],
                "Z":comunicador[2],
                "Este":comunicador[3],
                "Norte":comunicador[4]
            }
            with open("Json/Coords.json", "w") as write_file:
                json.dump(data1, write_file)
        
        
        self.close()

