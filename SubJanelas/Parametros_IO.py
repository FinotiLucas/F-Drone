from PyQt5 import QtGui
from PyQt5.QtGui import QIcon, QColor
from ferramentas import ler, textos, medidas
from PyQt5.QtWidgets import (QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout, QAction)
from Dialogos import DFormUTM
import json

class TabelaEntrada(QWidget):

    def __init__(self, parent, dados):

        super(TabelaEntrada, self).__init__(parent)

        # Comunicador
        self.comunicador = []

        # Pai
        self.pai = parent

        # Título da Janela

        # Pegando os dados
        self.dados = dados

        # Iniciar Tabela
        self.IniciarTabelaEntrada()
        self.pai.setCentralWidget(self.tabela)

        # Ferramentas
        self.barra_ferramentas = parent.addToolBar("Editar Entrada")
        self.barra_ferramentas.addAction(self.acao_coordenada_conhecida)
        self.barra_ferramentas.addAction(self.acao_exportar)

        # Ferramentas ativas
        self.adicionar_coordenada = False

        # Edições
        self.coordenadas_conhecidas = []

    def IniciarTabelaEntrada(self):

        self.tabela = QTableWidget()
        dados = ler.ler_xlsx(self.dados[1], "Files")
        print(dados)
        self.tabela.setColumnCount(len(dados))
        self.tabela.setRowCount(len(dados[0])+1)

        self.tabela.setItem(0, 0, QTableWidgetItem("x0"))
        self.tabela.setItem(0, 1, QTableWidgetItem("y0"))
        self.tabela.setItem(0, 2, QTableWidgetItem("K1"))
        self.tabela.setItem(0, 3, QTableWidgetItem("K2"))
        self.tabela.setItem(0, 4, QTableWidgetItem("K3"))
        self.tabela.setItem(0, 5, QTableWidgetItem("P1"))
        self.tabela.setItem(0, 6, QTableWidgetItem("P2"))
        self.tabela.setItem(0, 7, QTableWidgetItem("f"))

        self.agentes_tabela = []

        contador_linhas = 1
        contador_colunas = 0
        for dado in dados:
            for item in dados:
                celula = QTableWidgetItem(str(item))
                if(contador_colunas == 1):
                    self.agentes_tabela.append(celula)
                self.tabela.setItem(contador_linhas, contador_colunas, QTableWidgetItem(celula))
                contador_linhas = contador_linhas + 1
            contador_linhas = 1
            contador_colunas = contador_colunas + 1

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tabela)
        self.tabela.cellClicked.connect(self.CelulaClicada)

        self.acao_coordenada_conhecida = QAction(QIcon("icones/localizacao/svg/031-check-in.svg"), "Adicionar Coordenada Conhecida", self)
        self.acao_coordenada_conhecida.triggered.connect(self.AtivarCoordenadaConhecida)

        self.acao_exportar = QAction(QIcon(), "Exportar dados para Análise", self)
        self.acao_exportar.triggered.connect(self.Exportardados)

    """
        Eventos
    """
    def CelulaClicada(self, linha, coluna):
        if(self.adicionar_coordenada and coluna == 1):
            self.tabela.item(linha, coluna).setBackground(QColor(100,100,150))
            DFormUTM.DialogoFormUTM(self, self.tabela.item(linha, coluna).text())

    def AtivarCoordenadaConhecida(self):
        if(self.adicionar_coordenada):
            self.adicionar_coordenada = False
        else:
            self.adicionar_coordenada = True

    def Exportardados(self):
        jsonstring = json.dumps(["Oi!", "Tudo BEM?", "sim! E vc ?"])
        print(jsonstring)
