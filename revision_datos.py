from carga import cargar_datos

clientes, ventas = cargar_datos()

print("\n--- TAMAÑO DE LAS TABLAS ---")
print("Clientes:", clientes.shape)
print("Ventas:", ventas.shape)

print("\n--- INFORMACIÓN DE CLIENTES ---")
clientes.info()

print("\n--- INFORMACIÓN DE VENTAS ---")
ventas.info()

print("\n--- RESUMEN DE CLIENTES ---")
print(clientes.describe())

print("\n--- RESUMEN DE VENTAS ---")
print(ventas.describe())

def limpiar_ventas(ventas):
    print("\n[ventas] Nulos por columna:")
    print(ventas.isnull().sum())

    print(f"[ventas] Filas duplicadas: {ventas.duplicated().sum()}")

    ventas = _quitar_espacios(ventas)
