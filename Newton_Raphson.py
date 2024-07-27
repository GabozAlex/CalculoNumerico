def my_newton(f, df, x0, tol):
    while abs(f(x0)) > tol:
        x0 -= f(x0) / df(x0)
    return x0

# Funcion a evaluar
def funcion_ejemplo(x):
    return x**2 - 4
# Derivada de la funcion
def derivada_funcion_ejemplo(x):
    return 2*x

x0 = 1.4
tolerancia = 1e-6
raiz_aproximada = my_newton(funcion_ejemplo, derivada_funcion_ejemplo, x0, tolerancia)

print("Raíz aproximada:", raiz_aproximada)
