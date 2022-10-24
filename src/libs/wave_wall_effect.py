# -*- coding: utf-8 -*-
"""
Created on Sat Jul  9 13:24:36 2022

@author: Adilson José Pereira Junior
"""

import sympy as sym

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

def solver_variacaodepressao(
    v=1, 
    deltap = sym.Symbol('Δp'),
    H = sym.Symbol('H'),
    L= sym.Symbol('L'),
    h = sym.Symbol('h')):
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
    rho = sym.Symbol('𝜌'),
    g = sym.Symbol('g'),
    H = sym.Symbol('H'),
    h = sym.Symbol('h')):
    return(sym.solvers.nsolve(
        ( (deltap + rho*g*h) * ( (H + deltah)/(H + h + deltah) ) ) - p17
        , v
    ))

def solver_p58(
    v=1,
    p58 = sym.Symbol('p58'),
    deltah = sym.Symbol('Δh'),
    rho = sym.Symbol('𝜌'),
    g = sym.Symbol('g'),
    H = sym.Symbol('H')):
    return(sym.solvers.nsolve(
        (rho*g*( H - deltah )) - p58
        , v
    ))

def solver_forca_onda_arrebentacao_parede(
    v=1,
    Ft = sym.Symbol('Ft'),
    Cp = sym.Symbol('Cp'),
    gama_agua = sym.Symbol('𝛾w'),
    ds = sym.Symbol('ds')):
    return(sym.solvers.nsolve(
        ( (1.1 * Cp * gama_agua * (ds**2)) + (2.4 * gama_agua * (ds**2) )) - Ft
        , v
    ))