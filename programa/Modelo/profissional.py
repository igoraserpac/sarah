from programa.Modelo.usuario import *


class Medico(Usuario):
    def __init__(
            self,
            nome,
            idade,
            cpf,
            sexo,
            localizacao,
            preco_consulta,
            convenios,
            temp_atividade,
            formacao,
            crm,
            especializacao
    ):
        super().__init__(nome, idade, cpf, sexo, localizacao)
        self.preco_consulta = preco_consulta
        self.convenios = convenios
        self.temp_atividade = temp_atividade
        self.formacao = formacao
        self.crm = crm
        self.especializacao = especializacao

    def get_especializacao(self):
        return self.especializacao

    def get_crm(self):
        return self.crm

    def get_formacao(self):
        return self.formacao

    def get_temp_atividade(self):
        return self.temp_atividade

    def get_convenios(self):
        return self.convenios

    def get_preco_consulta(self):
        return self.preco_consulta

    def set_especializacao(self, especializacao):
        self.especializacao = especializacao

    def set_crm(self, crm):
        self.crm = crm

    def set_formacao(self, formacao):
        self.formacao = formacao

    def set_temp_atividade(self, temp_atividade):
        self.temp_atividade = temp_atividade

    def set_convenios(self, convenios):
        self.convenios = convenios

    def set_preco_consulta(self, preco_consulta):
        self.preco_consulta = preco_consulta
