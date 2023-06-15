from abc import ABC, abstractmethod
import json


# Clase base AgenteUniversitario
class AgenteUniversitario(ABC):
    def __init__(self, cuil, apellido, nombre, sueldo_basico, antiguedad):
        self.cuil = cuil
        self.apellido = apellido
        self.nombre = nombre
        self.sueldo_basico = sueldo_basico
        self.antiguedad = antiguedad

    @abstractmethod
    def calcular_sueldo(self):
        pass









# Clase Investigador

# Clase DocenteInvestigador



# Interfaz IDirector


