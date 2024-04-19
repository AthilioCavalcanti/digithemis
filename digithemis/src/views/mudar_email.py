from pathlib import Path
import tkinter as tk
from tkinter import Canvas, Entry, Button, PhotoImage, Frame, messagebox
from controllers import AdvogadoController
from errors import EmailInvalidoError


class ChangeEmailApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.centralize()
        self.configure(bg='#81A69F')
        self.output_path = Path(__file__).parent
        self.assets_path = self.output_path / 'assets'
        self.title('Mudar e-mail')
        self.iconbitmap(f'{self.relative_to_assets('favicon.ico')}')

        self.controlador = AdvogadoController()

        self.create_widgets()

    def relative_to_assets(self, path: str) -> Path:
        return self.assets_path / Path(path)

    def centralize(self):
        from .app import App

        App.centralize_app(self)

    def create_widgets(self):
        self.create_canvas()
        self.create_entries()
        self.create_buttons()

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

        # Adiciona a imagem de fundo ao canvas
        background_image = PhotoImage(
            file=self.relative_to_assets('mudar_email_image_1.png')
        )
        self.canvas.create_image(503.0, 320.0, image=background_image)
        self.canvas.background = (
            background_image  # Mantém a referência à imagem de fundo
        )

        # Adiciona a segunda imagem ao canvas
        second_image = PhotoImage(
            file=self.relative_to_assets('mudar_email_image_2.png')
        )
        self.canvas.create_image(503.0, 27.0, image=second_image)
        self.canvas.second_image = (
            second_image  # Mantém a referência à segunda imagem
        )

    def create_entries(self):
        self.entry_new_email = self.create_entry(
            283.0, 329.0, 418.0, 45.0, 'EMAIL NOVO:'
        )
        self.entry_old_email = self.create_entry(
            283.0, 198.0, 418.0, 45.0, 'EMAIL ANTIGO:'
        )
        from .app import App

        self.entry_old_email.insert(0, App.load_user_state()['email'])
        self.entry_old_email.config(
            state='disable', disabledbackground='#FFFFFF'
        )

    def create_entry(self, x, y, width, height, label_text):
        entry_image = PhotoImage(
            file=self.relative_to_assets('mudar_email_entry_1.png')
        )
        entry_bg = self.canvas.create_image(492.0, y + 23.5, image=entry_image)
        entry_frame = Frame(self, bg='#FFFFFF', padx=10)
        entry_frame.place(x=x - 10, y=y, width=418.0, height=45.0)
        entry = Entry(
            self, bd=0, bg='#FFFFFF', fg='#000716', highlightthickness=0
        )
        entry.place(x=x, y=y, width=width, height=height)
        self.canvas.create_text(
            x,  # Offset para alinhar com a entrada
            y - 20,  # Offset para alinhar com a entrada
            anchor='nw',
            text=label_text,
            fill='#FFFFFF',
            font=('HammersmithOne Regular', 15 * -1),
        )
        return entry

    def create_buttons(self):
        self.create_button(
            378.0,
            414.0,
            252.0,
            61.0,
            'mudar_email_button_1.png',
            self.button_1_clicked,
        )
        self.create_button(
            17.0,
            17.0,
            20.0,
            20.0,
            'mudar_email_button_2.png',
            self.button_2_clicked,
        )

    def create_button(self, x, y, width, height, image_path, command):
        button_image = PhotoImage(file=self.relative_to_assets(image_path))
        button = Button(
            self,
            image=button_image,
            borderwidth=0,
            highlightthickness=0,
            command=command,
            relief='flat',
        )
        button.image = (
            button_image  # Garante que a imagem seja mantida em memória
        )
        button.place(x=x, y=y, width=width, height=height)

    def button_1_clicked(self):
        novo_email = self.entry_new_email.get()
        if novo_email:
            try:
                from .app import App

                if novo_email == App.load_user_state()['email']:
                    messagebox.showwarning(
                        'Notificação',
                        'Atualize o email antes de tentar alterar.',
                    )
                else:
                    cpf = App.load_user_state()['cpf']
                    self.controlador.atualizar_email_advogado(cpf, novo_email)
                    messagebox.showinfo(
                        'Notificação', 'Email atualizado com sucesso'
                    )

                    App.update_user_state('email', novo_email)
            except EmailInvalidoError as erro_email:
                messagebox.showerror('Notificação', f'{erro_email}')
            except Exception as erro:
                messagebox.showerror('Notificação', f'{erro}')
        else:
            messagebox.showwarning(
                'Notificação', 'Preencha o campo de novo email.'
            )

    def button_2_clicked(self):
        self.destroy()
        from .editar_perfil import EditProfileApp

        edit = EditProfileApp()


if __name__ == '__main__':
    app = ChangeEmailApp()
    app.mainloop()
