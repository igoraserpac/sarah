from abc import ABC, abstractmethod
from programa.Modelo.usuario import Usuario


class Persistencia(ABC):

    @abstractmethod
    def gravar_dados(self, usuario: Usuario):
        pass

    @abstractmethod
    def gravar_mensagem(self, usuario: Usuario):
        pass

    @abstractmethod
    def excluir_consulta(self, usuario: Usuario):
        pass

    @abstractmethod
    def gravar_consulta(self, usuario: Usuario):
        pass

