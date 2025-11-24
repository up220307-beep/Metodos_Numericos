import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

print("===== MÉTODO DE EULER MEJORADO (HEUN) =====")

print("La ecuación debe ser de la forma dy/dt = f(t,y)")
func_str = input("Ingresa la función f(t,y): ")

t, y = sp.symbols('t y')
f = sp.sympify(func_str)
f_num = sp.lambdify((t, y), f)

t0 = float(input("\nIngresa t0 (inicio): "))
y0 = float(input("Ingresa y0 (valor inicial de y): "))
h = float(input("Ingresa el paso h (ejemplo 0.1): "))
t_end = float(input("Ingresa el valor final del intervalo: "))

ts = np.arange(t0, t_end + h, h)
ys = np.zeros(len(ts))
ys[0] = y0

for i in range(1, len(ts)):
    tn = ts[i-1]
    yn = ys[i-1]
    k1 = f_num(tn, yn)
    y_pred = yn + h * k1                 # predictor (Euler explícito)
    k2 = f_num(tn + h, y_pred)           # slope at predictor
    ys[i] = yn + (h / 2.0) * (k1 + k2)   # corrector (promedio de pendientes)
    print(f"t = {ts[i]:.6g}, y = {ys[i]:.6f}")

# Gráfica de los resultados
plt.figure(figsize=(8,5))
plt.plot(ts, ys, '-o', label='Heun (Euler mejorado)')
plt.xlabel('t')
plt.ylabel('y')
plt.title('Solución numérica por Método de Euler Mejorado (Heun)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

print("\nCálculo terminado.")