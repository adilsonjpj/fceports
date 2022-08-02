# -*- coding: utf-8 -*-
"""
Created on Sat Jul  9 13:24:36 2022

@author: Adilson José Pereira Junior
"""

#from cairo import PS_LEVEL_3
import sympy as sym
from own_libs.waves_lib import OceanWave
from own_libs.gui_lib import Point, Line, Text

# Eta
def solver_eta(
    v=1,
    eta = sym.Symbol('𝜂'),
    k = sym.Symbol('k'),
    h = sym.Symbol('h')):
    return(sym.solvers.nsolve(
        (0.5 * (1 + ( (2*k*h)/(sym.sinh(2*k*h)) ) )) - eta
        , v
    ))

## EFEITO DA ONDA EM PAREDES

def solver_planomediodaonda(
    v=1, 
    deltah = sym.Symbol('Δh'), 
    H = sym.Symbol('H'),
    L= sym.Symbol('L'),
    h = sym.Symbol('h')):
    return(sym.solvers.nsolve(
        (((sym.pi*H**2)/L) * sym.coth((2*sym.pi*h)/L)) - deltah
        , v
    ))

def solver_variacaodepressao(v=1, deltap = sym.Symbol('Δp'), H = sym.Symbol('H'),L= sym.Symbol('L'),h = sym.Symbol('h')):
    return(sym.solvers.nsolve(
        ( H / sym.cosh((2*sym.pi*h)/L)) - deltap
        , v
    ))

def solver_deltap(
    v=1, 
    deltap = sym.Symbol('Δp'), 
    H = sym.Symbol('H'),
    L= sym.Symbol('L'),
    rho = sym.Symbol('𝜌'),
    g = sym.Symbol('g'),
    h = sym.Symbol('h')):
    return(sym.solvers.nsolve(
        ( (rho*g*H) / sym.cosh((2*sym.pi*h)/L)) - deltap
        , v
    ))

def solver_p17(
    v=1,
    p17 = sym.Symbol('p17'), 
    deltap = sym.Symbol('Δp'),
    deltah = sym.Symbol('Δh'),
    H = sym.Symbol('H'),
    h = sym.Symbol('h')):
    return(sym.solvers.nsolve(
        ( (deltap + h) * ( (H + deltah)/(H + h + deltah) ) ) - p17
        , v
    ))

def solver_p58(
    v=1,
    p58 = sym.Symbol('p58'),
    deltah = sym.Symbol('Δh'),
    H = sym.Symbol('H')):
    return(sym.solvers.nsolve(
        ( H - deltah ) - p58
        , v
    ))

def forca_onda_arrebentacao_parede(
    v=1,
    Ft = sym.Symbol('Ft'),
    Cp = sym.Symbol('Cp'),
    gama_agua = sym.Symbol('𝛾w'),
    ds = sym.Symbol('ds'),
    Hb = sym.Symbol('Hb')):
    return(sym.solvers.nsolve(
        ( (1.1 * Cp * gama_agua * (ds**2)) + (2.4 * gama_agua * (ds**2) )) - Ft
        , v
    ))


############################################################################################
## REPASSANDO OS VALORES CALCULADOS PARA A INTERFACE GRÁFICA
############################################################################################

