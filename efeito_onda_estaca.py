# -*- coding: utf-8 -*-
"""
Created on Sat Jul  9 13:24:36 2022

@author: Adilson José Pereira Junior
"""

import sympy as sym
from own_libs.waves_lib import OceanWave
from own_libs.gui_lib import Point, Line

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

## EFEITO DA ONDA EM ESTACAS

class ForcaEstaca:
    CM
    CD
    rho
    g,
    D,
    H,
    T,
    L,
    k,
    z,
    t,
    h,

    def solver_forca_inercia_gui(CM, rho, g, D, H, T, L, k, z, t, h):
        FM = ( CM*rho*g*(math.pi*(D**2)/4)*H*( (math.pi/L) * ((math.cosh(k*(z+h)))/(math.cosh(k*h))) ) * math.sin(-2*math.pi*t/T))
        return( FM )


###############################################################################
###############################################################################
# FORCA DE INERCIA
###############################################################################
###############################################################################
def solver_forca_inercia(
    v=1,
    FM = sym.Symbol('FM'),
    CM = sym.Symbol('CM'),
    rho = sym.Symbol('𝜌'),
    g = sym.Symbol('g'),
    D = sym.Symbol('D'),
    H = sym.Symbol('H'),
    T = sym.Symbol('T'),
    L = sym.Symbol('L'),
    k = sym.Symbol('k'),
    z = sym.Symbol('z'),
    t = sym.Symbol('t'),
    h = sym.Symbol('h')):
    return(sym.solvers.nsolve(
        ( CM*rho*g*(sym.pi*(D**2)/4)*H* 
        ( (sym.pi/L) * ((sym.cosh(k*(z+h)))/(sym.cosh(k*h))) ) *
        sym.sin(-2*sym.pi*t/T)) - FM
        , v
    ))

def solver_forca_inercia_max(
    v=1,
    FM = sym.Symbol('FM'),
    CM = sym.Symbol('CM'),
    rho = sym.Symbol('𝜌'),
    g = sym.Symbol('g'),
    D = sym.Symbol('D'),
    H = sym.Symbol('H'),
    T = sym.Symbol('T'),
    L = sym.Symbol('L'),
    k = sym.Symbol('k'),
    z = sym.Symbol('z'),
    h = sym.Symbol('h')):
    return(sym.solvers.nsolve(
        ( CM*rho*g*(sym.pi*(D**2)/4)*H* 
        ( (sym.pi/L) * ((sym.cosh(k*(z+h)))/(sym.cosh(k*h))) ) - FM)
        , v
    ))

def solver_forca_inercia_res(
    v=1,
    FM = sym.Symbol('FM'),
    CM = sym.Symbol('CM'),
    rho = sym.Symbol('𝜌'),
    g = sym.Symbol('g'),
    D = sym.Symbol('D'),
    H = sym.Symbol('H'),
    km = sym.Symbol('km')):
    return(sym.solvers.nsolve(
        (CM * rho * g * (sym.pi * (D**2)/4) * H * km) - FM
        , v
    ))

def solver_forca_inercia_km(
    v=1,
    km = sym.Symbol('km'),
    t = sym.Symbol('t'),
    k = sym.Symbol('k'),
    h = sym.Symbol('h'),
    T = sym.Symbol('T')):
    return(sym.solvers.nsolve(
        ( (1/2) * sym.tanh(k*h) * sym.sin( -2*sym.pi*t/T )) - km
        , v
    ))

def solver_forca_inercia_km_max(
    v=1,
    km = sym.Symbol('km'),
    k = sym.Symbol('k'),
    h = sym.Symbol('h')):
    return(sym.solvers.nsolve(
        ( (1/2) * sym.tanh(k*h) ) - km
        , v
    ))
### PERFORMANCE PARA O GUI
def solver_forca_inercia_gui(CM, rho, g, D, H, T, L, k, z, t, h):
    FM = ( CM*rho*g*(math.pi*(D**2)/4)*H*( (math.pi/L) * ((math.cosh(k*(z+h)))/(math.cosh(k*h))) ) * math.sin(-2*math.pi*t/T))
    return( FM )
def solver_forca_inercia_max_gui(CM, rho, g, D, H, L, k, z, h):
    FM = CM*rho*g*(math.pi*(D**2)/4)*H* ( (math.pi/L) * ((math.cosh(k*(z+h)))/(math.cosh(k*h))) )
    return( FM )

