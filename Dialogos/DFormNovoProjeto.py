from Ferramentas import ler, textos, medidas
from SubJanelas import Tabela
from Ferramentas import CriarDiretorio
from PyQt5.QtWidgets import (QFileDialog, QPushButton, QDialog, QDialogButtonBox, QFormLayout, QGroupBox, QLabel, QLineEdit, QComboBox, QVBoxLayout)
import json
import os

class DialogoFormNovoProjeto(QDialog):

    def __init__(self, parent):

        super(DialogoFormNovoProjeto, self).__init__(parent)

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
        self.pb_pasta_projeto = QPushButton("Criar/Escolher pasta do projeto", self)
        self.pb_pasta_projeto.clicked.connect(self.PastaProjeto)
        self.le_pasta_projeto = QLineEdit()


        # Formulário
        self.le_nome = QLineEdit()
        self.le_responsavel_tecnico = QLineEdit()
        self.le_crea = QLineEdit()
        self.le_empresa = QLineEdit()
        self.le_pais = QLineEdit()      
        self.le_local = QLineEdit()
        self.le_cidade = QLineEdit()
        self.le_uf = QLineEdit()
        self.le_descricao = QLineEdit()

        self.IniciarDialogoFormNovoProjeto()

    """
        Métodos
    """
    def IniciarDialogoFormNovoProjeto(self):

        # Caminho Projeto
        self.pasta_novo_projeto_gb = QGroupBox("Pasta do Projeto")
        layout_pasta = QVBoxLayout()
        layout_pasta.addWidget(self.pb_pasta_projeto)
        layout_pasta.addWidget(self.le_pasta_projeto)
        self.pasta_novo_projeto_gb.setLayout(layout_pasta)

        # Entradas
        self.form_novo_projeto_gb = QGroupBox("Novo Projeto")
        layout_form = QFormLayout()
        layout_form.addRow(QLabel(textos.NOME), self.le_nome)
        layout_form.addRow(QLabel(textos.RESPONSAVEL_TECNICO), self.le_responsavel_tecnico)
        layout_form.addRow(QLabel(textos.CREA), self.le_crea)
        layout_form.addRow(QLabel(textos.EMPRESA), self.le_empresa)
        layout_form.addRow(QLabel(textos.LOCAL), self.le_local)
        layout_form.addRow(QLabel(textos.PAIS), self.le_pais)
        layout_form.addRow(QLabel(textos.CIDADE), self.le_cidade)
        layout_form.addRow(QLabel(textos.UF), self.le_uf)
        layout_form.addRow(QLabel(textos.DESCRICAO), self.le_descricao)

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
            self.le_pasta_projeto.text(),
            self.le_nome.text(),
            self.le_responsavel_tecnico.text(),
            self.le_local.text(),
            self.le_crea.text(),
            self.le_empresa.text(),
            self.le_pais.text(),      
            self.le_cidade.text(),
            self.le_uf.text(),
            self.le_descricao.text(),
        ]
        self.CriarJson(self.comunicador)
        
    def CriarJson(self, comunicador):
        
        data = {
                "Pasta do Projeto":comunicador[0],
                "Nome":comunicador[1],
                "Responsavel Tecnico":comunicador[2],
                "Local":comunicador[3],
                "Crea":comunicador[4],
                "Empresa":comunicador[5],
                "Pais":comunicador[6],
                "Cidade":comunicador[7],
                "UF":comunicador[8],
                "Descricao":comunicador[9],
            }

        path = {
            "Path": comunicador[0],
        }

        with open("settings.json", "w") as write_file:
            json.dump(path, write_file)

        CriarDiretorio.criar_diretorios(comunicador[0]) # Cria as pastas no novo Diretorio Escolhido
        
        with open(comunicador[0] + "/Json/ProjectData.json", "w") as write_file:
            json.dump(data, write_file)
        
        self.close()


