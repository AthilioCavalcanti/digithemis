from pathlib import Path
import tkinter as tk
from tkinter import Canvas, Button, PhotoImage

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / 'assets'


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


class Menu_advogadoapp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.centralize()
        self.configure(bg='#81A69F')
        self.create_canvas()
        self.create_buttons()
        self.title('Menu')
        self.iconbitmap(f'{relative_to_assets('favicon.ico')}')
        self.mainloop()

    def centralize(self):
        from .app import App
        App.centralize_app(self)

    def create_canvas(self):
        self.canvas = Canvas(
            self,
            bg='#81A69F',
            height=641,
            width=1007,
            bd=0,
            highlightthickness=0,
            relief='ridge',
        )
        self.canvas.place(x=0, y=0)

        self.image_image_1 = PhotoImage(
            file=relative_to_assets('advogado_image_1.png')
        )
        self.image_1 = self.canvas.create_image(
            503.0, 320.0, image=self.image_image_1
        )

        self.image_image_2 = PhotoImage(
            file=relative_to_assets('advogado_image_2.png')
        )
        self.image_2 = self.canvas.create_image(
            503.0, 27.0, image=self.image_image_2
        )

    def create_buttons(self):
        buttons_info = [
            ('advogado_button_1.png', (437.0, 396.0), self.button_1_clicked),
            ('advogado_button_2.png', (437.0, 209.0), self.button_2_clicked),
            ('advogado_button_3.png', (127.0, 209.0), self.button_3_clicked),
            ('advogado_button_4.png', (747.0, 209.0), self.button_4_clicked),
        ]

        for image_name, (x, y), command in buttons_info:
            self.create_button(image_name, x, y, command)

        self.create_button(
            'logout.png',
            14.0,
            14.0,
            self.button_5_clicked,
        )

    def create_button(self, image_name, x, y, command, **kwargs):
        button_image = PhotoImage(file=relative_to_assets(image_name))
        button = Button(
            self,
            image=button_image,
            borderwidth=0,
            highlightthickness=0,
            command=command,
            relief='flat',
        )
        button.image = button_image
        button.place(x=x, y=y, **kwargs)

    # Funções associadas a cada botão
    def button_1_clicked(self):
        self.destroy()
        # from .editar_perfil import EditProfileApp

        # editar = EditProfileApp()
        from .perfil_advogado import AplicativoPerfilAdvogado
        editar = AplicativoPerfilAdvogado()

    def button_2_clicked(self):
        self.destroy()
        from .inserir_processo import InsertProcess
        inserir_Processo = InsertProcess()

    def button_3_clicked(self):
        self.destroy()
        from .cadastrar_cliente import RegisterClientApp

        registro_cliente = RegisterClientApp()

    def button_4_clicked(self):
        self.destroy()
        from .buscar_clientes import SearchApp

        procurar = SearchApp()

    def button_5_clicked(self):
        self.destroy()
        from .app import App
        from .login import LoginApp
        # logout
        if App.user_state_exists():
            App.delete_user_state()
        login_tela = LoginApp()


if __name__ == '__main__':
    app = Menu_advogadoapp()
