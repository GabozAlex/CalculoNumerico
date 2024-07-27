def riemann_integral(f, a, b, n):
    h = (b - a) / n
    integral_sum = 0
    for i in range(n):
        xi = a + i * h
        integral_sum += h * f(xi)
    return integral_sum

# Funciona a evaluar
def funcion_ejemplo(x):
    return x**2

a = 0.0
b = 2.0
num_subintervalos = 100
integral_aproximada = riemann_integral(funcion_ejemplo, a, b, num_subintervalos)
print("Integral aproximada:", integral_aproximada)
