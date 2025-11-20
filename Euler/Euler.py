import numpy as np

print("===== MÉTODO DE EULER =====")

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
    ys[i] = ys[i-1] + h * f_num(ts[i-1], ys[i-1])
    print(f"t = {ts[i]:.3f}, y = {ys[i]:.6f}")

print("\nCálculo terminado.")