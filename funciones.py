import pandas as pd

def cargar_datos(ruta):
    return pd.read_csv(ruta)

def limpiar_nulos(df):
    return df.dropna()

def estandarizar_texto(df, columna):
   
    df[columna] = df[columna].astype(str).str.lower().str.strip()
    return df