from abc import ABC, abstractmethod
from programa.Modelo.usuario import Usuario
from programa.Persistencia.persistencia import Persistencia


class Controle(ABC):
    def __init__(self):
        self.persistencia = Persistencia()

    @abstractmethod
    def solicita_login(self, usuario: Usuario):
        pass

    @abstractmethod
    def cadastrar_usuario(self, usuario: Usuario):
        pass

    @abstractmethod
    def enviar_mensagem(self, usuario: Usuario):
        pass

    @abstractmethod
    def remarcar_consulta(self, usuario: Usuario):
        pass

    @abstractmethod
    def desmarcar_consulta(self, usuario: Usuario):
        pass

    @abstractmethod
    def mudar_tela(self):
        pass