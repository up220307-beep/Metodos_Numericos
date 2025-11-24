import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

# Título del programa para que el usuario sepa qué método se está usando
print("===== MÉTODO DE EULER MEJORADO (HEUN) =====")

# Explicamos al usuario qué forma debe tener la ecuación diferencial
print("La ecuación debe ser de la forma dy/dt = f(t,y)")

# Pedimos al usuario que ingrese la función como texto (ej: "t + y")
func_str = input("Ingresa la función f(t,y): ")

# Creamos variables simbólicas 't' e 'y' para trabajar con sympy
t, y = sp.symbols('t y')

# Convertimos el texto ingresado en una expresión matemática simbólica
f = sp.sympify(func_str)

# Convertimos la expresión simbólica en una función numérica que podamos evaluar
f_num = sp.lambdify((t, y), f)

# Pedimos al usuario los parámetros iniciales
t0 = float(input("\nIngresa t0 (inicio): "))  # Condición inicial de t
y0 = float(input("Ingresa y0 (valor inicial de y): "))  # Condición inicial de y
h = float(input("Ingresa el paso h (ejemplo 0.1): "))  # Tamaño del paso
t_end = float(input("Ingresa el valor final del intervalo: "))  # Límite superior de t

# Creamos un array con los valores de t desde t0 hasta t_end con paso h
ts = np.arange(t0, t_end + h, h)
# Inicializamos el array para almacenar los valores de y
ys = np.zeros(len(ts))
# Asignamos la condición inicial y0
ys[0] = y0

# Iteramos desde el segundo punto hasta el final
for i in range(1, len(ts)):
    tn = ts[i-1]  # Valor actual de t
    yn = ys[i-1]  # Valor actual de y
    k1 = f_num(tn, yn)  # Primera pendiente (en el punto actual)
    y_pred = yn + h * k1  # Predictor: estimación con Euler explícito
    k2 = f_num(tn + h, y_pred)  # Segunda pendiente (en el punto predictor)
    ys[i] = yn + (h / 2.0) * (k1 + k2)  # Corrector: promedio ponderado de pendientes
    print(f"t = {ts[i]:.6g}, y = {ys[i]:.6f}")

# Gráfica de los resultados
plt.figure(figsize=(8,5))  # Crear figura con tamaño específico
plt.plot(ts, ys, '-o', label='Heun (Euler mejorado)')  # Graficar solución
plt.xlabel('t')  # Etiqueta eje x
plt.ylabel('y')  # Etiqueta eje y
plt.title('Solución numérica por Método de Euler Mejorado (Heun)')  # Título
plt.grid(True)  # Mostrar grilla
plt.legend()  # Mostrar leyenda
plt.tight_layout()  # Ajustar márgenes
plt.show()  # Mostrar gráfica

print("\nCálculo terminado.")  # Mensaje final