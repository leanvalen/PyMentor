# # --- Módulo de Facturación ---

# def calcular_total_factura(items):
#     """Calcula el total de una factura sumando los precios de los items."""
#     subtotal = sum(item['precio'] for item in items)

#     # Aplicamos el 21% de IVA
#     impuesto = subtotal * 0.21
#     total = subtotal + impuesto

#     print(
#         f"Factura generada. Subtotal: ${subtotal:.2f}, IVA: ${impuesto:.2f}, Total: ${total:.2f}")
#     return total

# # --- Módulo de Catálogo ---


# def obtener_info_producto(producto):
#     """Obtiene una cadena de texto con la información de un producto para el catálogo."""

#     # Necesitamos mostrar el precio final con IVA
#     precio_base = producto['precio']
#     impuesto = precio_base * 0.21
#     precio_final = precio_base + impuesto

#     return f"{producto['nombre']} - Precio Final: ${precio_final:.2f} (IVA incluido)"


# # --- Uso del código ---
# mi_carrito = [{'nombre': 'Tornillo de Acero', 'precio': 100},
#               {'nombre': 'Tuerca', 'precio': 50}]
# mi_producto = {'nombre': 'Martillo de Goma', 'precio': 1200}

# calcular_total_factura(mi_carrito)
# print(obtener_info_producto(mi_producto))
# --- Módulo de Utilidades de Finanzas (Nuestra "Especificación Maestra") ---

IVA_TASA = 0.21  # ¡La única fuente de verdad!


def calcular_monto_con_iva(monto_base):
    """Calcula un monto final aplicando la tasa de IVA vigente."""
    impuesto = monto_base * IVA_TASA
    return monto_base + impuesto

# --- Módulo de Facturación (Refactorizado) ---


def calcular_total_factura(items):
    """Calcula el total de una factura sumando los precios de los items."""
    subtotal = sum(item['precio'] for item in items)

    # Usamos nuestra función centralizada
    total = calcular_monto_con_iva(subtotal)

    # (Para el desglose, podríamos incluso mejorar esto más, pero centrémonos en el total)
    print(f"Factura generada. Total a pagar: ${total:.2f}")
    return total

# --- Módulo de Catálogo (Refactorizado) ---


def obtener_info_producto(producto):
    """Obtiene una cadena de texto con la información de un producto para el catálogo."""

    # Usamos nuestra función centralizada
    precio_final = calcular_monto_con_iva(producto['precio'])

    return f"{producto['nombre']} - Precio Final: ${precio_final:.2f} (IVA incluido)"


# --- Uso del código ---
mi_carrito = [{'nombre': 'Tornillo de Acero', 'precio': 100},
              {'nombre': 'Tuerca', 'precio': 50}]
mi_producto = {'nombre': 'Martillo de Goma', 'precio': 1200}

calcular_total_factura(mi_carrito)
print(obtener_info_producto(mi_producto))
