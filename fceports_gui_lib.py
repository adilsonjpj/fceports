# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 09:30:17 2022

@author: Adilson José Pereira Junior
"""


# Classe texto
class Texto:
    x = float
    y = float
    texto = str
    cor = 'black'
    fonte = ('Times New Roman', 11)

    def __init__(self, x, y, texto, cor=cor, fonte=fonte) -> None:
        self.x = x
        self.y = y
        self.texto = texto
        self.cor = cor
        self.fonte = fonte



# Classe carga
class CargaPontual:
    valor = float
    unidade = str
    def __init__(self) -> None:
        pass
    # Retorna uma string contendo o valor da carga junto da sua unidade
    def forca_texto(self) -> str:
        return(str(self.valor) + ' ' + self.unidade)
