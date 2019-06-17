import pdfkit
# https://pypi.org/project/pdfkit/

#pdfkit.from_string(...)

def gerar_relatorios(caminho, destino):
    pdfkit.from_file(caminho, destino)