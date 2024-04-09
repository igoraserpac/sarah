from programa.Modelo.usuario import *


class Paciente(Usuario):
    def __init__(self, nome, idade, cpf, sexo, localizacao, faixa_preco, convenios):
        super().__init__(nome, idade, cpf, sexo, localizacao)
        self.faixa_preco = faixa_preco
        self.convenios = convenios

    def get_faixa_preco(self):
        return self.faixa_preco

    def get_convenios(self):
        return self.convenios
