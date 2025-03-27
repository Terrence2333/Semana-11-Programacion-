def calcular_descuento(monto_total, porcentaje_descuento=25):
    """
    Función para calcular el descuento basado en el monto total y el porcentaje de descuento.

    Parámetros:
        monto_total (float): El monto total de la compra.
        porcentaje_descuento (float, opcional): El porcentaje de descuento. Por defecto es 35%.

    Retorna:
        float: El monto del descuento calculado.
    """
    descuento = (monto_total * porcentaje_descuento) / 100
    return descuento


def calcular_monto_final(monto_total, descuento):
    """
    Función para calcular el monto final a pagar después de aplicar el descuento.

    Parámetros:
        monto_total (float): El monto total de la compra.
        descuento (float): El monto del descuento calculado.

    Retorna:
        float: El monto final a pagar después del descuento.
    """
    return monto_total - descuento


def mostrar_resultados(monto_total, descuento, monto_final, porcentaje_descuento, nombre_empresa):
    """
    Función para mostrar los resultados del cálculo de descuento y el monto final.

    Parámetros:
        monto_total (float): El monto total de la compra.
        descuento (float): El monto del descuento calculado.
        monto_final (float): El monto final después de aplicar el descuento.
        porcentaje_descuento (float): El porcentaje de descuento aplicado.
        nombre_empresa (str): El nombre de la empresa.
        nombre_ciudad (str): El nombre de la ciudad de la empresa.
    """
    print(f"Empresa: {nombre_empresa}")
    print(f"ciudad: {"nombre_ciudad-Quito"}")
    print(f"Compra de {monto_total:.2f} con un descuento de {descuento:.2f} ({porcentaje_descuento}%).")
    print(f"Monto final a pagar después del descuento: {monto_final:.2f}\n")


def ejecutar_calculos():
    """
    Función principal para ejecutar los cálculos y mostrar los resultados para diferentes valores.
    """
    # Lista de compras de diferentes clientes o productos
    compras = [
        {"monto_total": 1500, "porcentaje_descuento": 35},
        {"monto_total": 2000, "porcentaje_descuento": 35},
        {"monto_total": 750, "porcentaje_descuento": 35},
        {"monto_total": 1200, "porcentaje_descuento": 35},
        {"monto_total": 3000, "porcentaje_descuento": 35},
        {"monto_total": 4500, "porcentaje_descuento": 35},
        {"monto_total": 2500, "porcentaje_descuento": 35},
        {"monto_total": 3200, "porcentaje_descuento": 35},
        {"monto_total": 500, "porcentaje_descuento": 35},
        {"monto_total": 10000, "porcentaje_descuento": 35},
        {"monto_total": 1200, "porcentaje_descuento": 35},
        {"monto_total": 1800, "porcentaje_descuento": 35},
        {"monto_total": 3500, "porcentaje_descuento": 35},
        {"monto_total": 4100, "porcentaje_descuento": 35},
        {"monto_total": 6000, "porcentaje_descuento": 35},
        {"monto_total": 2200, "porcentaje_descuento": 35},
        {"monto_total": 9500, "porcentaje_descuento": 35},
        {"monto_total": 4800, "porcentaje_descuento": 35},
        {"monto_total": 5500, "porcentaje_descuento": 35},
        {"monto_total": 3200, "porcentaje_descuento": 35},
        {"monto_total": 11500, "porcentaje_descuento": 35},
        {"monto_total": 23500, "porcentaje_descuento": 35},
        {"monto_total": 25300, "porcentaje_descuento": 35},
        {"monto_total": 25500, "porcentaje_descuento": 35},
        {"monto_total": 25100, "porcentaje_descuento": 35},
        {"monto_total": 23500, "porcentaje_descuento": 35},
        {"monto_total": 25700, "porcentaje_descuento": 35},
        {"monto_total": 25900, "porcentaje_descuento": 35},
        {"monto_total": 25000, "porcentaje_descuento": 35},
        {"monto_total": 255500, "porcentaje_descuento": 35}
    ]

    # Nombre de la empresa
    nombre_empresa = "Mancontwwordlservi S.A ferrisariato S.A MarglobalS.A."



    # nombre de la ciudad de la empresa
    "Quito Guayaquil Miami."

    # Iteramos a través de las compras y mostramos los resultados
    for compra in compras:
        monto_total = compra["monto_total"]
        porcentaje_descuento = compra["porcentaje_descuento"]

        # Calcular el descuento y monto final
        descuento = calcular_descuento(monto_total, porcentaje_descuento)
        monto_final = calcular_monto_final(monto_total, descuento)

        # Mostrar los resultados
        mostrar_resultados(monto_total, descuento, monto_final, porcentaje_descuento, nombre_empresa)


# Llamada a la función principal para ejecutar los cálculos
ejecutar_calculos()
