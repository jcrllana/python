# Función para obtener una entrada numérica válida entre 0 y 5
def obtener_valoracion(categoria):
    while True:
        try:
            valor = float(input(f"{categoria} (0-5): "))
            if 0 <= valor <= 5:
                return valor
            else:
                print("Por favor, introduce un número entre 0 y 5.")
        except ValueError:
            print("Entrada inválida. Por favor, introduce un número.")

# Función para obtener datos de un profesor
def obtener_datos_profesor():
    nombre = input("Introduce el nombre del profesor: ")
    conocimiento = obtener_valoracion("Nivel de conocimiento en Java")
    experiencia = obtener_valoracion("Años de experiencia en Java")
    comunicacion = obtener_valoracion("Capacidad comunicativa")
    
    # Calcular la puntuación total
    puntuacion = (conocimiento + experiencia + comunicacion) / 3
    
    return {
        "nombre": nombre,
        "conocimiento": conocimiento,
        "experiencia": experiencia,
        "comunicacion": comunicacion,
        "puntuacion": puntuacion
    }

# Obtener datos de los tres profesores
profesores = []
for i in range(3):
    print(f"\nIntroduce los datos del profesor {i+1}:")
    profesor = obtener_datos_profesor()
    profesores.append(profesor)

# Ordenar la lista de profesores por puntuación de mayor a menor
profesores_ordenados = sorted(profesores, key=lambda x: x["puntuacion"], reverse=True)

# Mostrar los resultados ordenados
print("\nLista de profesores ordenada por puntuación (de mayor a menor):")
for profesor in profesores_ordenados:
    print(f"{profesor['nombre']} - Puntuación: {profesor['puntuacion']:.2f}")
