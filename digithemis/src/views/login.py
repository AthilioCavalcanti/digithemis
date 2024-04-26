import json
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, Frame, messagebox
from controllers import AdvogadoController
from .menu_admin import AdminApp
from .menu_advogado import Menu_advogadoapp
from .esqueci_senha import EsqueciSenhaApp


class LoginApp:
    def __init__(self):
        self.window = Tk()
        self.centralize()
        self.window.configure(bg='#81A69F')
        self.window.title('Login')
        self.window.iconbitmap(f'{self.get_assets_path()}\\favicon.ico')
        self.controlador = AdvogadoController()

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

        self.assets_path = self.get_assets_path()

        self.create_images()
        self.input_login, self.input_password = self.create_entries()
        self.create_buttons()

        self.window.resizable(False, False)
        self.window.mainloop()

    def centralize(self):
        from .app import App

        App.centralize_app(self.window)

    def open_menu(self):
        cpf = str(self.input_login.get())
        senha = str(self.input_password.get())
        if cpf and senha:
            resposta = self.controlador.validar_acesso(cpf, senha)
            if resposta['acesso']:
                usuario = resposta['estado']
                self.save_user_state(usuario)
                self.window.destroy()

                if usuario['admin']:
                    menu_admin = AdminApp()
                if not usuario['admin']:
                    menu_advogado = Menu_advogadoapp()
            else:
                # condicionais de acordo com o erro retornado
                self.input_password.delete(0, 'end')
                messagebox.showwarning('Notificação', 'Credenciais inválidas.')
        else:
            messagebox.showwarning('Notificação', 'Preencha todos os campos')

    def open_esqueci(self):
        # self.window.destroy()
        # esqueci_senha = EsqueciSenhaApp()
        messagebox.showwarning(
            'Notificação',
            'Entre em contado com o suporte para recuperação da senha.',
        )

    def get_assets_path(self):
        current_dir = Path(__file__).parent
        assets_path = current_dir / './assets/'
        return assets_path

    def create_images(self):
        image_positions = [
            (503.0, 320.0),  # Image 1
            (500.96875, 96.0),  # Image 2
        ]
        image_files = ['login_image_1.png', 'login_image_2.png']
        self.images = []
        for position, image_path in zip(image_positions, image_files):
            image = PhotoImage(file=self.assets_path / image_path)
            self.images.append(image)
            self.canvas.create_image(*position, image=image)

    def create_buttons(self):
        button_info = [
            (445.0, 399.0, 'login_button_1.png', self.open_esqueci),
            (382.0, 434.0, 'login_button_3.png', self.open_menu),
        ]
        for info in button_info:
            self.create_button(*info)

    def create_button(self, x, y, image_path, command):
        button_image = PhotoImage(file=self.assets_path / image_path)
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

    def create_entries(self):
        entry_positions = [
            (504.0, 352.5),  # Entry 1
            (504.0, 265.5),  # Entry 2
        ]
        for position in entry_positions:
            self.canvas.create_image(*position)

        entry_frame_1 = Frame(self.window, bg='#FFFFFF', padx=10)
        entry_frame_1.place(x=295.0, y=242.0, width=418.0, height=45.0)
        entry_1 = Entry(
            entry_frame_1,
            bd=0,
            bg='#FFFFFF',
            fg='#000716',
            highlightthickness=0,
        )
        entry_1.pack(expand=True, fill='both')

        entry_frame_2 = Frame(self.window, bg='#FFFFFF', padx=10)
        entry_frame_2.place(x=295.0, y=329.0, width=418.0, height=45.0)
        entry_2 = Entry(
            entry_frame_2,
            bd=0,
            bg='#FFFFFF',
            fg='#000716',
            highlightthickness=0,
            show='*',
        )
        entry_2.pack(expand=True, fill='both')

        self.canvas.create_text(
            306.0,
            222.0,
            anchor='nw',
            text='CPF:',
            fill='#FFFFFF',
            font=('HammersmithOne Regular', 15 * -1),
        )

        self.canvas.create_text(
            306.0,
            311.0,
            anchor='nw',
            text='SENHA:',
            fill='#FFFFFF',
            font=('HammersmithOne Regular', 15 * -1),
        )

        return entry_1, entry_2

    def save_user_state(self, usuario):
        file_path = './user_state.json'
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(usuario, file, ensure_ascii=False)


if __name__ == '__main__':
    app = LoginApp()
