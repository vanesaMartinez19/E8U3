class DocenteInvestigador(Docente, Investigador):
    def __init__(
        self,
        cuil,
        apellido,
        nombre,
        sueldo_basico,
        antiguedad,
        carrera,
        cargo,
        catedra,
        area_investigacion,
        tipo_investigacion,
        categoria,
        importe_extra,
    ):
        Docente.__init__(self, cuil, apellido, nombre, sueldo_basico, antiguedad, carrera, cargo, catedra)
        Investigador.__init__(self, cuil, apellido, nombre, sueldo_basico, antiguedad, area_investigacion, tipo_investigacion)
        self.categoria = categoria
        self.importe_extra = importe_extra

    def calcular_sueldo(self):
        sueldo_docente = super().calcular_sueldo()
        return sueldo_docente + self.importe_extra
