import os
from tkinter import Tk, Canvas, Button, PhotoImage


class AdminApp:
    def __init__(self):
        self.window = Tk()
        self.centralize()
        self.window.configure(bg='#81A69F')
        self.window.title('Menu')
        self.window.iconbitmap(f'{self.relative_to_assets('favicon.ico')}')

        self.canvas = Canvas(
            self.window,
            bg='#81A69F',
            height=641,
            width=1007,
            bd=0,
            highlightthickness=0,
            relief='ridge',
        )
        self.canvas.place(x=0, y=0)

        self.create_images()
        self.create_buttons()

        self.window.resizable(False, False)
        self.window.mainloop()

    def centralize(self):
        from .app import App
        App.centralize_app(self.window)

    def relative_to_assets(self, path):
        current_dir = os.path.dirname(__file__)
        assets_dir = os.path.join(current_dir, 'assets')
        return os.path.join(assets_dir, path)

    def create_images(self):
        image_positions = [(503.0, 320.0), (503.0, 27.0)]  # Image 1  # Image 2
        image_files = ['admin_image_1.png', 'admin_image_2.png']
        self.images = []
        for position, image_path in zip(image_positions, image_files):
            image = PhotoImage(file=self.relative_to_assets(image_path))
            self.images.append(image)
            self.canvas.create_image(*position, image=image)

    def create_buttons(self):
        button_info = [
            (127.0, 406.0, 'admin_button_1.png', self.button_1_clicked),
            (437.0, 406.0, 'admin_button_2.png', self.button_2_clicked),
            (747.0, 406.0, 'admin_button_3.png', self.button_3_clicked),
            (437.0, 209.0, 'admin_button_4.png', self.button_4_clicked),
            (127.0, 209.0, 'admin_button_5.png', self.button_5_clicked),
            (747.0, 209.0, 'admin_button_6.png', self.button_6_clicked),
            (15.0, 15.0, 'logout.png', self.button_7_clicked),
        ]
        for info in button_info:
            self.create_button(*info)

    def create_button(self, x, y, image_path, command):
        button_image = PhotoImage(file=self.relative_to_assets(image_path))
        button = Button(
            self.window,
            image=button_image,
            borderwidth=0,
            highlightthickness=0,
            command=command,
            relief='flat',
        )
        button.image = button_image
        button.place(x=x, y=y)

    # Funções associadas a cada botão
    def button_1_clicked(self):
        self.window.destroy()
        # from .editar_perfil import EditProfileApp

        # editar = EditProfileApp()
        from .perfil_advogado import AplicativoPerfilAdvogado
        perfil = AplicativoPerfilAdvogado()

    def button_2_clicked(self):
        self.window.destroy()
        from .buscar_advogados import SearchApp

        procurar = SearchApp()

    def button_3_clicked(self):
        print('Button 3 clicked')

    def button_4_clicked(self):
        self.window.destroy()
        from .inserir_processo import InsertProcess

        inserir_Processo = InsertProcess()

    def button_5_clicked(self):
        self.window.destroy()
        from .cadastrar_cliente import RegisterClientApp

        registro_cliente = RegisterClientApp()

    def button_6_clicked(self):
        self.window.destroy()
        from .buscar_clientes import SearchApp

        procurar = SearchApp()

    def button_7_clicked(self):
        self.window.destroy()
        from .app import App
        from .login import LoginApp

        # logout
        if App.user_state_exists():
            App.delete_user_state()
        login_tela = LoginApp()


if __name__ == '__main__':
    app = AdminApp()
