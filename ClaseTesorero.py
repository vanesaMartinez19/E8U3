from  InterfaceTesorero import ITesorero
# Implementación de ITesorero
class Tesorero(ITesorero):
    def __init__(self, agentes):
        self.agentes = agentes

    def gastosSueldoPorEmpleado(self, dni):
        for agente in self.agentes:
            if agente.cuil == dni:
                return agente.calcular_sueldo()
        return 0


