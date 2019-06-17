from PyQt5 import QtGui
from PyQt5.QtGui import QIcon, QColor
from Ferramentas import ler, textos, medidas
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
        poligonal = ler.ler_xlsx(self.dados[1], "Poligonal")
    def ExibirTabela(self, dados):
        linhas = len(dados[0]) + 1
        self.table.tablewidget.setRowCount(linhas)
        self.table.tablewidget.setColumnCount(6)
        self.table.tablewidget.setItem(0, 0, QTableWidgetItem("Ré"))
        self.table.tablewidget.setItem(0, 1, QTableWidgetItem("Estação"))
        self.table.tablewidget.setItem(0, 2, QTableWidgetItem("Vante"))
        self.table.tablewidget.setItem(0, 3, QTableWidgetItem("Distância Inclinda"))
        self.table.tablewidget.setItem(0, 4, QTableWidgetItem("Ângulo Horizontal"))
        self.table.tablewidget.setItem(0, 5, QTableWidgetItem("Ângulo Horizontal (radianos)"))
        
        contador_linhas = 1
        for dado in dados[0]:
            self.table.tablewidget.setItem(contador_linhas, 0, QTableWidgetItem(dado))
            contador_linhas = contador_linhas + 1

        contador_linhas = 1
        for dado in dados[1]:
            self.table.tablewidget.setItem(contador_linhas, 1, QTableWidgetItem(dado))
            contador_linhas = contador_linhas + 1
            
        contador_linhas = 1
        for dado in dados[2]:
            self.table.tablewidget.setItem(contador_linhas, 2, QTableWidgetItem(dado))
            contador_linhas = contador_linhas + 1

        contador_linhas = 1
        for dado in dados[3]:
            self.table.tablewidget.setItem(contador_linhas, 3, QTableWidgetItem(str(dado)))
            contador_linhas = contador_linhas + 1

        contador_linhas = 1
        for dado in dados[4]:
            self.table.tablewidget.setItem(contador_linhas, 4, QTableWidgetItem(dado))
            contador_linhas = contador_linhas + 1

        contador_linhas = 1
        for dado in dados[5]:
            self.table.tablewidget.setItem(contador_linhas, 5, QTableWidgetItem(str(dado)))
            contador_linhas = contador_linhas + 1

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tabela)
        self.tabela.cellClicked.connect(self.CelulaClicada)

        self.acao_coordenada_conhecida = QAction(QIcon("icones/localizacao/svg/031-check-in.svg"), "Adicionar Coordenada Conhecida", self)
        self.acao_coordenada_conhecida.triggered.connect(self.AtivarCoordenadaConhecida)

        self.acao_exportar = QAction(QIcon(), "Exportar Poligonal para Análise", self)
        self.acao_exportar.triggered.connect(self.ExportarPoligonal)

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
