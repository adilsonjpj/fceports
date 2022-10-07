import sympy as sym

def solver_reynolds(
    v=1, 
    Re = sym.Symbol('Re'), 
    Uo = sym.Symbol('Uo'),
    D= sym.Symbol('D'),
    viscosidade_cinematica = sym.Symbol('𝜈')):
    return(sym.solvers.nsolve(
        ((Uo * D)/viscosidade_cinematica) - Re
        , v
    ))

def solver_strouhal(
    v=1, 
    S = sym.Symbol('S'), 
    fk = sym.Symbol('fk'),
    D = sym.Symbol('D'),
    Uo = sym.Symbol('Uo')):
    return(sym.solvers.nsolve(
        ((fk * D)/Uo) - S
        , v
    ))

def solver_forca_corrente_estaca(
    v=1, 
    FD = sym.Symbol('FD'), 
    CD = sym.Symbol('CD'),
    rho= sym.Symbol('𝜌'),
    Uo= sym.Symbol('Uo'),
    D = sym.Symbol('D')):
    return(sym.solvers.nsolve(
        (0.5*CD*rho*(Uo**2)*D) - FD
        , v
    ))

def solver_impulso_lateral(
    v=1, 
    L = sym.Symbol('L'), 
    Ck = sym.Symbol('Ck'), 
    rho = sym.Symbol('𝜌'), 
    Uo = sym.Symbol('Uo'), 
    D = sym.Symbol('D'), 
    fk = sym.Symbol('fk'),
    t = sym.Symbol('t')):
    return(sym.solvers.nsolve(
        ( Ck * 0.5 * rho * (Uo**2) * D * sym.sin(2 * sym.pi * fk * t) ) - L
        , v
    ))

def solver_coeficiente_amortecimento(
    v=1, 
    CA = sym.Symbol('CA'), 
    m = sym.Symbol('m'),
    delta= sym.Symbol('Δ'),
    rho = sym.Symbol('𝜌'),
    D = sym.Symbol('D')):
    return(sym.solvers.nsolve(
        ((2 * m * delta)/(rho * (D**2))) - CA
        , v
    ))

def solver_velocidade_critica(
    v=1, 
    Vcrit = sym.Symbol('Vcrit'), 
    k = sym.Symbol('k'),
    fn = sym.Symbol('fn'),
    D = sym.Symbol('D')):
    return(sym.solvers.nsolve(
        (k * fn * D) - Vcrit
        , v
    ))

### INTEGRAL COMO FAZER? MASSA EFETIVA
def solver_massa_efetiva(
    v=1, 
    m = sym.Symbol('Vcrit'), 
    k = sym.Symbol('k'),
    fn = sym.Symbol('fn'),
    D = sym.Symbol('D')):
    return(sym.solvers.nsolve(
        (k * fn * D) - m
        , v
    ))

def solver_frequencia_natural(
    v=1, 
    fn = sym.Symbol('fn'),
    k = sym.Symbol('k'),
    l = sym.Symbol('l'),
    E = sym.Symbol('E'),
    I = sym.Symbol('I'),
    m = sym.Symbol('m')):
    return(sym.solvers.nsolve(
        ( (k/(l**2)) * sym.sqrt((E*I)/m) ) - fn
        , v
    ))