import geopy.distance
import datetime

def obtener_coordenadas(ciudad):
    # Diccionario de coordenadas de algunas ciudades de Chile y Argentina
    ciudades = {
        'Santiago': (-33.4489, -70.6693),
        'Buenos Aires': (-34.6037, -58.3816),
        'Valparaíso': (-33.0472, -71.6127),
        'Mendoza': (-32.8894, -68.8458),
        'La Serena': (-29.9045, -71.2489),
        'Córdoba': (-31.4201, -64.1888),
        'Concepción': (-36.827, -73.0503),
        'Rosario': (-32.9468, -60.6393)
    }
    return ciudades.get(ciudad, None)

def calcular_distancia(coord1, coord2):
    return geopy.distance.geodesic(coord1, coord2).km

def obtener_duracion(distancia, medio_transporte):
    velocidades = {
        'auto': 80, # km/h
        'bus': 60, # km/h
        'tren': 100, # km/h
        'avión': 800 # km/h
    }
    velocidad = velocidades.get(medio_transporte, 0)
    if velocidad == 0:
        return None
    horas = distancia / velocidad
    return datetime.timedelta(hours=horas)

def mostrar_narrativa(ciudad_origen, ciudad_destino, distancia_km, duracion, medio_transporte):
    distancia_millas = distancia_km * 0.621371
    print(f"\nNarrativa del viaje desde {ciudad_origen} hasta {ciudad_destino}:")
    print(f"Distancia: {distancia_km:.2f} km / {distancia_millas:.2f} millas")
    print(f"Medio de transporte: {medio_transporte.capitalize()}")
    print(f"Duración estimada del viaje: {duracion}")

def main():
    while True:
        ciudad_origen = input("Ciudad de Origen (o 's' para salir): ")
        if ciudad_origen.lower() == 's':
            break
        ciudad_destino = input("Ciudad de Destino: ")
        if ciudad_destino.lower() == 's':
            break
        
        coord_origen = obtener_coordenadas(ciudad_origen)
        coord_destino = obtener_coordenadas(ciudad_destino)
        
        if not coord_origen or not coord_destino:
            print("Una o ambas ciudades no están en la base de datos. Intenta de nuevo.")
            continue
        
        distancia_km = calcular_distancia(coord_origen, coord_destino)
        
        print("Medios de transporte disponibles: auto, bus, tren, avión")
        medio_transporte = input("Elige el medio de transporte: ").lower()
        
        duracion = obtener_duracion(distancia_km, medio_transporte)
        if duracion is None:
            print("Medio de transporte no válido. Intenta de nuevo.")
            continue
        
        mostrar_narrativa(ciudad_origen, ciudad_destino, distancia_km, duracion, medio_transporte)

if __name__ == "__main__":
    main()

