
## README — Uso sencillo de newton.py

Resumen
- Archivo: newton.py (en el mismo directorio).
- Propósito: encontrar raíces de funciones reales usando el método de Newton (Newton–Raphson).

Requisitos
- Python 3.x
- (Opcional) sympy para derivadas simbólicas: pip install sympy

Cómo usar (recomendado: como módulo)
1. Abra newton.py para verificar la firma exacta de la(s) función(es) exportada(s). Un uso típico es:
    - newton(f, df, x0, tol=1e-8, max_iter=50)

2. Ejemplo mínimo:
```python
from newton import newton  # ajustar según la exportación real

def f(x):
     return x**3 - 2*x - 5

def df(x):
     return 3*x**2 - 2

root = newton(f, df, x0=2.0, tol=1e-8, max_iter=50)
print("Raíz aproximada:", root)
```

3. Obtener la derivada automáticamente (opcional, usando sympy):
```python
import sympy as sp
from newton import newton

x = sp.symbols('x')
expr = x**3 - 2*x - 5
f = sp.lambdify(x, expr, 'math')
df = sp.lambdify(x, sp.diff(expr, x), 'math')

root = newton(f, df, x0=2.0)
```

Uso como script (si está implementado)
- Si newton.py acepta argumentos CLI, un ejemplo posible:
```bash
python newton.py --func "x**3-2*x-5" --x0 2 --tol 1e-8 --max-iter 50
```
Abra el archivo para ver las opciones exactas de línea de comandos.

Consejos prácticos
- Elegir x0 cercano a la raíz esperada mejora convergencia.
- Si la derivada se anula o es muy pequeña en iteraciones, el método puede fallar; pruebe otro x0 o método alternativo.
- Ajuste tol y max_iter según precisión y costos computacionales.

Salida esperada
- Un número (raíz aproximada) o una tupla con información adicional (iteraciones, convergencia). Verifique la implementación exacta en newton.py.

Contacto / mantenimiento
- Para modificar o extender, edite newton.py: añada comprobaciones de errores, manejo de excepciones y tests unitarios.

Fin.