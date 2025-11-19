import sympy as sp

print("===== MÉTODO DE NEWTON–RAPHSON =====")

# El usuario coloca su función
func_str = input("Ingresa tu función f(x): ")
f = sp.sympify(func_str)

# Se calcula la derivada automáticamente
df = sp.diff(f, 'x')

print("\nLa derivada calculada automáticamente es:")
print("f'(x) =", df)

# Conversión a funciones evaluables
f_num = sp.lambdify(sp.symbols('x'), f)
df_num = sp.lambdify(sp.symbols('x'), df)

# Datos del usuario
x0 = float(input("\nIngresa el valor inicial x0: "))
tol = float(input("Ingresa la tolerancia (ejemplo 1e-6): "))
max_iter = int(input("Ingresa el número máximo de iteraciones: "))

x = x0
for i in range(max_iter):
    x_new = x - f_num(x)/df_num(x)

    print(f"Iteración {i+1}: x = {x_new}")

    if abs(x_new - x) < tol:
        print("\nCONVERGIÓ!")
        print("Raíz aproximada:", x_new)
        print("Iteraciones utilizadas:", i+1)
        break

    x = x_new
else:
    print("El método NO convergió dentro del límite de iteraciones.")