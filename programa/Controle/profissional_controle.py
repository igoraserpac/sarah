from programa.Modelo.profissional import *
from programa.Modelo.paciente import *
from programa.Persistencia.profissional_persistencia import *
from programa.Persistencia.paciente_persistencia import *


class ControleProfissional:

    def __init__(self):
        self.pacientes = PacientePersistencia()

    def get_pacientes(self):
        vetor_pacientes = []
        for m in self.pacientes.get_pacientes():
            paciente = Paciente(
                m[0],
                m[1],
                m[2],
                m[3],
                m[4],
                m[5],
                m[6],
            )
            vetor_pacientes.append(paciente)

        return vetor_pacientes
