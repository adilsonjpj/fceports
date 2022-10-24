import sympy as sym
import math
###################################
### PIANC 2002 Energia Cinética ###
###################################

def solver_energia_cinetica_atracacao(
    v=1,
    En = sym.Symbol('En'),
    MD = sym.Symbol('MD'),
    Va = sym.Symbol('Va'),
    Cm = sym.Symbol('Cm'),
    Ce = sym.Symbol('Ce'),
    Cs = sym.Symbol('Cs'),
    Cc = sym.Symbol('Cc')):
    return(sym.solvers.nsolve(
        (0.5 * MD * (Va**2) * Cm * Ce * Cs * Cc) - En
        , v
    ))

###################################
#### Coeficiente adc. de massa ####
###################################

def solver_coef_adicional_massa_pianc2002(Kc, D):
    # para Kc/D menor que 0.1
    Cm = 1.8
    # relacao entre Kc e D
    aux = Kc/D
    if(aux >= 0.1 and aux <= 0.5):
        Cm = 1.875 -(0.75 * (Kc/D))
    if(aux >= 0.5):
        Cm = 1.5
    return(Cm)

def solver_coef_adicional_massa_shigeraueda1981(D, CB, B):
    Cm = 1 + ((math.pi * D)/(2 * CB * B))
    return(Cm)

def solver_coef_adicional_massa_vascocosta1964(D, B):
    Cm = 1 + (2*D/B)
    return(Cm)

###################################
## Coeficiente de excentricidade ##
###################################

def solver_coef_excentricidade(k, R, gamma):
    Ce = ((k**2)+((R**2) * (math.cos(gamma)**2)))/((k**2)+(R**2))
    return(Ce)

def solver_k(CB, LBP):
    k = (0.19 * CB + 0.11) * LBP
    return(k)

def solver_R(LBP, x, B):
    R = math.sqrt((((LBP/2) - x)**2) + ((B/2)**2))
    return(R)

def solver_gamma(alpha, B, R):
    gamma = 90 - alpha - math.degrees(math.asin(B/(2*R)))
    return(gamma)

###################################
##### Coeficiente de rigidez ######
###################################

def solver_coef_rigidez(deltaf):
    Cs = 1.0
    # deltaf em milímetros
    if (deltaf <= 150):
        Cs = 0.9
    return(Cs)

###################################
### Est. Fechada - C. Conf. Cais ##
###################################

def solver_cc_est_fechada(Kc, D, alpha):
    # relacao entre Kc e D
    aux = Kc/D
    if(aux <= 0.5):
        Cc = 0.8
    if(aux > 0.5):
        Cc = 0.9
    if(alpha > 5):
        Cc = 1
    return(Cc)

###################################
# E. Semi-Fechada - C. Conf. Cais #
###################################

def solver_cc_est_semi_fechada(Kc, D, alpha):
    # relacao entre Kc e D
    aux = Kc/D
    if(aux <= 0.5):
        Cc = 0.9
    if(aux > 0.5):
        Cc = 1.0
    if(alpha > 5):
        Cc = 1
    return(Cc)


###################################
### Est. Aberta - C. Conf. Cais ###
###################################

def solver_cc_est_aberta():
    return(1.0)


###################################
### Força Exercida pelo Fluido ####
###################################

def solver_forca_fluido(
    guess=1,
    F = sym.Symbol('F'),
    Cf = sym.Symbol('Cf'),
    rho = sym.Symbol('𝜌'),
    v = sym.Symbol('v'),
    A = sym.Symbol('A')):
    return(sym.solvers.nsolve(
        (Cf * 0.5 * rho * (v**2) * A) - F
        , guess
    ))

###################################
##### Força Exercida pelo Ar ######
###################################

def solver_forca_trans_ar(
    v=1,
    FTW = sym.Symbol('FTW'),
    CTW = sym.Symbol('CTW'),
    rhoA = sym.Symbol('𝜌A'),
    AL = sym.Symbol('AL'),
    VW = sym.Symbol('VW')):
    return(sym.solvers.nsolve(
        (CTW * rhoA * AL * (VW**2) * (10**-4)) - FTW
        , v
    ))

def solver_forca_longi_ar(
    v=1,
    FLW = sym.Symbol('FLW'),
    CLW = sym.Symbol('CLW'),
    rhoA = sym.Symbol('𝜌A'),
    AL = sym.Symbol('AL'),
    VW = sym.Symbol('VW')):
    return(sym.solvers.nsolve(
        (CLW * rhoA * AL * (VW**2) * (10**-4)) - FLW
        , v
    ))

###################################
## Força Exercida pela Corrente ###
###################################

def solver_forca_trans_corrente(
    v=1,
    FTC = sym.Symbol('FTC'),
    CTC = sym.Symbol('CTC'),
    CCT = sym.Symbol('CCT'),
    rho = sym.Symbol('𝜌'),
    LBP = sym.Symbol('LBP'),
    dm = sym.Symbol('dm'),
    Vc = sym.Symbol('Vc')):
    return(sym.solvers.nsolve(
        (CTC * CCT * rho * LBP * dm * (Vc**2) * (10**-4)) - FTC
        , v
    ))

def solver_forca_longi_corrente(
    v=1,
    FLC = sym.Symbol('FLC'),
    CLC = sym.Symbol('CLC'),
    CCL = sym.Symbol('CCL'),
    rho = sym.Symbol('𝜌'),
    LBP = sym.Symbol('LBP'),
    dm = sym.Symbol('dm'),
    Vc = sym.Symbol('Vc')):
    return(sym.solvers.nsolve(
        (CLC * CCL * rho * LBP * dm * (Vc**2) * (10**-4)) - FLC
        , v
    ))