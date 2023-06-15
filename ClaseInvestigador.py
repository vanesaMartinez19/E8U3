class Investigador(AgenteUniversitario):
    def __init__(self, cuil, apellido, nombre, sueldo_basico, antiguedad, area_investigacion, tipo_investigacion):
        super().__init__(cuil, apellido, nombre, sueldo_basico, antiguedad)
        self.area_investigacion = area_investigacion
        self.tipo_investigacion = tipo_investigacion

    def calcular_sueldo(self):
        return self.sueldo_basico + (self.antiguedad * self.sueldo_basico)

