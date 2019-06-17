import sys
from Dialogos import DFormNovoProjeto, DFormUTM, DFormPlanejamentoDeVoo, DFormOrientacaoInterior, DFormSpatialReference
from Ferramentas import ler, textos, medidas
from PyQt5 import QtGui
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QTabWidget, QApplication, QMainWindow, QLabel, QMessageBox, QStatusBar, QAction, QMenu, QMenuBar, QFileDialog, QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout
from SubJanelas import ImageViewer
import json
import os
import sys

class FDrone(QMainWindow):

    """
        Construtor
    """
    def __init__(self, parent=None):

        super(FDrone, self).__init__(parent)

        # Comunicador
        self.comunicador = []

        # Statusbar
        self.statusbar = self.statusBar()

        # Título da Janela
        self.titulo = textos.FDrone
        # Incone do aplicativo
        self.setWindowIcon(QtGui.QIcon("icones/logo.svg"))

        """
            Definindo barra de ferramentas
        """
        self.toolbar = self.addToolBar("Ferramentas Teste")

        self.ferramenta_importar_imagem = QAction(QtGui.QIcon("icones/geral/svg/image-svgrepo-com.svg"), "Importar Imagem", self)
        self.ferramenta_importar_imagem.setShortcut("CTRL + I")
        self.ferramenta_importar_imagem.triggered.connect(self.AbrirImagem)
        self.toolbar.addAction(self.ferramenta_importar_imagem)

        ferramenta_visualizar_estatisticas = QAction(QtGui.QIcon("icones/geral/svg/pie-chart.svg"), "Visualizar Estatísticas", self)
        #ferramenta_visualizar_estatisticas.setShortcut("")
        #ferramenta_visualizar_estatisticas.triggered.connect()
        self.toolbar.addAction(ferramenta_visualizar_estatisticas)

        ferramenta_georeferrenciar = QAction(QtGui.QIcon("icones/geral/svg/maps-and-flags-map-svgrepo-com.svg"), "Georreferenciar Imagem", self)
        #ferramenta_georeferrenciar.setShortcut("")
        #ferramenta_georeferrenciar.triggered.connect()
        self.toolbar.addAction(ferramenta_georeferrenciar)

        ferramenta_gerar_ortofoto = QAction(QtGui.QIcon("icones/geral/svg/geography-map-svgrepo-com.svg"), "Gerar Ortofoto", self)
        #ferramenta_gerar_ortofoto.setShortcut("")
        #ferramenta_gerar_ortofoto.triggered.connect()
        self.toolbar.addAction(ferramenta_gerar_ortofoto)

        ferramenta_gerar_relatorio = QAction(QtGui.QIcon("icones/geral/svg/document-svgrepo-com.svg"), "Gerar Relatório", self)
        #ferramenta_gerar_relatorio.setShortcut("")
        #ferramenta_gerar_relatorio.triggered.connect()
        self.toolbar.addAction(ferramenta_gerar_relatorio)


        # Geometria da Janela
        self.topo = medidas.topo
        self.esquerda = medidas.esquerda
        self.largura = medidas.largura
        self.altura = medidas.altura

        # Iniciar
        self.IniciarFDrone()


    """
        Métodos
    """
    def IniciarFDrone(self):

        # Menu
        self.menu = self.menuBar()
        self.menu_arquivo = self.menu.addMenu("Projeto")

        self.menu_ajuda = self.menu.addMenu("Ajuda")
        self.menu_sobre = self.menu.addMenu("Sobre")
        # Submenu menu Projeto - Novo Projeto
        self.mb_novo_projeto = QAction(QtGui.QIcon("icones/geral/svg/folder.svg"), "Novo Projeto", self)
        self.mb_novo_projeto.setShortcut("Ctrl+N")
        self.mb_novo_projeto.setStatusTip("Novo Projeto")
        self.mb_novo_projeto.triggered.connect(self.NovoProjetoDialogo)
        self.menu_arquivo.addAction(self.mb_novo_projeto)
        # Submenu menu Projeto - Orientação interior
        self.mb_orientacao_interior = QAction(QtGui.QIcon("icones/drone2-icons/svg/photo-camera.svg"), "Parâmetros de Orientação Interior", self)
        self.mb_orientacao_interior.setShortcut("Ctrl+Shift+I")
        self.mb_orientacao_interior.setStatusTip("Orientacao Interior")
        self.mb_orientacao_interior.triggered.connect(self.OrientacaoInterior)
        self.menu_arquivo.addAction(self.mb_orientacao_interior)
        # Submenu menu Projeto - Planejamento de Voo
        self.mb_planejamento_voo = QAction(QtGui.QIcon("icones/drone-icons/svg/023-street-map.svg"), "Planejamento de Voo", self)
        self.mb_planejamento_voo.setShortcut("Ctrl+P")
        self.mb_planejamento_voo.setStatusTip("Planejamento de Voo")
        self.mb_planejamento_voo.triggered.connect(self.PlanejamentoDeVoo)
        self.menu_arquivo.addAction(self.mb_planejamento_voo)
        # Submenu menu Projeto - Datum
        self.mb_spatial_reference = QAction(QtGui.QIcon("icones/drone2-icons/svg/placeholder.svg"), "Referencia Espacial", self)
        self.mb_spatial_reference.setShortcut("Ctrl+R")
        self.mb_spatial_reference.setStatusTip("Referencia Espacial")
        self.mb_spatial_reference.triggered.connect(self.SpatialReference)
        self.menu_arquivo.addAction(self.mb_spatial_reference)
        # Submenu menu Projeto - Sair
        self.botao_sair = QAction(QtGui.QIcon("icones/geral/svg/door.svg"), "Sair", self)
        self.botao_sair.setShortcut("Ctrl+E")
        self.botao_sair.setStatusTip("Sair do FDrone ?")
        self.botao_sair.triggered.connect(self.SairFDrone)
        self.menu_arquivo.addAction(self.botao_sair)

        # Submenu menu sobre
        self.botao_sobre = QAction(QtGui.QIcon("icones/geral/svg/Help_and_Support_23389"), "Sobre F-Drone", self)
        self.botao_sobre.setStatusTip("Sobre o FDrone")
        self.botao_sobre.triggered.connect(self.SobreFDrone)
        self.menu_sobre.addAction(self.botao_sobre)

        # Submenu menu_ajuda

        # Titulo da Janela
        self.setWindowTitle(self.titulo)
        # Geometria da Janela
        self.setGeometry(self.topo, self.esquerda, self.largura, self.altura)

        # Exibindo
        self.show()

    """
        Eventos
    """
    def SairFDrone(self):
        self.statusbar.showMessage("O botão 'Sair' foi selecionado.")
        mensagem = QMessageBox.question(self, "Sair do FDrone ?", "Você realmente deseja sair do FDrone ?", QMessageBox.Yes|QMessageBox.No, QMessageBox.No)
        if(mensagem == QMessageBox.Yes):
            QCoreApplication.instance().quit()
        else:
            self.statusbar.showMessage("")

    def SobreFDrone(self):
        self.statusbar.showMessage("O botão 'Sobre' foi selecionado.")
        QMessageBox.about(self, "Sobre o F-Drone", "F-Drone - Versão Alfa 0.0.2 \n")

    def NovoProjetoDialogo(self):
        self.formulario_novo_projeto = DFormNovoProjeto.DialogoFormNovoProjeto(self)

    def PlanejamentoDeVoo(self):
        self.formulario_planejamento_voo = DFormPlanejamentoDeVoo.DialogoFormPlanejamentoDeVoo(self)

    def OrientacaoInterior(self):
        self.formulario_orientacao_interior = DFormOrientacaoInterior.DialogoOrientacaoInterior(self)

    def SpatialReference(self):
        self.formulario_spatial_reference = DFormSpatialReference.DialogoFormSpatialReference(self)

    def AbrirImagem(self):
        self.viewer = ImageViewer.QtImageViewer()
        self.setWindowTitle("Imagem")
        self.abrir_imagem = self.viewer.loadImageFromFile()  # Pops up file dialog.
        self.setCentralWidget(self.viewer)
        self.viewer.leftMouseButtonPressed.connect(self.viewer.handleLeftClick)
        self.viewer.show()




if __name__ == '__main__':
    Aplicativo = QApplication(sys.argv)
    JanelaFDrone = FDrone()

    exists = os.path.isfile("/settings.json")

    if exists:
        with open("settings.json") as settings:
            data = json.load(settings)
        os.chdir(data["Path"]) # Seta o Diretorio do projeto anterior como o original como o principal
        
    sys.exit(Aplicativo.exec())
    