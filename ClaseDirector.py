from InterfaceDirector import IDirector
rom ClaseDocente import Docente
from ClaseDocenteInvestigador import DocenteInvestigador
from ClaseInvestigador import Investigador
from ClasePersonalApoyo import PersonalDeApoyo
from InterfaceTesorero import ITesorero
from InterfaceDirector import IDirector

# Implementación de IDirector
class Director(IDirector):
    def __init__(self, agentes):
        self.agentes = agentes

    def modificarBasico(self, dni, nuevoBasico):
        for agente in self.agentes:
            if agente.cuil == dni:
                agente.sueldo_basico = nuevoBasico

    def modificarPorcentajeporcargo(self, dni, nuevoPorcentaje):
        for agente in self.agentes:
            if isinstance(agente, Docente) and agente.cuil == dni:
                agente.porcentaje_cargo = nuevoPorcentaje

    def modificarPorcentajeporcategoria(self, dni, nuevoPorcentaje):
        for agente in self.agentes:
            if isinstance(agente, PersonalDeApoyo) and agente.cuil == dni:
                agente.porcentaje_categoria = nuevoPorcentaje

    def modificarImporteExtra(self, dni, nuevoImporteExtra):
        for agente in self.agentes:
            if isinstance(agente, DocenteInvestigador) and agente.cuil == dni:
                agente.importe_extra = nuevoImporteExtra

