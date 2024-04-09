from programa.modelo.profissional import *
from programa.persistencia.profissional_persistencia import *
from programa.persistencia.paciente_persistencia import *


class ControlePaciente:

    def __init__(self):
        self.profissionais = ProfissionalPersistencia()

    def get_medicos(self):
        vetor_medicos = []
        for m in self.profissionais.get_medicos():
            medico = Medico(
                m[0],
                m[1],
                m[2],
                m[3],
                m[4],
                m[5],
                m[6],
                m[7],
                m[8],
                m[9],
                m[10],
            )
            vetor_medicos.append(medico)

        return vetor_medicos
