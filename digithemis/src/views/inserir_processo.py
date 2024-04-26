from pathlib import Path
import tkinter as tk
from tkinter import Canvas, Button, PhotoImage, filedialog, Label

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / 'assets'


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


class InsertProcess(tk.Tk):
    def __init__(self):
        super().__init__()
        self.centralize()
        self.title('Adicionar processo')
        self.iconbitmap(f'{relative_to_assets('favicon.ico')}')
        self.configure(bg='#81A69F')
        self.create_canvas()
        self.create_buttons()
        self.display_path = None

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
            file=relative_to_assets('inserir_processo_image_1.png')
        )
        self.image_1 = self.canvas.create_image(
            503.0, 320.0, image=self.image_image_1
        )

        self.image_image_2 = PhotoImage(
            file=relative_to_assets('inserir_processo_image_2.png')
        )
        self.image_2 = self.canvas.create_image(
            503.0, 27.0, image=self.image_image_2
        )

    def create_buttons(self):
        self.canvas.create_text(
            311.0,
            208.0,
            anchor='nw',
            text='SELECIONAR O DOCUMENTO:',
            fill='#FFFFFF',
            font=('HammersmithOne Regular', 15 * -1),
        )

        buttons_info = [
            (
                'inserir_processo_button_1.png',
                (23.0, 12.0),
                self.button_1_clicked,
                {'width': 25.0, 'height': 30.0},
            ),
            (
                'inserir_processo_button_2.png',
                (461.0, 353.0),
                self.button_2_clicked,
                {'width': 87.0, 'height': 81.0},
            ),
            (
                'inserir_processo_button_3.png',
                (295.0, 228.0),
                self.button_3_clicked,
                {'width': 418.0, 'height': 47.0},
            ),
        ]

        for image_name, (x, y), command, kwargs in buttons_info:
            self.create_button(image_name, x, y, command, **kwargs)

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

        return button

    # Funções associadas a cada botão
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
        pass

    def button_3_clicked(self):
        # Sendo processo é melhor apenas PDF
        caminho_arquivo = filedialog.askopenfilename(
            filetypes=[('Processo', '*.pdf;*.jpg;*.jpeg;*.png')]
        )
        print('O caminho para o arquivo selecionado é')
        if caminho_arquivo:
            texto_caminho = caminho_arquivo
            if len(caminho_arquivo) > 55:
                texto_caminho = caminho_arquivo[:53] + '...'

            self.display_path = Label(
                self, text=texto_caminho, compound='left', fg='black'
            )
            self.display_path.place(x=295.0, y=229.0, width=360.0, height=45.0)


if __name__ == '__main__':
    app = InsertProcess()
    app.mainloop()
