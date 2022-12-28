import sympy as sym

x = sym.Symbol('x')

sym.solve(sym.tan(x) - sym.tanh(x), x)