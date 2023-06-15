class Docente(AgenteUniversitario):
    def __init__(self, cuil, apellido, nombre, sueldo_basico, antiguedad, carrera, cargo, catedra):
        super().__init__(cuil, apellido, nombre, sueldo_basico, antiguedad)
        self.carrera = carrera
        self.cargo = cargo
        self.catedra = catedra

    def calcular_sueldo(self):
        porcentaje_cargo = 0.1 if self.cargo == "simple" else 0.2 if self.cargo == "semiexclusivo" else 0.5
        return self.sueldo_basico + (self.antiguedad * self.sueldo_basico) + (porcentaje_cargo * self.sueldo_basico)