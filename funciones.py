import pandas as pd

def cargar_datos(ruta):
    return pd.read_csv(ruta)

def manejar_nulos(df):
    # Eliminar filas donde el ID del producto o de venta sea nulo (no nos sirven)
    df = df.dropna(subset=[df.columns[0]]) 
    # Rellenar otros nulos con "Sin especificar" para texto o 0 para números
    df = df.fillna({'categoria': 'general', 'color': 'n/a', 'precio': 0, 'cantidad': 0})
    return df

def estandarizar_moda(df):
    """Limpia columnas de texto para una tienda de moda"""
    columnas_texto = ['nombre_producto', 'categoria', 'color', 'talla']
    for col in columnas_texto:
        if col in df.columns:
            df[col] = df[col].astype(str).str.lower().str.strip()
    return df

def limpiar_precios(df, columna='precio'):
    """Quita el signo $ y convierte a número decimal"""
    if columna in df.columns:
        df[columna] = df[columna].replace({'\$': '', ',': ''}, regex=True)
        df[columna] = pd.to_numeric(df[columna], errors='coerce')
    return df