def coordenadas_canva(
    largura_canva, # Largura do canva
    altura_canva, # Altura do Canva
    periodo_onda, # Periodo da onda
    profundidade, # Profundidade da onda
    rho,
    altura_onda
    ):
    
    # Calculando o comprimento da onda em funcao da profundidade e do periodo
    #comprimento_onda = solver_dispersao(T= periodo_onda, h = profundidade)
    
    # criando a onda
    onda = OceanWave(period=periodo_onda, height=altura_onda)
    # calculando o comprimento
    onda.find_length(depth=profundidade)

    ## SETANDO AS VARIAVEIS DA FORMULA
    h = profundidade # Profundidade do local

    # VARIAVEIS PARA O DESENHO
    # PORCENTAGENS
    h_parede = 80/100
    h_agua = 55/100
    h_solo = 5/100
    h_H = 15/100
    h_deltah = 3/100
    l_maxima = 50/100
    
    #########################################################################################
    # SISTEMA DE COORDENADAS CANTO SUPERIOR ESQUERDO (0,0) CANTO INFERIOR DIREITO (MAX,MAX)
    # LIMITES DO QUADRO DE DESENHO
    x_lim_min = 0 # Canto esquerdo da tela
    x_lim_max = largura_canva # Canto direito da tela

    # DESENHO FIXO, DEVE SER MODIFICADO AQUI
    
    # DESENHO DO SOLO
    yS_solo = altura_canva - altura_canva*h_solo
    solo = Line(
        p1 = Point(x_lim_min, altura_canva), 
        p2 = Point(x_lim_max, yS_solo)
    )

    # DESENHO DA AGUA
    y_agua = yS_solo - (altura_canva*h_agua)
    agua = Line(
        p1 = Point(x_lim_min, y_agua), 
        p2 = Point(x_lim_max, y_agua)
    )
    
    # DESENHO PLANO MEDIO
    y_planomedio = y_agua - (altura_canva*h_deltah)
    plano_medio = Line(
        p1 = Point(x_lim_min, y_planomedio), 
        p2 = Point(x_lim_max, y_planomedio)
    )

    # DESENHO DA PAREDE
    x_parede = x_lim_max/2
    parede = Line(
        p1 = Point(x_parede, yS_solo), 
        p2 = Point(x_parede, yS_solo - (altura_canva*h_parede))
    )

    deltah = solver_planomediodaonda(H = onda.H, L = onda.L, h = h)
    deltap = solver_variacaodepressao(H = onda.H, L = onda.L, h = h)

    # CARGAS
    x_p17 = solver_p17(deltap = deltap, deltah = deltah, H = onda.H, h = h)
    x_p58 = solver_p58(deltah = deltah, H = onda.H)

    fator_l = l_maxima *(x_lim_max/2)/x_p17

    # DESENHO DO CARREGAMENTO
    x_p3 = x_parede
    y_p3 = y_agua -altura_canva*(h_H + h_deltah)
    x_p7 = x_parede + x_p17*fator_l
    y_p7 = y_agua
    x_p4 = x_parede + deltap*fator_l
    y_p4 = yS_solo
    x_p6 = x_parede - deltap*fator_l
    y_p6 = yS_solo
    x_p8 = x_parede - x_p58*fator_l
    y_p8 = y_planomedio + h_H*altura_canva
    x_p1 = x_parede
    y_p1 = y_agua
    
    # TEXTOS
    t_agua = [x_lim_max - (8*4), y_agua -10, 'Água'] # x,y,text
    t_solo = [x_lim_max - (8*4), yS_solo -10 , 'Solo'] # x,y,text
    t_deltah = [plano_medio.p1.x + 50, plano_medio.p1.y -10 , 'Plano médio (Δℎ)'] # x,y,text
    t_carga_17 = [x_p7 + 30 , y_p7 +20, str(round(x_p17, 2)) + ' kPa'] # x,y,text
    t_carga_85 = [x_p8 - 30 , y_p8 +20, str(round(x_p58, 2)) + ' kPa'] # x,y,text
    t_carga_base_e = [parede.p1.x - (parede.p1.x - x_p6)/2 , y_p6 -20, str(round(deltap, 2)) + ' kPa'] # x,y,text
    t_carga_base_d = [parede.p1.x + (x_p4 - parede.p1.x)/2 , y_p4 -20, str(round(deltap, 2)) + ' kPa'] # x,y,text

    textos = [t_agua, t_solo, t_deltah, t_carga_17, t_carga_85, t_carga_base_e, t_carga_base_d]

    carregamento = [x_p3, y_p3, x_p7, y_p7, x_p4, y_p4, x_p6, y_p6, x_p8, y_p8, x_p1, y_p1]
    return(solo, agua, parede, carregamento, plano_medio, textos)