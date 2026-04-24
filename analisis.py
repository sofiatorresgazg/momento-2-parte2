from funciones import *

# Cargar archivos de la carpeta raw
productos = cargar_datos('data/raw/productos.csv')
ventas = cargar_datos('data/raw/ventas.csv')

# --- PROCESO DE LIMPIEZA ---
# Limpiar Productos
productos = manejar_nulos(productos)
productos = estandarizar_moda(productos)
productos = limpiar_precios(productos, 'precio')

# Limpiar Ventas
ventas = manejar_nulos(ventas)
ventas = estandarizar_moda(ventas) # Por si hay tallas en ventas

# --- COMBINACIÓN (Merge) ---
# Unimos por 'id_producto' para saber qué se vendió y a qué precio
df_tienda = pd.merge(ventas, productos, on='id_producto', how='inner')

# Guardar los archivos limpios como te pide el proyecto
productos.to_csv('data/processed/productos_limpios.csv', index=False)
ventas.to_csv('data/processed/ventas_limpios.csv', index=False)


print(">>> ANÁLISIS DE TIENDA DE MODA <<<")

# 1. ¿Cuál es la prenda más vendida? (Frecuencia)
prenda_top = df_tienda['nombre_producto'].value_counts().idxmax()
print(f"1. Prenda con más ventas: {prenda_top}")

# 2. ¿Cuánto dinero ingresó por cada categoría (Ej: calzado, superior)? (Agregación)
# Nota: Ingreso = Cantidad vendida * Precio
df_tienda['total_venta'] = df_tienda['cantidad'] * df_tienda['precio']
ingresos_cat = df_tienda.groupby('categoria')['total_venta'].sum()
print(f"\n2. Ingresos por categoría:\n{ingresos_cat}")

# 3. ¿Cuántas ventas fueron de la categoría 'accesorios'? (Filtrado y Conteo)
conteo_accesorios = df_tienda[df_tienda['categoria'] == 'accesorios'].shape[0]
print(f"\n3. Cantidad de transacciones de accesorios: {conteo_accesorios}")