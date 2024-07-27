# Metodo de biseccion
def bisection_metodo(f, a, b, tol, max_iter):
    if f(a) * f(b) >= 0:
        raise ValueError("La función no cumple con el teorema de Bolzano en el intervalo dado.")

    for i in range(max_iter):
        c = (a + b) / 2
        if abs(f(c)) < tol:
            return c
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c

    raise ValueError("No se alcanzó la convergencia después de {} iteraciones.".format(max_iter))

# Funcion a evaluar
def funcion_ejemplo(x):
    return x**2 - 4

a = 1.0
b = 3.0
raiz_aproximada = bisection_metodo(funcion_ejemplo, a, b,1e-6,100)
print("Raíz aproximada:", raiz_aproximada)
