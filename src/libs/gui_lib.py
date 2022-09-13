# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 09:30:17 2022

@author: Adilson José Pereira Junior
"""
from typing import List, Dict




# Classe carga
class CargaPontual:
    valor: float
    unidade: str
    def __init__(self, valor, unidade) -> None:
        self.valor = valor
        self.unidade = unidade
    # Retorna uma string contendo o valor da carga junto da sua unidade
    def forca_texto(self) -> str:
        return(str(self.valor) + ' ' + self.unidade)

# Classe ponto
class Point:
    x: float
    y: float
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y
    # Retorna uma lista com X seguido de Y
    def coord(self) -> List[float]:
        return([self.x, self.y])


# Classe linha
class Line:
    p1: Point
    p2: Point
    def __init__(self, p1: Point, p2: Point) -> None:
        self.p1 = p1
        self.p2 = p2
    # Retorna uma lista com X seguido de Y
    def coord(self) -> List[float]:
        return([self.p1.x, self.p1.y, self.p2.x, self.p2.y])


# Classe texto
class Text:
    p: Point
    text: str
    color: str
    font = ('Times New Roman', 11)

    def __init__(self, p: Point, text: str, color: str='black', font=font) -> None:
        self.p = p
        self.text = text
        self.color = color
        self.font = font