def calcular_letra_frances(capital, tasa_anual, plazo_meses):
    """
    Calcula la letra de un préstamo según el sistema francés.
    
    :capital: capital prestado
    :tasa_anual: Tasa de interés anual en porcentaje (ej. 5 para 5%)
    :plazo_meses: Plazo del préstamo en meses
    :return: Valor de la cuota mensual
    """

    # Convertir la tasa anual a tasa mensual (en decimal)
    tasa_mensual = (tasa_anual / 100) / 12

    # Calcular la letra usando la fórmula del sistema francés
    
    letra = (capital * tasa_mensual) / (1 - (1 + tasa_mensual) ** -plazo_meses)
   
    return letra

# Ejemplo de uso
capital_prestado = 100000  # Capital en euros
tasa_interes_anual = 5    # Tasa de interés anual en porcentaje
plazo = 240                # Plazo del préstamo en meses (20 años)

letra = calcular_letra_frances(capital_prestado, tasa_interes_anual, plazo)
print(f"La cuota mensual es: {letra:.2f} euros")