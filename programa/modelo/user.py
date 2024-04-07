class Usuario:

    def __init__(self, nome, idade, cpf, sexo, localizacao):
        self.__nome = nome
        self.__idade = idade
        self.__cpf = cpf
        self.__sexo = sexo
        self.__localizacao = localizacao

    def get_nome(self):
        return self.__nome

    def get_idade(self):
        return self.__idade

    def get_cpf(self):
        return self.__cpf

    def get_sexo(self):
        return self.__sexo

    def set_nome(self, nome):
        self.__nome = nome

    def set_idade(self, idade):
        self.__idade = idade

    def set_cpf(self, cpf):
        self.__cpf = cpf

    def set_sexo(self, sexo):
        self.__sexo = sexo