###############################################################################
###############################################################################
# FORCA DE ARRASTE
###############################################################################
###############################################################################
def solver_forca_arraste(
    v=1,
    FD = sym.Symbol('FD'),
    CD = sym.Symbol('CD'),
    rho = sym.Symbol('𝜌'),
    g = sym.Symbol('g'),
    D = sym.Symbol('D'),
    H = sym.Symbol('H'),
    T = sym.Symbol('T'),
    L = sym.Symbol('L'),
    k = sym.Symbol('k'),
    z = sym.Symbol('z'),
    t = sym.Symbol('t'),
    h = sym.Symbol('h')):
    return(sym.solvers.nsolve(
        ( CD*0.5*rho*g*D*(H**2) * 
        ( ((g*T**2)/(4*L**2)) * (( (sym.cosh(k*(z+h)))/(sym.cosh(k*h)) )**2)) *
        sym.Abs(sym.cos(2*sym.pi*t/T)) * sym.cos(2*sym.pi*t/T) ) - FD
        , v
    ))

def solver_forca_arraste_max(
    v=1,
    FD = sym.Symbol('FD'),
    CD = sym.Symbol('CD'),
    rho = sym.Symbol('𝜌'),
    g = sym.Symbol('g'),
    D = sym.Symbol('D'),
    H = sym.Symbol('H'),
    T = sym.Symbol('T'),
    L = sym.Symbol('L'),
    k = sym.Symbol('k'),
    z = sym.Symbol('z'),
    h = sym.Symbol('h')):
    return(sym.solvers.nsolve(
        ( CD*0.5*rho*g*D*(H**2) * 
        ( ((g*T**2)/(4*L**2)) * (( (sym.cosh(k*(z+h)))/(sym.cosh(k*h)) )**2)) - FD)
        , v
    ))

def solver_forca_arraste_res(
    v=1,
    FD = sym.Symbol('FD'),
    CD = sym.Symbol('CD'),
    rho = sym.Symbol('𝜌'),
    g = sym.Symbol('g'),
    D = sym.Symbol('D'),
    H = sym.Symbol('H'),
    kd = sym.Symbol('kd')):
    return(sym.solvers.nsolve(
        (CD * 0.5 * rho * g * D * (H**2) * kd) - FD
        , v
    ))


def solver_forca_arraste_kd(
    v=1,
    kd = sym.Symbol('kd'),
    eta = sym.Symbol('𝜂'),
    t = sym.Symbol('t'),
    T = sym.Symbol('T')):
    return(sym.solvers.nsolve(
        ( (1/4) * eta * sym.Abs( sym.cos(2*sym.pi*t/T) ) * sym.cos(2*sym.pi*t/T)) - kd
        , v
    ))

# PERFORMANCE
def solver_forca_arraste_gui(CD, rho, g, D, H, T, L, k, z, t, h):
    FD = ( CD*0.5*rho*g*D*(H**2) * ( ((g*T**2)/(4*L**2)) * (( (math.cosh(k*(z+h)))/(math.cosh(k*h)) )**2)) * math.Abs(math.cos(2*math.pi*t/T)) * math.cos(2*math.pi*t/T) )
    return( FD )

def solver_forca_arraste_max_gui(CD, rho, g, D, H, T, L, k, z, h):
    FD = CD*0.5*rho*g*D*(H**2) * ( ((g*T**2)/(4*L**2)) * (( (math.cosh(k*(z+h)))/(math.cosh(k*h)) )**2))
    return( FD )

###############################################################################
###############################################################################
# MOMENTO DE ARRASTE
###############################################################################
###############################################################################
def solver_momento_arraste_res(
    v=1,
    MD = sym.Symbol('MD'),
    FD = sym.Symbol('FD'),
    h = sym.Symbol('h'),
    sd = sym.Symbol('sd')):
    return(sym.solvers.nsolve(
        (FD * h * sd) - MD
        , v
    ))

def solver_momento_arraste_sd(
    v=1,
    sd = sym.Symbol('sd'),
    eta = sym.Symbol('𝜂'),
    k = sym.Symbol('k'),
    h = sym.Symbol('h')):
    return(sym.solvers.nsolve(
        ( (1/2) + ( (1/(2*eta)) * ( (1-sym.cosh(2*k*h)) / (2*k*h*sym.sinh(2*k*h)) ) ) ) - sd
        , v
    ))

###############################################################################
###############################################################################
# MOMENTO DE INERCIA
###############################################################################
###############################################################################
def solver_momento_inercia_res(
    v=1,
    MM = sym.Symbol('MM'),
    FM = sym.Symbol('FM'),
    h = sym.Symbol('h'),
    sm = sym.Symbol('sm')):
    return(sym.solvers.nsolve(
        (FM * h * sm ) - MM
        , v
    ))
