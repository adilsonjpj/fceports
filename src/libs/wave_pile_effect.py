# -*- coding: utf-8 -*-
"""
Created on Sat Jul  9 13:24:36 2022

@author: Adilson José Pereira Junior
"""

import sympy as sym
import math
#from libs.waves_lib import OceanWave
#from libs.gui_lib import Point, Line
#from libs.structures_lib import Pile

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

def solver_forca_arraste_kd_max(
    v=1,
    kd = sym.Symbol('kd'),
    eta = sym.Symbol('𝜂')):
    return(sym.solvers.nsolve(
        (( (1/4) * eta ) - kd)
        , v
    ))

# PERFORMANCE
def solver_forca_arraste_gui(CD, rho, g, D, H, T, L, k, z, t, h):
    FD = ( CD*0.5*rho*g*D*(H**2) * ( ((g*T**2)/(4*L**2)) * (( (math.cosh(k*(z+h)))/(math.cosh(k*h)) )**2)) * math.Abs(math.cos(2*math.pi*t/T)) * math.cos(2*math.pi*t/T) )
    return( FD )

def solver_forca_arraste_max_gui(CD , rho, g, D, H, T, L, k, z, h):
   return(( CD*0.5*rho*g*D*(H**2) * ( ((g*T**2)/(4*L**2)) * (( (math.cosh(k*(z+h)))/(math.cosh(k*h)) )**2))))

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
        (( 0.5 + ((0.5/eta) * ( 0.5 + (1-sym.cosh(2*k*h))/(2*k*h*sym.sinh(2*k*h)) )) ) - sd), v
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


##################################
##################################
######### ARREBENTACAO ###########
##################################
##################################
def solver_forca_onda_arrebentacao_estaca(
    v=1,
    Fb = sym.Symbol('Fb'),
    gamma_agua = sym.Symbol('𝛾𝑤'),
    CD = sym.Symbol('CD'),
    D = sym.Symbol('D'),
    Hb = sym.Symbol('Hb')):
    return(sym.solvers.nsolve(
        (CD * 0.5 * gamma_agua * D * (Hb**2)) - Fb
        , v
    ))