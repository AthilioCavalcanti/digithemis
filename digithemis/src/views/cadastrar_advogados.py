from pathlib import Path
import tkinter as tk
from tkinter import Canvas, Entry, Button, PhotoImage, Frame, messagebox
from controllers import AdvogadoController
from errors import *


class RegisterUserApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.centralize()
        self.configure(bg='#81A69F')
        self.output_path = Path(__file__).parent
        self.assets_path = self.output_path / 'assets'

        self.title('Cadastrar advogado')
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
            file=self.relative_to_assets('cadastrar_usuario_image_1.png')
        )
        self.canvas.create_image(0, 0, anchor=tk.NW, image=background_image)
        self.canvas.background = (
            background_image  # Mantém a referência à imagem de fundo
        )

        # Adiciona a segunda imagem ao canvas
        second_image = PhotoImage(
            file=self.relative_to_assets('cadastrar_usuario_image_2.png')
        )
        self.canvas.create_image(503.0, 27.0, image=second_image)
        self.canvas.second_image = (
            second_image  # Mantém a referência à segunda imagem
        )

        # Adiciona os campos de entrada e seus rótulos
        list_entries = []
        entries_info = [
            (70.0, 124.0, 418.0, 45.0, 'NOME:'),
            (525.0, 124.0, 418.0, 45.0, 'CPF:'),
            (70.0, 322.0, 418.0, 45.0, 'SENHA:'),
            (525.0, 322.0, 418.0, 45.0, 'TELEFONE:'),
            (70.0, 223.0, 418.0, 45.0, 'EMAIL:'),
            (525.0, 223.0, 418.0, 45.0, 'OAB:'),
        ]
        for info in entries_info:
            list_entries.append(self.create_entry(*info))
        list_entries[2].config(show='*')
        self.entries = tuple(list_entries)

    def create_entry(self, x, y, width, height, label_text):
        entry_image = PhotoImage(
            file=self.relative_to_assets('cadastrar_usuario_entry_1.png')
        )
        entry_bg = self.canvas.create_image(
            x + 225, y + 22.5, image=entry_image
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
            'cadastrar_usuario_button_1.png',
            self.button_1_clicked,
        )
        self.create_button(
            379.0,
            455.0,
            250.0,
            76.0,
            'cadastrar_usuario_button_2.png',
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
        cpf = self.entries[1].get()
        senha = self.entries[2].get()
        telefone = self.entries[3].get()
        email = self.entries[4].get()
        oab = self.entries[5].get()

        if nome and cpf and senha and email and oab and telefone:
            try:
                self.controlador.adicionar_advogado(
                    nome, cpf, oab, email, telefone, senha
                )
                messagebox.showinfo(
                    'Notificação', 'Advogado cadastrado com sucesso'
                )
                for entrada in self.entries:
                    entrada.delete(0, 'end')
                self.entries[0].focus_set()
            except RegistroExistenteError:
                messagebox.showerror(
                    'Notificação', 'Advogado já está cadastrado no sistema'
                )
            except CPFInvalidoError:
                messagebox.showerror(
                    'Notificação', 'CPF inválido!'
                )
            except OABInvalidaError:
                messagebox.showerror(
                    'Notificação', 'OAB inválida!'
                )
            except EmailInvalidoError:
                messagebox.showerror(
                    'Notificação', 'E-mail inválido!'
                )
            except TelefoneInvalidoError:
                messagebox.showerror(
                    'Notificação', 'Telefone inválido!'
                )
            except Exception as erro:
                messagebox.showerror(
                    'Notificação', f'{erro}'
                )
                
        else:
            messagebox.showwarning('Notificação', f'Preencha todos os campos.')


if __name__ == '__main__':
    app = RegisterUserApp()
    app.mainloop()