def solver_momento_inercia_sm(
    v=1,
    sm = sym.Symbol('sm'),
    k = sym.Symbol('k'),
    h = sym.Symbol('h')):
    return(sym.solvers.nsolve(
        ( 1 + ((1-sym.cosh(k*h)) / (k*h*sym.sinh(k*h)))) - sm
        , v
    ))

############################################################################################
## REPASSANDO OS VALORES CALCULADOS PARA A INTERFACE GRÁFICA
############################################################################################

def coordenadas_canva_arraste(
    largura_canva, # Largura do canva
    altura_canva, # Altura do Canva
    periodo_onda, # Periodo da onda
    profundidade, # Profundidade da onda
    diametro, # Diametro da Estaca
    CD,
    CM,
    rho,
    altura_onda
    ):
    
    
    
    
    
    
    
    
    # criando a onda
    onda = OceanWave(T=periodo_onda, H=altura_onda)
    # calculando o comprimento
    onda.find_length(h=profundidade)

    ## SETANDO AS VARIAVEIS DA FORMULA
    h = round(profundidade,2) # Profundidade do local

    # VARIAVEIS PARA O DESENHO
    # PORCENTAGENS
    h_estaca = 80/100
    h_agua = 55/100
    h_solo = 5/100
    h_H = 15/100
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
    
    # DESENHO DA ESTACA
    x_estaca = x_lim_max/2
    estaca = Line(
        p1 = Point(x_estaca, yS_solo), 
        p2 = Point(x_estaca, yS_solo - (altura_canva*h_estaca))
    )
    
    ## SETANDO AS VARIAVEIS DA FORMULA
    D = diametro # Diâmetro da estaca

    # Resultante
    #km_max = solver_forca_inercia_km_max(k=k, h=profundidade)
    #FM = solver_forca_inercia_res(CM=CM, rho=rho, g=9.81, D=diametro, H=altura_onda, km=km_max)

    # Momentos
    #sm = solver_momento_inercia_sm(k=a, h=profundidade)
    #MM = solver_momento_inercia_res(FM=FM, h=profundidade, sm=sm)

    # DESENHO DO CARREGAMENTO

    carga_original_topo = 0
    carga_original_base = 0

    loads = []
    loads.append( x_estaca ) # Primeiro x
    loads.append( y_agua ) 
    for i in range(int(h*10) + 1):
        carga_ponto = solver_forca_arraste_max_gui(
            CD = CD,
            rho = rho,
            g = 9.81,
            D = D,
            H = H,
            T = T,
            L = L,
            k = k,
            z = float(-i/10),
            h = h
        )
        # Salvando os max e min
        if (i==0):
            carga_original_topo = carga_ponto/1000
        if (i==h*10):
            carga_original_base = carga_ponto/1000
        
        x = (carga_ponto/escala_x) + xS_estaca
        y = ((i/10) * escala_y) + y_agua
        #print('x=' + str(x))
        #print('y=' + str(y))
        loads.append( x ) # X
        loads.append( y ) # Vai ser o Y

    # Final
    loads.append( xS_estaca )
    loads.append( yI_estaca )

    # TEXTOS
    t_agua = [x_lim_max - (8*4), y_agua -15, 'Água'] # x,y,text
    t_solo = [x_lim_max - (8*4), yS_solo -15 , 'Solo'] # x,y,text
    t_carga_topo = [loads[2] + 30 , loads[1] +20, str(round(carga_original_topo, 2)) + ' kN/m'] # x,y,text
    t_carga_base = [loads[-4] + 30 , loads[-1] -20, str(round(carga_original_base, 2)) + ' kN/m'] # x,y,text
    
    textos = [t_agua, t_solo, t_carga_topo, t_carga_base]

    solo = [xI_solo, yI_solo, xS_solo, yS_solo]
    agua = [xI_agua, y_agua, xS_agua, y_agua]
    estaca = [xI_estaca, yI_estaca, xS_estaca, yS_estaca]
    carga = loads

    return(solo, agua, estaca, carga, textos)

###################################################
###################################################
###################################################
###################################################
###################################################
###################################################
###################################################
###################################################
###################################################
###################################################
###################################################
###################################################
###################################################
###################################################
###################################################
###################################################
###################################################
###################################################
###################################################
###################################################
###################################################
###################################################
###################################################
###################################################
###################################################
###################################################

