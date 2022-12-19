# -*- coding: utf-8 -*-
"""
Created on Sat Jul  9 13:24:36 2022

@author: Adilson José Pereira Junior
"""

#import sympy as sym
from libs.waves_lib import OceanWave
from libs.gui_lib import Point, Line
from libs.structures_lib import Wall

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
    h_deltah = 10/100
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

    wall = Wall(length=h)
    wall.set_wave(onda)
    wall.calculate_deltah()
    wall.calculate_deltap(rho=rho)
    wall.calculate_p1(rho=rho)
    wall.calculate_p2(rho=rho)
    
    # CARGAS
    fator_l = l_maxima *(x_lim_max/2)/wall.p1

    # DESENHO DO CARREGAMENTO
    x_p3 = x_parede
    y_p3 = y_agua -altura_canva*(h_H + h_deltah)
    x_p7 = x_parede + wall.p1*fator_l
    y_p7 = y_agua
    x_p4 = x_parede + wall.deltap*fator_l
    y_p4 = yS_solo
    x_p6 = x_parede - wall.deltap*fator_l
    y_p6 = yS_solo
    x_p8 = x_parede - wall.p2*fator_l
    y_p8 = y_planomedio + h_H*altura_canva + 20
    x_p1 = x_parede
    y_p1 = y_agua
    
    #### COTAS
    # COTA DELTAH
    cota_deltah = Line(
        p1 = Point(l_maxima *(x_lim_max/4), y_planomedio),
        p2 = Point(l_maxima *(x_lim_max/4), y_agua)
    )
    t_cota_deltah = [cota_deltah.p1.x - 5, (cota_deltah.p2.y + cota_deltah.p1.y)/2 , str(round(wall.deltah,2)) + 'm']
    # COTA ALTURA DA PAREDE
    cota_h = Line(
        p1 = Point(l_maxima *(x_lim_max/4), y_agua),
        p2 = Point(l_maxima *(x_lim_max/4), yS_solo)
    )
    t_cota_h = [cota_h.p1.x - 5, (cota_h.p2.y + cota_h.p1.y)/2, str(round(profundidade - (altura_onda-wall.deltah),2)) + 'm']
    # COTA ALTURA DA PAREDE + ONDA
    cota_onda = Line(
        p1 = Point(l_maxima *(x_lim_max/4), y_p3),
        p2 = Point(l_maxima *(x_lim_max/4), y_planomedio)
    )
    t_cota_onda = [cota_onda.p1.x - 5, (cota_onda.p2.y + cota_onda.p1.y)/2, str(round((altura_onda),2)) + 'm']
    # COTA ALTURA DA PAREDE + ONDA
    cota_58 = Line(
        p1 = Point(l_maxima *(x_lim_max/4), y_agua),
        p2 = Point(l_maxima *(x_lim_max/4), y_p8)
    )
    t_cota_58 = [cota_58.p1.x - 5, (cota_58.p2.y + cota_58.p1.y)/2, str(round((altura_onda-wall.deltah),2)) + 'm']

    linha_58 = Line(
        p1 = Point(x_lim_min, y_p8),
        p2 = Point(x_lim_max, y_p8)
    )
    
    # TEXTOS
    t_agua = [x_lim_max - (8*4), y_agua -10, 'Água'] # x,y,text
    t_solo = [x_lim_max - (8*4), yS_solo -10 , 'Solo'] # x,y,text
    t_deltah = [plano_medio.p2.x - 60, plano_medio.p1.y -10 , 'Plano médio (Δℎ)'] # x,y,text
    t_carga_17 = [x_p7 + 30 , y_p7 +20, str(round(wall.p1/1000, 2)) + ' kPa'] # x,y,text
    t_carga_85 = [x_p8 - 30 , y_p8 +20, str(round(wall.p2/1000, 2)) + ' kPa'] # x,y,text
    t_carga_base_e = [parede.p1.x - (parede.p1.x - x_p6)/2 , y_p6 -20, str(round(wall.deltap/1000, 2)) + ' kPa'] # x,y,text
    t_carga_base_d = [parede.p1.x + (x_p4 - parede.p1.x)/2 , y_p4 -20, str(round(wall.deltap/1000, 2)) + ' kPa'] # x,y,text

    textos = [t_agua, t_solo, t_deltah, t_carga_17, t_carga_85, t_carga_base_e, t_carga_base_d]
    textos_cotas = [t_cota_deltah, t_cota_h, t_cota_onda, t_cota_58]
    cotas = [cota_deltah, cota_h, cota_onda, cota_58]
    carregamento = [x_p3, y_p3, x_p7, y_p7, x_p4, y_p4, x_p6, y_p6, x_p8, y_p8, x_p1, y_p1]
    return(solo, agua, parede, carregamento, plano_medio, textos, cotas, textos_cotas, linha_58)