from src.utils import textos, medidas
from src.components import table
from PyQt5.QtWidgets import (QFileDialog, QPushButton, QDialog, QDialogButtonBox, QFormLayout, QGroupBox, QLabel, QLineEdit, QComboBox, QVBoxLayout)
import json
import sys
from PyQt5.QtGui import *

class DialogoFormSpatialReference(QDialog):

    def __init__(self, parent):

        super(DialogoFormSpatialReference, self).__init__(parent)

        # Comunicador
        self.comunicador = []

        # Pai
        self.pai = parent

        # Título da Janela
        self.titulo = textos.JANELA_REFERENCIA_ESPACIAL
        # Geometria da Janela
        self.topo = medidas.topo
        self.esquerda = medidas.esquerda
        self.largura = medidas.dialogo_largura
        self.altura = medidas.dialogo_altura

        # Formulário
        self.le_projecao = QComboBox()
        self.le_zone = QLineEdit()      
        self.le_elipsoide = QComboBox()
        self.le_datum = QComboBox()
        self.le_unidade = QComboBox()

        # Adicionar as Opcoes para o Formulario 
            #Projeção
        self.le_projecao.addItem("UTM")
            #Elipsoide
        self.le_elipsoide.addItem("WGS84")
            #Datum
        self.le_datum.addItem("SAD69")
        self.le_datum.addItem("WGS84")
        self.le_datum.addItem("SIRGAS2000")
            #Unidade
        self.le_unidade.addItem("Metros")
        self.le_unidade.addItem("Quilômetros")


        #
        self.IniciarDialogoFormNovoProjeto()

    """
        Métodos
    """
    def IniciarDialogoFormNovoProjeto(self):

        # Entradas
        self.form_novo_projeto_gb = QGroupBox("Parâmetros de Orientação Interior")
        layout_form = QFormLayout()
        layout_form.addRow(QLabel(textos.PROJECAO), self.le_projecao)
        layout_form.addRow(QLabel(textos.ZONA), self.le_zone)
        layout_form.addRow(QLabel(textos.ELIPSOIDE), self.le_elipsoide)
        layout_form.addRow(QLabel(textos.DATUM), self.le_datum)
        layout_form.addRow(QLabel(textos.UNIDADE), self.le_unidade)


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

            self.le_projecao.currentText(),        
            self.le_zone.text(),
            self.le_elipsoide.currentText(),
            self.le_datum.currentText(),
            self.le_unidade.currentText()

        ]
        self.CriarJson(self.comunicador)
 
    def CriarJson(self, comunicador):
        
        data = {
                "Projeção":comunicador[0],
                "Zona":comunicador[1],
                "Elipsoide":comunicador[2],
                "Datum":comunicador[3],
                "Unidade":comunicador[4]
            }
        
        with open("settings.json") as config:
            setting = json.load(config)

        from jsonmerge import merge
        result = merge(setting, data)

        with open("settings.json", "w") as write_file:
            json.dump(result, write_file)
        
        self.close()


