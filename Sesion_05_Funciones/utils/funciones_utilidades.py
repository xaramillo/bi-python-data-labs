# 🛠️ Funciones Utilitarias para Análisis de Datos
# Sesión 5: Funciones - Archivo de utilidades

def limpiar_texto(texto):
    """
    Limpia y formatea texto para análisis de datos
    """
    if not texto:
        return ""
    return texto.strip().title()

def validar_email(email):
    """
    Valida formato básico de email
    """
    return '@' in email and '.' in email.split('@')[1]

def formatear_moneda(cantidad, moneda="$"):
    """
    Formatea números como moneda
    """
    return f"{moneda}{cantidad:,.2f}"

def calcular_estadisticas(datos):
    """
    Calcula estadísticas básicas de una lista de números
    """
    if not datos:
        return None
    
    return {
        'total': sum(datos),
        'promedio': sum(datos) / len(datos),
        'minimo': min(datos),
        'maximo': max(datos),
        'count': len(datos)
    }

def procesar_csv_simple(archivo):
    """
    Procesador simple de archivos CSV
    """
    try:
        with open(archivo, 'r', encoding='utf-8') as file:
            lineas = file.readlines()
            headers = lineas[0].strip().split(',')
            
            datos = []
            for linea in lineas[1:]:
                valores = linea.strip().split(',')
                registro = {headers[i]: valores[i] for i in range(len(headers))}
                datos.append(registro)
            
            return datos
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {archivo}")
        return []

# Ejemplo de uso:
# datos = procesar_csv_simple('datos.csv')
# estadisticas = calcular_estadisticas([1, 2, 3, 4, 5])
# print(formatear_moneda(12500.75))