def coordenadas_canva_inercia(
    largura_canva, # Largura do canva
    altura_canva, # Altura do Canva
    periodo_onda, # Periodo da onda
    profundidade, # Profundidade da onda
    diametro, # Diametro da Estaca
    CD,
    CM,
    rho,
    altura_onda
    ):
    
    # Calculando o comprimento da onda em funcao da profundidade e do periodo
    comprimento_onda = solver_dispersao(T= periodo_onda, h = profundidade)
    
    ## SETANDO AS VARIAVEIS DA FORMULA
    D = diametro # Diâmetro da estaca
    h = round(profundidade,2) # Profundidade do local
    L = comprimento_onda
    H = altura_onda
    T = periodo_onda
    k = (2*sym.pi)/L

    # VARIAVEIS PARA O DESENHO
    escala_y = 15
    escala_x = 40
    h_desenho = h * escala_y
    D_desenho = D
    # RETORNO DA FUNCAO
#    solo = []
#    agua = []
#    estaca = []
#    carga = []
    #########################################################################################
    # SISTEMA DE COORDENADAS CANTO SUPERIOR ESQUERDO (0,0) CANTO INFERIOR DIREITO (MAX,MAX)
    # LIMITES DO QUADRO DE DESENHO
    x_lim_min = 0 # Canto esquerdo da tela
    x_lim_max = largura_canva # Canto direito da tela

    # DESENHO DO SOLO
    # DESENHO FIXO, DEVE SER MODIFICADO AQUI
    xI_solo = x_lim_min
    yI_solo = altura_canva
    xS_solo = x_lim_max
    yS_solo = altura_canva - 30

    # DESENHO DA AGUA
    y_agua = yS_solo - h_desenho
    xI_agua = x_lim_min
    xS_agua = x_lim_max
   
    # DESENHO DA ESTACA
    xI_estaca = x_lim_max/2 -D_desenho/2
    yI_estaca = yS_solo
    xS_estaca = x_lim_max/2 +D_desenho/2
    yS_estaca = yS_solo - h_desenho - 50 # Somei 50 para ficar acima do nível d'agua

    # Resultante
    km_max = solver_forca_inercia_km_max(k=k, h=profundidade)
    FM = solver_forca_inercia_res(CM=CM, rho=rho, g=9.81, D=diametro, H=altura_onda, km=km_max)

    # Momentos
    sm = solver_momento_inercia_sm(k=k, h=profundidade)
    MM = solver_momento_inercia_res(FM=FM, h=profundidade, sm=sm)

    # DESENHO DA RESULTANTE
    resultante = 'aaa'

    # DESENHO DO CARREGAMENTO

    carga_original_topo = 0
    carga_original_base = 0

    loads = []
    loads.append( xS_estaca ) # Primeiro x
    loads.append( y_agua ) 
    for i in range(int(h*10) + 1):
        carga_ponto = solver_forca_inercia_max_gui(
            CM=CM, 
            rho=rho, 
            g=9.81, 
            D=D, 
            H=H, 
            L=L, 
            k=k, 
            z=float(-i/10), 
            h=h)
        # Salvando os max e min
        if (i==0):
            carga_original_topo = carga_ponto/1000
        if (i==h*10):
            carga_original_base = carga_ponto/1000
        
        x = (carga_ponto/escala_x) + xS_estaca
        y = ((i/10) * escala_y) + y_agua
        #print('x=' + str(x))
        #print('y=' + str(y))
        loads.append( x ) # X
        loads.append( y ) # Vai ser o Y

    # Final
    loads.append( xS_estaca )
    loads.append( yI_estaca )

    

    # TEXTOS
    t_agua = [x_lim_max - (8*4), y_agua -15, 'Água'] # x,y,text
    t_solo = [x_lim_max - (8*4), yS_solo -15 , 'Solo'] # x,y,text
    t_carga_topo = [loads[2] + 30 , loads[1] +20, str(round(carga_original_topo, 2)) + ' kN/m'] # x,y,text
    t_carga_base = [loads[-4] + 30 , loads[-1] -20, str(round(carga_original_base, 2)) + ' kN/m'] # x,y,text
    
    textos = [t_agua, t_solo, t_carga_topo, t_carga_base]
    
    solo = [xI_solo, yI_solo, xS_solo, yS_solo]
    agua = [xI_agua, y_agua, xS_agua, y_agua]
    estaca = [xI_estaca, yI_estaca, xS_estaca, yS_estaca]
    carga = loads

    return(solo, agua, estaca, carga, textos, )