import math

def taylor_polinomio(f, a, n, x):
    result = 0
    for k in range(n + 1):
        result += (f(a) / math.factorial(k)) * (x - a) ** k
    return result

# Funcion a evaluar:
def funcion_ejemplo(x):
    return math.cos(x)

x0 = 0.0
grado = 3
valor_evaluado = 0.01
aproximacion = taylor_polinomio(funcion_ejemplo, x0, grado, valor_evaluado)
print("Aproximación:", aproximacion)
