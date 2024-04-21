from pathlib import Path
import tkinter as tk
from tkinter import Canvas, Entry, Frame, Button, PhotoImage, messagebox
from controllers import ClienteController
from errors import RegistroExistenteError, validacao_error


class RegisterClientApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.centralize()
        self.configure(bg='#81A69F')
        self.output_path = Path(__file__).parent
        self.assets_path = self.output_path / 'assets'
        self.title('Cadastrar de cliente')
        self.iconbitmap(f'{self.relative_to_assets('favicon.ico')}')
        self.entries = []
        self.create_widgets()
        self.controller = ClienteController()

    def relative_to_assets(self, path: str) -> Path:
        return self.assets_path / Path(path)

    def centralize(self):
        from .app import App

        App.centralize_app(self)

    def create_widgets(self):
        self.create_canvas()
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
            file=self.relative_to_assets('cadastrar_cliente_image_1.png')
        )
        self.canvas.create_image(0, 0, anchor=tk.NW, image=background_image)
        self.canvas.background = (
            background_image  # Mantém a referência à imagem de fundo
        )

        # Adiciona a segunda imagem ao canvas
        second_image = PhotoImage(
            file=self.relative_to_assets('cadastrar_cliente_image_2.png')
        )
        self.canvas.create_image(503.0, 27.0, image=second_image)
        self.canvas.second_image = (
            second_image  # Mantém a referência à segunda imagem
        )

        list_entries = []
        # Adiciona os campos de entrada e seus rótulos
        entries_info = [
            (67.0, 182.0, 418.0, 45.0, 'NOME:'),
            (522.0, 182.0, 418.0, 45.0, 'CPF/CNPJ:'),
            (67.0, 319.0, 418.0, 45.0, 'EMAIL:'),
            (522.0, 319.0, 418.0, 45.0, 'TELEFONE:'),
        ]
        for info in entries_info:
            list_entries.append(self.create_entry(*info))

        self.entries = tuple(list_entries)

    def create_entry(self, x, y, width, height, label_text):
        entry_image = PhotoImage(
            file=self.relative_to_assets('cadastrar_cliente_entry_1.png')
        )
        entry_bg = self.canvas.create_image(
            x + 204, y + 22.5, image=entry_image
        )
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
            17.0,
            20.0,
            14.0,
            14.0,
            'cadastrar_cliente_button_1.png',
            self.button_1_clicked,
        )
        self.create_button(
            379.0,
            455.0,
            250.0,
            76.0,
            'cadastrar_cliente_button_2.png',
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
        self.destroy()
        from .app import App

        usuario = App.load_user_state()
        if usuario['admin']:
            from .menu_admin import AdminApp

            menu_admin = AdminApp()

        if not usuario['admin']:
            from .menu_advogado import Menu_advogadoapp

            menu_advogado = Menu_advogadoapp()

    def button_2_clicked(self):
        nome = self.entries[0].get()
        cpf_cnpj = self.entries[1].get()
        email = self.entries[2].get()
        telefone = self.entries[3].get()

        if nome and cpf_cnpj and email and telefone:
            try:
                self.controller.adicionar_cliente(
                    nome, cpf_cnpj, email, telefone
                )
                messagebox.showinfo(
                    'Notificação', 'Cliente cadastrado com sucesso'
                )
                for entrada in self.entries:
                    entrada.delete(0, 'end')
                self.entries[0].focus_set()
            except RegistroExistenteError:
                messagebox.showerror(
                    'Notificação', 'Cliente já está cadastrado no sistema'
                )
            except validacao_error.CPFInvalidoError:
                messagebox.showerror(
                    'Notificação', 'CPF inválido!'
                )
            except validacao_error.CNPJInvalidoError:
                messagebox.showerror(
                    'Notificação', 'CNPJ inválido!'
                )
            except validacao_error.EmailInvalidoError:
                messagebox.showerror(
                    'Notificação', 'E-mail inválido!'
                )
            except Exception as erro:
                messagebox.showerror(
                    'Notificação', f'{erro}'
                )
                
        else:
            messagebox.showwarning('Notificação', f'Preencha todos os campos.')


if __name__ == '__main__':
    app = RegisterClientApp()
    app.mainloop()
