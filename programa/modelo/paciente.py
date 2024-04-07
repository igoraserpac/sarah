from user import *


class Paciente(Usuario):
    def __init__(self, nome, idade, cpf, sexo, localizacao, faixa_preco, convenios):
        super().__init__(nome, idade, cpf, sexo, localizacao)
        self.__faixa_preco = faixa_preco
        self.__convenios = convenios

    def get_faixa_preco(self):
        return self.__faixa_preco

    def get_convenios(self):
        return self.__convenios