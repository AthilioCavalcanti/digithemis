from pathlib import Path
import tkinter as tk
from tkinter import Canvas, Entry, Button, PhotoImage


class RegisterUserApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('1007x641')
        self.configure(bg='#81A69F')
        self.output_path = Path(__file__).parent
        self.assets_path = self.output_path / 'assets'

        self.create_widgets()

    def relative_to_assets(self, path: str) -> Path:
        return self.assets_path / Path(path)

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
        entries_info = [
            (70.0, 124.0, 418.0, 45.0, 'NOME:'),
            (525.0, 124.0, 418.0, 45.0, 'CPF:'),
            (70.0, 322.0, 418.0, 45.0, 'SENHA:'),
            (525.0, 322.0, 418.0, 45.0, 'TELEFONE:'),
            (70.0, 223.0, 418.0, 45.0, 'EMAIL:'),
            (525.0, 223.0, 418.0, 45.0, 'OAB:'),
        ]
        for info in entries_info:
            self.create_entry(*info)

    def create_entry(self, x, y, width, height, label_text):
        entry_image = PhotoImage(
            file=self.relative_to_assets('cadastrar_usuario_entry_1.png')
        )
        entry_bg = self.canvas.create_image(
            x + 225, y + 22.5, image=entry_image
        )
        entry = Entry(
            self, bd=0, bg='#FFFFFF', fg='#000716', highlightthickness=0
        )
        entry.place(x=x, y=y, width=width, height=height)
        self.canvas.create_text(
            x + 11,  # Offset para alinhar com a entrada
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
        from .login import LoginApp

        login_tela = LoginApp()

    def button_2_clicked(self):
        print('button_2 clicked')


if __name__ == '__main__':
    app = RegisterUserApp()
    app.mainloop()
