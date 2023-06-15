class PersonalDeApoyo(AgenteUniversitario):
    def __init__(self, cuil, apellido, nombre, sueldo_basico, antiguedad, categoria):
        super().__init__(cuil, apellido, nombre, sueldo_basico, antiguedad)
        self.categoria = categoria

    def calcular_sueldo(self):
        porcentaje_categoria = 0.1 if 1 <= self.categoria <= 10 else 0.2 if 11 <= self.categoria <= 20 else 0.3
        return self.sueldo_basico + (self.antiguedad * self.sueldo_basico) + (porcentaje_categoria * self.sueldo_basico)
