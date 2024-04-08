from customtkinter import *

class TelaInicial(CTk):

    def __init__(self):
        super().__init__()

        self.title("Sarah")

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

        self.main_frame = CTkFrame(self, width=456, corner_radius=0)
        self.main_frame.grid(row=0, column=1, rowspan=4, sticky="nsew")

        self.card_profissional = CTkFrame(self.main_frame)
        self.card_profissional.grid(row=0, column=0)

        self.nome_label = CTkLabel(self.card_profissional, text="Nome:", font=CTkFont(size=12))
        self.nome_campo = CTkLabel(self.card_profissional, text="Fulano", font=CTkFont(size=15))

        self.especialidades_label = CTkLabel(self.card_profissional, text="Especialidades:", font=CTkFont(size=11))
        self.especialidades_campo = CTkLabel(self.card_profissional, text="exemplo", font=CTkFont(size=13))

        self.planos_label = CTkLabel(self.card_profissional, text="Panos:", font=CTkFont(size=12))
        self.planos_campo = CTkLabel(self.card_profissional, text="Santa casa", font=CTkFont(size=15))

        self.crm_label = CTkLabel(self.card_profissional, text="CRM:", font=CTkFont(size=12))
        self.crm_campo = CTkLabel(self.card_profissional, text="1234567890", font=CTkFont(size=15))

        self.nome_campo.grid(row=0, column=1, pady=(10, 0))
        self.nome_label.grid(row=0, column=0, pady=(10, 0))

        self.especialidades_campo.grid(row=1, column=1, pady=(10, 0))
        self.especialidades_label.grid(row=1, column=0, pady=(10, 0))

        self.planos_campo.grid(row=2, column=1, pady=(10, 0))
        self.planos_label.grid(row=2, column=0, pady=(10, 0))

        self.crm_campo.grid(row=3, column=1, pady=(10, 0))
        self.crm_label.grid(row=3, column=0, pady=(10, 0))

        self.pass_button = CTkButton(self.card_profissional, text="Passar", command=self.pass_button_event)
        self.pass_button.grid(row=4, column=0, padx=20, pady=(10, 10))
        self.like_button = CTkButton(self.card_profissional, text="Curtir", command=self.like_button_event)
        self.like_button.grid(row=4, column=1, padx=(20, 20), pady=(10, 10))

        self.card_profissional.configure(border_width=1, corner_radius=2)

    def sidebar_button_event(self):
        print("sidebar_button click")

    def pass_button_event(self):
        print("Pass button clicked")

    def like_button_event(self):
        print("Like button clicked")


if __name__ == "__main__":
    app = TelaInicial()
    app.mainloop()
