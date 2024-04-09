class Usuario:

    def __init__(self, nome, idade, cpf, sexo, localizacao):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.sexo = sexo
        self.localizacao = localizacao

    def get_nome(self):
        return self.nome

    def get_idade(self):
        return self.idade

    def get_cpf(self):
        return self.cpf

    def get_sexo(self):
        return self.sexo

    def set_nome(self, nome):
        self.nome = nome

    def set_idade(self, idade):
        self.idade = idade

    def set_cpf(self, cpf):
        self.cpf = cpf

    def set_sexo(self, sexo):
        self.sexo = sexo
