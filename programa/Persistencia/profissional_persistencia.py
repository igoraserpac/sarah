from programa.Modelo.profissional import *
import csv


class ProfissionalPersistencia():

    def get_medicos(self):
        vetor_medicos = []
        with open('Persistencia/medicos.csv') as medicos:
            leitor = csv.reader(medicos, delimiter=',')
            cabecalho = next(leitor)
            for linha in leitor:
                vetor_medicos.append(linha)
            return vetor_medicos
