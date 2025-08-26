# 🎯 Ejercicios - Sesión 2: Variables y Tipos de Datos

## Ejercicio 1: Calculadora de Conversiones
Crea un programa que convierta entre diferentes unidades:

```python
# TODO: Implementa conversores para:
# - Temperatura (C°, F°, K)
# - Peso (kg, lb, oz)
# - Distancia (m, km, mi, ft)

temperatura_celsius = 25
# Convertir a Fahrenheit y Kelvin
# Mostrar resultado formateado
```

## Ejercicio 2: Validador de Datos Personales
Valida y limpia información personal:

```python
# Datos de entrada "sucios"
datos_persona = {
    "nombre": "  JUAN CARLOS pérez-lópez  ",
    "email": "  Juan.PEREZ@Gmail.Com  ",
    "telefono": "+52 (555) 123-4567",
    "edad": "28",
    "salario": "$45,750.50"
}

# TODO: Limpia y valida cada campo
# Presenta un reporte profesional
```

## Ejercicio 3: Analizador de Texto
Analiza un texto y extrae estadísticas:

```python
texto = "Python es un lenguaje de programación muy versátil y poderoso para análisis de datos."

# TODO: Calcula:
# - Número de caracteres
# - Número de palabras
# - Palabra más larga
# - Número de vocales y consonantes
# - Convierte a diferentes formatos
```

## Ejercicio 4: Sistema de Inventario
Gestiona productos con diferentes tipos de datos:

```python
productos = [
    "Laptop,Dell XPS,15999.99,5,Electrónicos",
    "Mouse,Logitech,299.50,50,Accesorios",
    "Teclado,Mecánico,899.00,12,Accesorios"
]

# TODO: Procesa cada producto
# Calcula totales, promedios
# Identifica productos con stock bajo
```

## Ejercicio 5: Formateador de Reportes
Crea reportes profesionales:

```python
ventas_mensuales = [15000, 18500, 22000, 19750, 25000]
vendedores = ["Ana", "Carlos", "María", "Luis", "Pedro"]

# TODO: Crea un reporte que incluya:
# - Tabla formateada
# - Estadísticas (promedio, máximo, mínimo)
# - Porcentajes de participación
# - Formato monetario correcto
```

## Ejercicio 6: Limpiador de CSV
Procesa datos como si vinieran de un archivo CSV:

```python
datos_csv = [
    "ID,Nombre,Email,Teléfono,Edad,Activo",
    "1,  MARÍA GARCÍA  ,maria@empresa.com,555-1234,25,TRUE",
    "2,juan pérez,juan.empresa.com,123456789,30,1",
    "3,ANA TORRES,,555-9876,28,FALSE"
]

# TODO: 
# - Separa headers de datos
# - Limpia cada campo
# - Valida información
# - Maneja datos faltantes
# - Genera reporte de calidad
```

## Ejercicio Avanzado: Calculadora Financiera
Sistema completo de cálculos financieros:

```python
# Datos del préstamo
principal = "250000"      # Monto del préstamo
tasa_anual = "8.5"        # Tasa de interés anual %
años = "15"               # Años del préstamo

# TODO: Calcula:
# - Pago mensual
# - Total a pagar
# - Total de intereses
# - Tabla de amortización (primeros 12 meses)
# - Presenta todo en formato profesional
```

## Desafío Final: Procesador de Datos de Empleados
Sistema completo de gestión:

```python
empleados_datos = [
    "1001,MARÍA JOSÉ GARCÍA LÓPEZ,25,Analista,45000.50,maria.garcia@empresa.com,555-1234,TRUE",
    "1002,carlos lópez rodríguez,30,Desarrollador,55000,carlos@empresa.com,555-5678,1",
    "1003,Ana Torres Silva,28,Diseñadora,48000.75,ana.torres@empresa.com,555-9012,FALSE",
    "1004,LUIS FERNANDO CHEN WU,32,Gerente,65000,luis.chen@empresa.com,555-3456,TRUE"
]

# TODO: Crea un sistema que:
# 1. Parse y valide todos los datos
# 2. Limpie nombres, emails, teléfonos
# 3. Calcule estadísticas salariales
# 4. Genere reporte por departamento
# 5. Identifique empleados activos/inactivos
# 6. Presente todo profesionalmente
```

## Criterios de Evaluación:
- ✅ Código limpio y comentado
- ✅ Validación robusta de datos
- ✅ Manejo de errores
- ✅ Formateo profesional
- ✅ Nomenclatura correcta de variables
- ✅ Uso eficiente de tipos de datos

## Tips para Resolver:
1. Siempre valida los datos antes de procesarlos
2. Usa nombres de variables descriptivos
3. Formatea números con comas y decimales apropiados
4. Maneja casos edge (datos vacíos, nulos, etc.)
5. Presenta resultados de manera clara y profesional