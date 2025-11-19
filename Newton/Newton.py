import sympy as sp

print("===== MÉTODO DE NEWTON–RAPHSON =====")

# Pedimos al usuario una función en formato simbólico (por ejemplo: x**3 - 2*x - 5)
# sympify convierte la cadena ingresada en una expresión de SymPy
func_str = input("Ingresa tu función f(x): ")
f = sp.sympify(func_str)

# Calculamos la derivada simbólica de f respecto a x
# Esto evita que el usuario tenga que derivar a mano
df = sp.diff(f, 'x')

print("\nLa derivada calculada automáticamente es:")
print("f'(x) =", df)

# Convertimos las expresiones simbólicas a funciones numéricas evaluables,
# para poder usarlas con valores en coma flotante durante las iteraciones
f_num = sp.lambdify(sp.symbols('x'), f)
df_num = sp.lambdify(sp.symbols('x'), df)

# Pedimos los datos necesarios para el método:
# x0: aproximación inicial, tol: tolerancia para la parada, max_iter: tope de iteraciones
x0 = float(input("\nIngresa el valor inicial x0: "))
tol = float(input("Ingresa la tolerancia (ejemplo 1e-6): "))
max_iter = int(input("Ingresa el número máximo de iteraciones: "))

x = x0
for i in range(max_iter):
    # Evaluamos la derivada y evitamos dividir por cero
    df_val = df_num(x)
    # Si la derivada es cero o muy pequeña, intentamos aproximarla por diferencias finitas
    if df_val == 0 or abs(df_val) < 1e-12:
        delta = 1e-6
        # aproximación central de la derivada
        df_approx = (f_num(x + delta) - f_num(x - delta)) / (2 * delta)
        if abs(df_approx) < 1e-15:
            print(f"\nDerivada nula o muy pequeña en x = {x}; no se puede continuar.")
            break
        else:
            df_used = df_approx
            print(f"Derivada original muy pequeña en x = {x}; usando aproximación por diferencia finita.")
    else:
        df_used = df_val

    # Paso de Newton: nueva aproximación = antigua - f(x)/f'(x)
    x_new = x - f_num(x) / df_used

    # Mostramos el resultado de esta iteración
    print(f"Iteración {i+1}: x = {x_new}")

    # Si la diferencia entre aproximaciones consecutivas es menor que la tolerancia,
    # consideramos que se ha alcanzado la convergencia
    if abs(x_new - x) < tol:
        print("\nCONVERGIÓ!")
        print("Raíz aproximada:", x_new)
        print("Iteraciones utilizadas:", i+1)
        break

    x = x_new
else:
    # Este mensaje solo se muestra si no se alcanzó convergencia en las iteraciones
    print("El método NO convergió dentro del límite de iteraciones.")