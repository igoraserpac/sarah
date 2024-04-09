from customtkinter import *
import csv
from programa.modelo.paciente import *
from programa.controle.profissional_controle import *


class TelaInicial(CTk):

    def __init__(self):
        super().__init__()

        self.vetor_pacientes = []
        self.paciente_atual = 0
        self.num_pacientes = 0

        self.controlador = ControleProfissional()

        self.title("Sarah")
        self.geometry(f"{800}x{580}")

        self.get_pacientes()

        self.grid_columnconfigure(0, weight=20)
        self.grid_columnconfigure(1, weight=80)
        self.grid_rowconfigure((0, 1, 2, 3), weight=1)

        self.sidebar_frame = CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")

        self.sidebar_button_consultas = CTkButton(self.sidebar_frame, text="Consultas",
                                                  command=self.sidebar_consultas_event)
        self.sidebar_button_consultas.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.sidebar_button_busca = CTkButton(self.sidebar_frame, text="Buscar pacientes",
                                              command=self.sidebar_busca_event)
        self.sidebar_button_busca.grid(row=1, column=0, padx=20, pady=(10, 10))

        self.main_frame = CTkFrame(self)
        self.main_frame.grid(row=0, column=1, rowspan=5, sticky="nsew")

        self.card_profissional = CTkFrame(self.main_frame)
        self.card_profissional.grid(row=0, column=0, padx=(50, 50), pady=(50, 50))

        self.nome_label = CTkLabel(self.card_profissional, text="Nome:", font=CTkFont(size=15))
        self.nome_campo = CTkLabel(self.card_profissional, text=self.vetor_pacientes[self.paciente_atual].nome,
                                   font=CTkFont(size=15))

        self.convenios_label = CTkLabel(self.card_profissional, text="Convênios:", font=CTkFont(size=15))
        self.convenios_campo = CTkLabel(self.card_profissional,
                                        text=self.vetor_pacientes[self.paciente_atual].convenios, font=CTkFont(size=15))

        self.nome_campo.grid(row=0, column=1, pady=(10, 0))
        self.nome_label.grid(row=0, column=0, pady=(10, 0))

        self.convenios_campo.grid(row=1, column=1, pady=(10, 0))
        self.convenios_label.grid(row=1, column=0, pady=(10, 0))

        self.pass_button = CTkButton(self.card_profissional, text="Passar", command=self.pass_button_event)
        self.pass_button.grid(row=5, column=0, padx=20, pady=(10, 10))
        self.like_button = CTkButton(self.card_profissional, text="Ver", command=self.like_button_event)
        self.like_button.grid(row=5, column=1, padx=(20, 20), pady=(10, 10))

        self.card_profissional.configure(border_width=1, corner_radius=10)

    def get_pacientes(self):
        self.vetor_pacientes = self.controlador.get_pacientes()
        self.num_pacientes = len(self.vetor_pacientes)

    def prox_paciente(self):
        if self.paciente_atual < self.num_pacientes - 1:
            self.paciente_atual += 1
        else:
            self.paciente_atual = 0

    def update_card(self):
        """Updates the card with information from the current paciente."""
        paciente_atual = self.vetor_pacientes[self.paciente_atual]
        self.nome_campo.configure(text=paciente_atual.nome)
        self.convenios_campo.configure(text=paciente_atual.convenios)

    def sidebar_consultas_event(self):
        pass

    def sidebar_busca_event(self):
        pass

    def pass_button_event(self):
        self.prox_paciente()
        self.update_card()

    def like_button_event(self):
        self.prox_paciente()
        self.update_card()


if __name__ == "__main__":
    app = TelaInicial()
    app.mainloop()
