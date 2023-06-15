# Interfaz ITesorero
class ITesorero(ABC):
    @abstractmethod
    def gastosSueldoPorEmpleado(self, dni):
        pass

