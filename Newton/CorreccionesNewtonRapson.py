import matplotlib.pyplot as plt
import numpy as np
import sympy as sp


# Método 
print("===== MÉTODO DE NEWTON =====")

# Función dada
func_str = input("Ingresa tu función f(x): ")
f = sp.sympify(func_str)

# Coloca tú derivada de la función.
df_str = input("Ingresa la derivada f'(x): ")
df = sp.sympify(df_str)

print("\nFunción ingresada:")
print("f(x) =", f)
print("Derivada ingresada:")
print("f'(x) =", df)

f_num = sp.lambdify(sp.symbols('x'), f)
df_num = sp.lambdify(sp.symbols('x'), df)

# Valor inicial
x0 = float(input("\nIngresa el valor inicial x0: "))
# Valor máximo de iteraciones
max_iter = int(input("Ingresa el número máximo de iteraciones: "))
epsilon = np.finfo(float).eps
x = x0
x_values = [x0]
y_values = [f_num(x0)]

for i in range(max_iter):
        # Derivada en el punto actual
        df_val = df_num(x)

       #Formula
        x_new = x - f_num(x) / df_val

        print(f"Iteración {i+1}: x = {x_new:.15f}")

        # Valores para gráfica
        x_values.append(x_new)
        y_values.append(f_num(x_new))

        # Convergencia
        if abs(f_num(x_new)) < epsilon :
            print( i+1, "iteraciones.")
            print("Raíz aproximada:", x_new)
            break

        x = x_new
        
x_plot = np.linspace(min(x_values) - 1, max(x_values) + 1, 400)
y_plot = [f_num(x) for x in x_plot]

plt.figure(figsize=(10, 6))
plt.plot(x_plot, y_plot, label='f(x)')
plt.scatter(x_values, y_values, color='red', label='Iteraciones')
plt.scatter(x_values[-1], y_values[-1], color='green', label='Raíz aproximada')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Método de Newton')
plt.grid(True)
plt.legend()
plt.show()