# -*- coding: utf-8 -*-
"""
Created on Sat Jul  9 13:20:17 2022

@author: Adilson José Pereira Junior
"""

# Importação das bibliotecas necessárias
import sympy as sym
import math

### Equação da dispersão para ondas
### Necessário especificar todos -1 parâmetro a ser obtido
### A exatidão dos resultado pode variar de acordo com o v, pois é função do nsolve
# Exemplo de uso: solver_dispersao(T=5,h=1)
def solver_dispersao(v=1,L = sym.Symbol('L'),T= sym.Symbol('T'),h = sym.Symbol('h'),g = 9.81):
    return(sym.solvers.nsolve(g*(2*sym.pi/L)*sym.tanh(h*(2*sym.pi/L)) - ((2*sym.pi/T)**2), v))

### Equação para a velocidade de grupo
### Retorna diretamente a velocidade de grupo
def solver_velocidadedegrupo(L, T, h):
    return(((L/T)/2)*(1+(2*2*math.pi*h/L)/(math.sinh(2*2*math.pi*h/L))))
    
### Equação para a energia total da onda
def solver_energiatotal(H, g=9.81, ho=1024):
    return(ho*g*(H**2)/8)

### A onda tem propriedades, suas propriedades são
class Onda:
    def __init__(self, T, H) -> None:
        self.T = T
        self.H = H
        self.a = H/2
        self.sigma = (2*math.pi)/T
    
    def calcula_L(self, h) -> None:
        self.L = solver_dispersao(T= self.T, h = h, g = 9.81)
