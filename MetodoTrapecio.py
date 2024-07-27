def trapecio_integral(f, a, b, n):
    h = (b - a) / n
    integral_sum = 0
    for i in range(n):
        xi = a + i * h
        integral_sum += h * (f(xi) + f(xi + h)) / 2
    return integral_sum

# Funcion a Evaluar
def funcion_ejemplo(x):
    return x**2  # Cambia la función según tus necesidades

a = 0.0
b = 2.0
num_subintervalos = 4
integral_aproximada = trapecio_integral(funcion_ejemplo, a, b, num_subintervalos)
print("Integral aproximada:", integral_aproximada)
