# 📚 Recursos Adicionales - Sesión 1

## 🔗 Enlaces Útiles

### Documentación Oficial
- [Tutorial oficial de Python](https://docs.python.org/es/3/tutorial/)
- [Documentación de Python en español](https://docs.python.org/es/3/)
- [Jupyter Notebook Documentation](https://jupyter-notebook.readthedocs.io/)

### Guías de Instalación Detalladas

#### Windows
1. Ir a [python.org/downloads](https://www.python.org/downloads/)
2. Descargar la versión más reciente de Python 3.x
3. **IMPORTANTE**: Marcar "Add Python to PATH" durante la instalación
4. Abrir Command Prompt y verificar: `python --version`

#### macOS
```bash
# Opción 1: Desde python.org
# Descargar e instalar desde https://www.python.org/downloads/

# Opción 2: Usando Homebrew
brew install python

# Verificar instalación
python3 --version
```

#### Linux (Ubuntu/Debian)
```bash
# Actualizar sistema
sudo apt update
sudo apt upgrade

# Instalar Python 3 y pip
sudo apt install python3 python3-pip

# Verificar instalación
python3 --version
```

## 🛠️ Instalación de Jupyter Notebook

Una vez que tengas Python instalado:

```bash
# Instalar Jupyter
pip install jupyter

# Iniciar Jupyter Notebook
jupyter notebook
```

## 📝 Ejercicios Extra

### Ejercicio 1: Mi Primera Variable
```python
# Crea variables con tu información personal
mi_nombre = "Tu nombre aquí"
mi_edad = 0  # Tu edad
mi_ciudad = "Tu ciudad"
mi_profesion = "Tu profesión"

# Muestra la información
print(f"Hola, soy {mi_nombre}")
print(f"Tengo {mi_edad} años")
print(f"Vivo en {mi_ciudad}")
print(f"Trabajo como {mi_profesion}")
```

### Ejercicio 2: Calculadora Simple
```python
# Crea una calculadora que sume dos números
numero1 = float(input("Ingresa el primer número: "))
numero2 = float(input("Ingresa el segundo número: "))

resultado = numero1 + numero2
print(f"La suma de {numero1} + {numero2} = {resultado}")
```

## 🎯 Puntos Clave para Recordar

1. **Python es sensible a mayúsculas y minúsculas**
   - `Variable` ≠ `variable` ≠ `VARIABLE`

2. **La indentación es parte de la sintaxis**
   - Usa 4 espacios por nivel de indentación
   - Sé consistente en todo tu código

3. **Los nombres de variables deben ser descriptivos**
   - ✅ Bueno: `precio_producto`, `edad_usuario`
   - ❌ Malo: `x`, `data`, `temp`

4. **Usa comentarios para explicar el "por qué", no el "qué"**
   - ✅ Bueno: `# Calculamos el descuento del 15% para clientes VIP`
   - ❌ Malo: `# Multiplicamos precio por 0.15`

## 🐛 Errores Comunes y Cómo Solucionarlos

### Error: `NameError: name 'variable' is not defined`
```python
# ❌ Error
print(nombre)  # variable no definida

# ✅ Solución
nombre = "Juan"
print(nombre)
```

### Error: `IndentationError: expected an indented block`
```python
# ❌ Error
if edad >= 18:
print("Mayor de edad")  # Falta indentación

# ✅ Solución
if edad >= 18:
    print("Mayor de edad")  # Correctamente indentado
```

### Error: `TypeError: can't multiply sequence by non-int`
```python
# ❌ Error
numero = "5"
resultado = numero * 2.5  # String * float

# ✅ Solución
numero = 5  # int
# o
numero = int("5")  # Convertir string a int
resultado = numero * 2.5
```

## 📊 Tabla de Tipos de Datos

| Tipo | Python | Ejemplo | Descripción |
|------|--------|---------|-------------|
| Entero | `int` | `42` | Números sin decimales |
| Decimal | `float` | `3.14` | Números con decimales |
| Texto | `str` | `"Hola"` | Cadenas de caracteres |
| Booleano | `bool` | `True` | Verdadero o Falso |
| Nulo | `None` | `None` | Ausencia de valor |

## 🎮 Mini Desafíos

### Desafío 1: Adivina mi Edad
```python
# El usuario debe ingresar su año de nacimiento
# El programa calcula su edad
from datetime import date

anio_nacimiento = int(input("¿En qué año naciste? "))
anio_actual = date.today().year
edad = anio_actual - anio_nacimiento

print(f"Tienes aproximadamente {edad} años")
```

### Desafío 2: Conversor de Monedas
```python
# Programa que convierte pesos a dólares
pesos = float(input("Ingresa la cantidad en pesos: "))
tasa_cambio = 17.5  # Ejemplo: 1 USD = 17.5 MXN

dolares = pesos / tasa_cambio
print(f"${pesos} pesos = ${dolares:.2f} USD")
```

## 📖 Lectura Adicional

- [PEP 8 - Style Guide for Python Code](https://peps.python.org/pep-0008/)
- [Python Naming Conventions](https://peps.python.org/pep-0008/#naming-conventions)
- [The Zen of Python](https://peps.python.org/pep-0020/)

---

¡Practica estos ejercicios para reforzar lo aprendido! 💪