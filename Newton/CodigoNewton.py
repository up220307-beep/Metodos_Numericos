import sympy as sp

print("===== MÉTODO DE NEWTON–RAPHSON =====")

func_str = input("Ingresa tu función f(x): ")
f = sp.sympify(func_str)

df = sp.diff(f, 'x')

print("\nLa derivada calculada automáticamente es:")
print("f'(x) =", df)

f_num = sp.lambdify(sp.symbols('x'), f)
df_num = sp.lambdify(sp.symbols('x'), df)

x0 = float(input("\nIngresa el valor inicial x0: "))
tol = float(input("Ingresa la tolerancia (ejemplo 1e-6): "))
max_iter = int(input("Ingresa el número máximo de iteraciones: "))

x = x0
for i in range(max_iter):
    df_val = df_num(x)
    if df_val == 0 or abs(df_val) < 1e-12:
        delta = 1e-6
        df_approx = (f_num(x + delta) - f_num(x - delta)) / (2 * delta)
        if abs(df_approx) < 1e-15:
            print(f"\nDerivada nula o muy pequeña en x = {x}; no se puede continuar.")
            break
        else:
            df_used = df_approx
            print(f"Derivada original muy pequeña en x = {x}; usando aproximación por diferencia finita.")
    else:
        df_used = df_val

    x_new = x - f_num(x) / df_used

    print(f"Iteración {i+1}: x = {x_new}")

    if abs(x_new - x) < tol:
        print("\nCONVERGIÓ!")
        print("Raíz aproximada:", x_new)
        print("Iteraciones utilizadas:", i+1)
        break
    x = x_new
else:
    print("El método NO convergió dentro del límite de iteraciones.")
    