from Ferramentas import ler, textos, medidas
from SubJanelas import Tabela
from PyQt5.QtWidgets import (QFileDialog, QPushButton, QDialog, QDialogButtonBox, QFormLayout, QGroupBox, QLabel, QLineEdit, QComboBox, QVBoxLayout)
import json

class DialogoFormGerarRelatorio(QDialog):

    def __init__(self, parent):

        super(DialogoFormGerarRelatorio, self).__init__(parent)

        # Comunicador
        self.comunicador = []

        # Pai
        self.pai = parent

        # Título da Janela
        self.titulo = textos.JANELA_NOVO_PROJETO
        # Geometria da Janela
        self.topo = medidas.topo
        self.esquerda = medidas.esquerda
        self.largura = medidas.dialogo_largura
        self.altura = medidas.dialogo_altura

        # Pasta Projeto
        self.pb_pasta_projeto = QPushButton("Criar/Escolher pasta de destino do Relatório", self)
        self.pb_pasta_projeto.clicked.connect(self.PastaProjeto)
        self.le_pasta_projeto = QLineEdit()


        self.IniciarDialogoFormGerarRelatorio()

    """
        Métodos
    """
    def IniciarDialogoFormGerarRelatorio(self):

        # Caminho Projeto
        self.pasta_novo_projeto_gb = QGroupBox("Pasta do Projeto")
        layout_pasta = QVBoxLayout()
        layout_pasta.addWidget(self.pb_pasta_projeto)
        layout_pasta.addWidget(self.le_pasta_projeto)
        self.pasta_novo_projeto_gb.setLayout(layout_pasta)

        # Entradas

        self.form_novo_projeto_gb.setLayout(layout_form)

        # Botões
        self.caixa_de_botoes = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.caixa_de_botoes.accepted.connect(self.ok)
        self.caixa_de_botoes.rejected.connect(self.cancelar)

        # Definindo Layout
        self.layout_principal = QVBoxLayout()
        self.layout_principal.addWidget(self.pasta_novo_projeto_gb)
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
    def PastaProjeto(self):
        dialogo_pasta = QFileDialog()
        dialogo_pasta.setFileMode(QFileDialog.Directory)
        pasta = dialogo_pasta.getExistingDirectory()
        self.le_pasta_projeto.setText(pasta)


    def cancelar(self):
        self.close()

    def ok(self):
        self.comunicador = [

        ]
        Tabela.TabelaEntrada(self.pai, self.comunicador)
        self.close()