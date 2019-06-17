from Ferramentas import ler, textos, medidas
from Funcoes import  PlanejamentoDeVoo
from SubJanelas import Tabela
from PyQt5.QtWidgets import (QFileDialog, QPushButton, QDialog, QDialogButtonBox, QFormLayout, QGroupBox, QLabel, QLineEdit, QComboBox, QVBoxLayout)
import json

class DialogoFormPlanejamentoDeVoo(QDialog):

    def __init__(self, parent):

        super(DialogoFormPlanejamentoDeVoo, self).__init__(parent)

        # Comunicador
        self.comunicador = []

        # Pai
        self.pai = parent

        # Título da Janela
        self.titulo = textos.JANELA_PLANEJAMENTO_DE_VOO
        # Geometria da Janela
        self.topo = medidas.topo
        self.esquerda = medidas.esquerda
        self.largura = medidas.dialogo_largura
        self.altura = medidas.dialogo_altura




        # Formulário
        self.le_nome = QLineEdit()
        #Informaçõoes sobre a area
        self.le_comprimento_longetudinal = QLineEdit()
        self.le_comprimento_transversal = QLineEdit()
        #Determinação da escala de Voo
        self.le_altura_de_voo = QLineEdit()
        self.le_distancia_focal = QLineEdit()
        #Sobrepoasição desejada
        self.le_sobreposicao_longetudinal = QLineEdit()
        self.le_sobreposicao_lateral = QLineEdit()
        #Sensor
        self.le_numero_de_pixels_longetudinais = QLineEdit()
        self.le_numero_de_pixels_transversais = QLineEdit()
        self.le_GSD = QLineEdit()
        #Arrastamento
        self.le_tempo_de_exposição = QLineEdit()
        self.le_velocidade_de_voo = QLineEdit()
        #Bateria
        self.le_duração_da_bateria = QLineEdit()
        #Direção de voo
        self.le_azimute_do_voo = QLineEdit()
        self.le_azimute_transversal = QLineEdit()
        #Coordenadas UTM da primeira imagem
        self.le_este = QLineEdit()
        self.le_norte = QLineEdit()


        self.IniciarDialogoFormPlanejamentoDeVoo()

    """
        Métodos
    """
    def IniciarDialogoFormPlanejamentoDeVoo(self):


        # Entradas
        self.form_novo_projeto_gb = QGroupBox("Dados inicias para o Planejamento de Voo ")
        layout_form = QFormLayout()
        layout_form.addRow(QLabel(textos.COMPRIMENTO_LONGETUDINAL), self.le_comprimento_longetudinal)
        layout_form.addRow(QLabel(textos.COMPRIMENTO_TRANSVERSAL), self.le_comprimento_transversal)
        layout_form.addRow(QLabel(textos.ALTURA_DE_VOO), self.le_altura_de_voo)
        layout_form.addRow(QLabel(textos.DISTANCIA_FOCAL), self.le_distancia_focal)
        layout_form.addRow(QLabel(textos.SOBREPOSICAO_LONGITUDINAL), self.le_sobreposicao_longetudinal)
        layout_form.addRow(QLabel(textos.SOBREPOSICAO_LATERAL), self.le_sobreposicao_lateral)
        layout_form.addRow(QLabel(textos.NUMERO_DE_PIXELS_LONGITUDINAIS), self.le_numero_de_pixels_longetudinais)
        layout_form.addRow(QLabel(textos.NUMERO_DE_PIXELS_TRANSVERSAIS), self.le_numero_de_pixels_transversais)
        layout_form.addRow(QLabel(textos.GSD_GROUND), self.le_GSD)
        layout_form.addRow(QLabel(textos.TEMPO_DE_EXPOSICAO), self.le_tempo_de_exposição)
        layout_form.addRow(QLabel(textos.VELOCIDADE_DE_VOO), self.le_velocidade_de_voo)
        layout_form.addRow(QLabel(textos.DURACAO_DA_BATERIA), self.le_duração_da_bateria)
        layout_form.addRow(QLabel(textos.AZIMUTE_DE_VOO), self.le_azimute_do_voo)
        layout_form.addRow(QLabel(textos.AZIMUTE_TRANSVERSAL), self.le_azimute_transversal)
        layout_form.addRow(QLabel(textos.ESTE_INICIAL), self.le_este)
        layout_form.addRow(QLabel(textos.NORTE_INICIAL), self.le_norte)


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
            self.le_comprimento_longetudinal.text(),
            self.le_comprimento_transversal.text(),
            self.le_altura_de_voo.text(),
            self.le_distancia_focal.text(),
            self.le_sobreposicao_longetudinal.text(),
            self.le_sobreposicao_lateral.text(),
            self.le_numero_de_pixels_longetudinais.text(),
            self.le_numero_de_pixels_transversais.text(),
            self.le_GSD.text(),
            self.le_tempo_de_exposição.text(),
            self.le_velocidade_de_voo.text(),
            self.le_duração_da_bateria.text(),
            self.le_azimute_do_voo.text(),
            self.le_azimute_transversal.text(),
            self.le_este.text(),
            self.le_norte.text(),
            
        ]
        self.CriarJson(self.comunicador)
 
    def CriarJson(self, comunicador):
        
        data = {
                "Comprimento Longetudinal":float(comunicador[0]),
                "Comprimento Transversal":float(comunicador[1]),
                "Altura de Voo":float(comunicador[2]),
                "Distancia Focal":float(comunicador[3]),
                "Sobreposicao Longetudinal":float(comunicador[4]),
                "Sobreposicao Lateral":float(comunicador[5]),
                "Numero de Pixels Longetudinais":float(comunicador[6]),
                "Numero de Pixels Transversais":float(comunicador[7]),
                "GSD":float(comunicador[8]),
                "Tempo de Exposicao":float(comunicador[9]),
                "Velocidade de Voo":float(comunicador[10]),
                "Duracao da Bateria":float(comunicador[11]),
                "Azimute de Voo":float(comunicador[12]),
                "Azimute Transversal":float(comunicador[13]),
                "Este":float(comunicador[14]),
                "Norte":float(comunicador[15]),
            }
        
        with open("Json/FlightPlanning.json", "w") as write_file:
            json.dump(data, write_file)
        
        PlanejamentoDeVoo.PlanejamentodeVoo("Json/FlightPlanning.json")
        
        self.close()
