from Ferramentas import ler, textos, medidas
from SubJanelas import Tabela
from PyQt5.QtWidgets import (QFileDialog, QPushButton, QDialog, QDialogButtonBox, QFormLayout, QGroupBox, QLabel, QLineEdit, QComboBox, QVBoxLayout)
import json, os

class DialogoOrientacaoInterior(QDialog):

    def __init__(self, parent):

        super(DialogoOrientacaoInterior, self).__init__(parent)

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
        self.le_camera = QLineEdit()
        self.le_x0 = QLineEdit()
        self.le_y0 = QLineEdit()
        self.le_K1 = QLineEdit()
        self.le_K2 = QLineEdit()
        self.le_K3 = QLineEdit()      
        self.le_P1 = QLineEdit()
        self.le_P2 = QLineEdit()
        self.le_f = QLineEdit()
        self.le_sensor_width = QLineEdit()

        self.IniciarDialogoFormNovoProjeto()

    """
        Métodos
    """
    def IniciarDialogoFormNovoProjeto(self):

        # Entradas
        self.form_novo_projeto_gb = QGroupBox("Parâmetros de Orientação Interior")
        layout_form = QFormLayout()
        layout_form.addRow(QLabel(textos.CAMERA), self.le_camera)
        layout_form.addRow(QLabel(textos.X0), self.le_x0)
        layout_form.addRow(QLabel(textos.Y0), self.le_y0)
        layout_form.addRow(QLabel(textos.K1), self.le_K1)
        layout_form.addRow(QLabel(textos.K2), self.le_K2)
        layout_form.addRow(QLabel(textos.K3), self.le_K3)
        layout_form.addRow(QLabel(textos.P1), self.le_P1)
        layout_form.addRow(QLabel(textos.P2), self.le_P2)
        layout_form.addRow(QLabel(textos.DISTANCIA_FOCAL), self.le_f)
        layout_form.addRow(QLabel(textos.SENSOR_WIDTH), self.le_sensor_width)

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
            self.le_camera.text(),        
            self.le_x0.text(),
            self.le_y0.text(),
            self.le_K1.text(),
            self.le_K2.text(),
            self.le_K3.text(),      
            self.le_P1.text(),
            self.le_P2.text(),
            self.le_f.text(),
            self.le_sensor_width.text(),
        ]
        self.CriarJson(self.comunicador)
 
    def CriarJson(self, comunicador):
    
        with open("settings.json") as setting:
            path = json.load(setting)
     
        exists = os.path.isfile("settings.json")
        
        if exists:
                
            data = {
                    "Camera":comunicador[0],
                    "x0":comunicador[1],
                    "y0":comunicador[2],
                    "K1":comunicador[3],
                    "K2":comunicador[4],
                    "K3":comunicador[5],
                    "P1":comunicador[6],
                    "P2":comunicador[7],
                    "f":comunicador[8],
                    "Tamanho do Sensor":comunicador[9]
                }
            
            with open(path['Path'] + "/Json/InteriorOrientationData.json", "w") as write_file:
                json.dump(data, write_file)
        
        self.close()


