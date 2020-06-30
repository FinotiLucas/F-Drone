from src.utils import textos, medidas
from src.components import table
from PyQt5.QtWidgets import (QFileDialog, QPushButton, QDialog, QDialogButtonBox, QFormLayout, QGroupBox, QLabel, QLineEdit, QComboBox, QVBoxLayout)
import json

class DialogoFormUTM(QDialog):

    def __init__(self, parent, ponto):

        super(DialogoFormUTM, self).__init__(parent)

        self.pai = parent

        self.ponto = ponto

        # Título da Janela
        self.titulo = textos.JANELA_NOVO_UTM
        # Geometria da Janela
        self.topo = medidas.topo
        self.esquerda = medidas.esquerda
        self.largura = medidas.dialogo_largura
        self.altura = medidas.dialogo_altura

        # Formulário
        self.le_utmx = QLineEdit()
        self.le_utmy = QLineEdit()

        self.IniciarDialogoFormUTM()

    """
        Métodos
    """
    def IniciarDialogoFormUTM(self):

        # Entradas
        self.form_utm_gb = QGroupBox("Coordenadas UTM")
        layout_form = QFormLayout()
        layout_form.addRow(QLabel("UTM-X"), self.le_utmx)
        layout_form.addRow(QLabel("UTM-Y"), self.le_utmy)
        self.form_utm_gb.setLayout(layout_form)

        # Botões
        self.caixa_de_botoes = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.caixa_de_botoes.accepted.connect(self.ok)
        self.caixa_de_botoes.rejected.connect(self.cancelar)

        # Definindo Layout
        self.layout_principal = QVBoxLayout()
        self.layout_principal.addWidget(self.form_utm_gb)
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
        self.pai.comunicador = [
            self.le_utmx.text(),
            self.le_utmy.text()
        ]
        self.pai.coordenadas_conhecidas.append([self.ponto, self.le_utmx.text(), self.le_utmy.text()])
        print(self.pai.coordenadas_conhecidas)
        self.close()
