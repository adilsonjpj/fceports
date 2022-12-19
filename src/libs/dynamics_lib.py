import sympy as sym


# modos de vibracao das estacas/vigas
def solver_engastada_engastada(L, mL, superior, inferior):
    # Declaro a variavel xss
    x = sym.Symbol('x')
    # Obtenho o valor de alpha
    alpha = sym.Symbol('alpha')
    alpha = sym.solvers.nsolve(((sym.cosh(alpha*L) * sym.cos(alpha*L)) - 1), 1)
    print('alpha = ' + str(alpha))
    # Definindo as expressoes para integralas depois 
    k_engastada_engastada = (sym.cos(alpha*L) - sym.cosh(alpha*L))/(sym.sin(alpha*L) - sym.sinh(alpha*L))
    engastada_engastada = sym.cosh(alpha*x) - sym.cos(alpha*x) - (k_engastada_engastada*(sym.sinh(alpha*x) - sym.sin(alpha*x)))
    # integrando as parcelas e dividindo, obtendo assim a massa efetiva
    massa_efetiva_engastada = (sym.integrate(mL * engastada_engastada**2, (x, 0, superior)))/(sym.integrate(engastada_engastada**2, (x, 0, inferior)))
    return(round(massa_efetiva_engastada,3))

def solver_engastada_apoiada(L, mL, superior, inferior):
    # Declaro a variavel xss
    x = sym.Symbol('x')
    # Obtenho o valor de alpha
    beta = sym.Symbol('beta')
    beta = sym.solvers.nsolve((sym.tanh(beta*L) - sym.tan(beta*L)), 1)
    print('beta = ' + str(beta))
    # Definindo as expressoes para integralas depois
    k_engastada_apoiada = (sym.sinh(beta*L) + sym.sin(beta*L))/(sym.cosh(beta*L) + sym.cos(beta*L))
    engastada_apoiada = sym.sinh(beta*x) - sym.sin(beta*x) - (k_engastada_apoiada*(sym.cosh(beta*x) - sym.cos(beta*x)))
    # integrando as parcelas e dividindo, obtendo assim a massa efetiva
    massa_efetiva_apoiada = (sym.integrate(mL * engastada_apoiada**2, (x, 0, superior)))/(sym.integrate(engastada_apoiada**2, (x, 0, inferior)))
    return(round(massa_efetiva_apoiada,3))

def solver_engastada_livre(L, mL, superior, inferior):
    # Declaro a variavel xss
    x = sym.Symbol('x')
    # Obtenho o valor de alpha
    gamma = sym.Symbol('gamma')
    gamma = sym.solvers.nsolve(((sym.cosh(gamma*L) * sym.cos(gamma*L)) + 1), 1)
    print('gamma = ' + str(gamma))
    # Definindo as expressoes para integralas depois
    k_engastada_livre = (sym.cos(gamma*L) + sym.cosh(gamma*L))/(sym.sin(gamma*L) + sym.sinh(gamma*L))
    engastada_livre = sym.cosh(gamma*x) - sym.cos(gamma*x) - (k_engastada_livre*(sym.sinh(gamma*x) - sym.sin(gamma*x)))
    # integrando as parcelas e dividindo, obtendo assim a massa efetiva
    massa_efetiva_livre = (sym.integrate(mL * engastada_livre**2, (x, 0, superior)))/(sym.integrate(engastada_livre**2, (x, 0, inferior)))
    return(round(massa_efetiva_livre,3))
