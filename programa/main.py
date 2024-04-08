import customtkinter

class TelaInicial(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("CustomTkinter complex_example.py")
        self.geometry(f"{800}x{580}")

        # create grid layout (2x4)
        self.grid_columnconfigure(0, weight=20)
        self.grid_columnconfigure(1, weight=80)
        self.grid_rowconfigure((0, 1, 2, 3), weight=1)

        # create sidebar frame with buttons 1 and 2
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")

        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, text="Botão 1",
                                                        command=self.sidebar_button_event)
        self.sidebar_button_1.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, text="Botão 2",
                                                        command=self.sidebar_button_event)
        self.sidebar_button_2.grid(row=1, column=0, padx=20, pady=(10, 10))

        self.card_profissional = customtkinter.CTkFrame(self.)

        # Crie um novo frame para o card
        self.card_content_frame = customtkinter.CTkFrame(
            self.card_frame,
            fg_color="transparent",
        )
        self.card_content_frame.grid(row=1, column=0, columnspan=2, sticky="nsew")

        # Crie labels e widgets para cada campo
        self.name_label = customtkinter.CTkLabel(self.card_content_frame, text="Nome:",
                                                 font=customtkinter.CTkFont(size=12))
        self.name_entry = customtkinter.CTkEntry(self.card_content_frame, width=200)

        self.specialties_label = customtkinter.CTkLabel(self.card_content_frame, text="Especialidades:",
                                                        font=customtkinter.CTkFont(size=12))
        self.specialties_entry = customtkinter.CTkEntry(self.card_content_frame, width=200)

        self.plans_label = customtkinter.CTkLabel(self.card_content_frame, text="Planos:",
                                                  font=customtkinter.CTkFont(size=12))
        self.plans_entry = customtkinter.CTkEntry(self.card_content_frame, width=200)

        self.crm_label = customtkinter.CTkLabel(self.card_content_frame, text="CRM:",
                                                font=customtkinter.CTkFont(size=12))
        self.crm_entry = customtkinter.CTkEntry(self.card_content_frame, width=100)

        # Posicione os widgets na grade
        self.name_label.grid(row=0, column=0, pady=(10, 0))
        self.name_entry.grid(row=0, column=1, pady=(10, 0))

        self.specialties_label.grid(row=1, column=0, pady=(10, 0))
        self.specialties_entry.grid(row=1, column=1, pady=(10, 0))

        self.plans_label.grid(row=2, column=0, pady=(10, 0))
        self.plans_entry.grid(row=2, column=1, pady=(10, 0))

        self.crm_label.grid(row=3, column=0, pady=(10, 0))
        self.crm_entry.grid(row=3, column=1, pady=(10, 0))

        self.pass_button = customtkinter.CTkButton(self.card_frame, text="Passar", command=self.pass_button_event)
        self.pass_button.grid(row=2, column=0, padx=20, pady=(10, 10))
        self.like_button = customtkinter.CTkButton(self.card_frame, text="Curtir", command=self.like_button_event)
        self.like_button.grid(row=2, column=1, padx=(20, 20), pady=(10, 10))

        # Ajuste o layout do card
        self.card_content_frame.configure(border_width=1, corner_radius=2)

        # # create doctor card frame
        # self.card_frame = customtkinter.CTkFrame(self, fg_color="transparent")
        # self.card_frame.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")
        # self.card_frame.grid_columnconfigure((0, 1), weight=1)
        #
        # self.doctor_label = customtkinter.CTkButton(self.card_frame, text="Dr. Fulano de Tal", font=customtkinter.CTkFont(size=16))
        # self.doctor_label.grid(row=0, column=0, columnspan=2, padx=20, pady=(20, 10))  # Ajuste para preencher duas colunas


        # ... rest of your code (functions, etc.)

    def sidebar_button_event(self):
        print("sidebar_button click")

    def pass_button_event(self):
        print("Pass button clicked")

    def like_button_event(self):
        print("Like button clicked")


if __name__ == "__main__":
    app = TelaInicial()
    app.mainloop()
