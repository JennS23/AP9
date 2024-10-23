import math
from collections import Counter

class DatosMeteorologicos:
    def __init__(self, nombre_archivo: str):
        self.nombre_archivo = nombre_archivo
    
    def _direccion_a_grados(self, direccion):
        direcciones = {
            'N': 0, 'NNE': 22.5, 'NE': 45, 'ENE': 67.5,
            'E': 90, 'ESE': 112.5, 'SE': 135, 'SSE': 157.5,
            'S': 180, 'SSW': 202.5, 'SW': 225, 'WSW': 247.5,
            'W': 270, 'WNW': 292.5, 'NW': 315, 'NNW': 337.5
        }
        return direcciones[direccion]
    
    def _grados_a_direccion(self, grados):
        direcciones = [
            (0, 'N'), (22.5, 'NNE'), (45, 'NE'), (67.5, 'ENE'),
            (90, 'E'), (112.5, 'ESE'), (135, 'SE'), (157.5, 'SSE'),
            (180, 'S'), (202.5, 'SSW'), (225, 'SW'), (247.5, 'WSW'),
            (270, 'W'), (292.5, 'WNW'), (315, 'NW'), (337.5, 'NNW')
        ]
        return min(direcciones, key=lambda x: abs(x[0] - grados))[1]
    
    def procesar_datos(self):
        temperaturas = []
        humedades = []
        presiones = []
        velocidades_viento = []
        direcciones_viento = []

        with open(self.nombre_archivo, 'r') as archivo:
            for linea in archivo:
                if linea.strip():
                    partes = linea.split()
                    temperatura = float(partes[11].strip(','))
                    humedad = float(partes[13].strip(','))
                    presion = float(partes[15].strip(','))
                    velocidad_viento = float(partes[17].split(',')[0])
                    direccion_viento = partes[17].split(',')[1].strip()
                    temperaturas.append(temperatura)
                    humedades.append(humedad)
                    presiones.append(presion)
                    velocidades_viento.append(velocidad_viento)
                    direcciones_viento.append(direccion_viento)

        temp_promedio = sum(temperaturas) / len(temperaturas)
        humedad_promedio = sum(humedades) / len(humedades)
        presion_promedio = sum(presiones) / len(presiones)
        velocidad_viento_promedio = sum(velocidades_viento) / len(velocidades_viento)
        grados_viento = [self._direccion_a_grados(d) for d in direcciones_viento]
        promedio_grados = sum(grados_viento) / len(grados_viento)
        direccion_predominante = self._grados_a_direccion(promedio_grados)

        return (temp_promedio, humedad_promedio, presion_promedio, velocidad_viento_promedio, direccion_predominante)

