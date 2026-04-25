from funciones import cargar_datos, limpiar_nulos, estandarizar_texto
import pandas as pd

df_ventas = cargar_datos('data/raw/ventas.csv')
df_productos = cargar_datos('data/raw/productos.csv')

df_ventas.columns = df_ventas.columns.str.strip().str.lower()
df_productos.columns = df_productos.columns.str.strip().str.lower()

df_ventas = limpiar_nulos(df_ventas)

col_pago = [c for c in df_ventas.columns if 'metodo' in c or 'pago' in c][0]
df_ventas = estandarizar_texto(df_ventas, col_pago)

df_productos = limpiar_nulos(df_productos)


col_v = [c for c in df_ventas.columns if 'producto' in c][0]
col_p = [c for c in df_productos.columns if 'producto' in c or c == 'id'][0]

df_final = pd.merge(df_ventas, df_productos, left_on=col_v, right_on=col_p)

print("\n" + "="*30)
print("   ANALISIS COMPLETADO")
print("="*30)

if not df_final.empty:

    col_cant = 'cantidad_x' if 'cantidad_x' in df_final.columns else 'cantidad'
    col_nom = 'nombre' if 'nombre' in df_final.columns else col_p
    
    top = df_final.groupby(col_nom)[col_cant].sum().idxmax()
    print(f"Producto estrella: {top}")

    nequi = df_final[df_final[col_pago] == 'nequi'].shape[0]
    print(f"Ventas por Nequi: {nequi}")
else:
    print("Error: Los datos no coinciden entre los archivos.")

print("="*30 + "\n")