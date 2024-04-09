from customtkinter import *
from programa.Controle.paciente_controle import *


class TelaInicial(CTk):

    def __init__(self):
        super().__init__()

        self.controlador = ControlePaciente()

        self.vetor_medicos = []
        self.medico_atual = 0
        self.num_medicos = 0

        self.title("Sarah")
        self.geometry(f"{800}x{580}")

        self.get_medicos()

        self.grid_columnconfigure(0, weight=20)
        self.grid_columnconfigure(1, weight=80)
        self.grid_rowconfigure((0, 1, 2, 3), weight=1)

        self.sidebar_frame = CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")

        self.sidebar_button_consultas = CTkButton(self.sidebar_frame, text="Consultas",
                                                  command=self.sidebar_button_event)
        self.sidebar_button_consultas.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.sidebar_button_busca = CTkButton(self.sidebar_frame, text="Buscar profissionais",
                                              command=self.sidebar_button_event)
        self.sidebar_button_busca.grid(row=1, column=0, padx=20, pady=(10, 10))

        self.main_frame = CTkFrame(self)
        self.main_frame.grid(row=0, column=1, rowspan=5, sticky="nsew")

        self.card_profissional = CTkFrame(self.main_frame)
        self.card_profissional.grid(row=0, column=0, padx=(50, 50), pady=(50, 50))

        self.nome_label = CTkLabel(self.card_profissional, text="Nome:", font=CTkFont(size=15))
        self.nome_campo = CTkLabel(self.card_profissional, text=self.vetor_medicos[self.medico_atual].nome, font=CTkFont(size=15))

        self.especialidades_label = CTkLabel(self.card_profissional, text="Especialidades:", font=CTkFont(size=15))
        self.especialidades_campo = CTkLabel(self.card_profissional, text=self.vetor_medicos[self.medico_atual].especializacao, font=CTkFont(size=15))

        self.planos_label = CTkLabel(self.card_profissional, text="Planos:", font=CTkFont(size=15))
        self.planos_campo = CTkLabel(self.card_profissional, text=self.vetor_medicos[self.medico_atual].convenios, font=CTkFont(size=15))

        self.crm_label = CTkLabel(self.card_profissional, text="CRM:", font=CTkFont(size=15))
        self.crm_campo = CTkLabel(self.card_profissional, text=self.vetor_medicos[self.medico_atual].crm, font=CTkFont(size=15))

        self.preco_consulta_label = CTkLabel(self.card_profissional, text="Valor consulta:", font=CTkFont(size=15))
        self.preco_consulta_campo = CTkLabel(self.card_profissional, text=self.vetor_medicos[self.medico_atual].preco_consulta, font=CTkFont(size=15))

        self.nome_campo.grid(row=0, column=1, pady=(10, 0))
        self.nome_label.grid(row=0, column=0, pady=(10, 0))

        self.especialidades_campo.grid(row=1, column=1, pady=(10, 0))
        self.especialidades_label.grid(row=1, column=0, pady=(10, 0))

        self.planos_campo.grid(row=2, column=1, pady=(10, 0))
        self.planos_label.grid(row=2, column=0, pady=(10, 0))

        self.crm_campo.grid(row=3, column=1, pady=(10, 0))
        self.crm_label.grid(row=3, column=0, pady=(10, 0))

        self.preco_consulta_campo.grid(row=4, column=1, pady=(10, 0))
        self.preco_consulta_label.grid(row=4, column=0, pady=(10, 0))

        self.pass_button = CTkButton(self.card_profissional, text="Passar", command=self.pass_button_event)
        self.pass_button.grid(row=5, column=0, padx=20, pady=(10, 10))
        self.like_button = CTkButton(self.card_profissional, text="Curtir", command=self.like_button_event)
        self.like_button.grid(row=5, column=1, padx=(20, 20), pady=(10, 10))

        self.card_profissional.configure(border_width=1, corner_radius=6)

    def get_medicos(self):
        self.vetor_medicos = self.controlador.get_medicos()
        self.num_medicos = len(self.vetor_medicos)

    def prox_medico(self):
        if self.medico_atual < self.num_medicos-1:
            self.medico_atual += 1
        else:
            self.medico_atual = 0

    def update_card(self):
        """Updates the card with information from the current medico."""
        medico_atual = self.vetor_medicos[self.medico_atual]
        self.nome_campo.configure(text=medico_atual.nome)
        self.especialidades_campo.configure(text=medico_atual.especializacao)
        self.planos_campo.configure(text=medico_atual.convenios)
        self.crm_campo.configure(text=medico_atual.crm)
        self.preco_consulta_campo.configure(text=medico_atual.preco_consulta)

    def sidebar_button_event(self):
        print("sidebar_button click")

    def pass_button_event(self):
        self.prox_medico()
        self.update_card()

    def like_button_event(self):
        self.prox_medico()
        self.update_card()
