import csv


class PacientePersistencia:

    def get_pacientes(self):
        vetor_pacientes = []
        with open('persistencia/pacientes.csv') as pacientes:
            leitor = csv.reader(pacientes, delimiter=',')
            cabecalho = next(leitor)
            for linha in leitor:
                vetor_pacientes.append(linha)
            return vetor_pacientes
