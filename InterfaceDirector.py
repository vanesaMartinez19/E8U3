
class IDirector(ABC):
    @abstractmethod
    def modificarBasico(self, dni, nuevoBasico):
        pass

    @abstractmethod
    def modificarPorcentajeporcargo(self, dni, nuevoPorcentaje):
        pass

    @abstractmethod
    def modificarPorcentajeporcategoria(self, dni, nuevoPorcentaje):
        pass

    @abstractmethod
    def modificarImporteExtra(self, dni, nuevoImporteExtra):
        pass
