from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage


class EsqueciSenhaApp:
    def __init__(self):
        self.window = Tk()
        self.centralize()
        self.window.configure(bg='#81A69F')

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

        self.window.title('Recuperação de senha')
        self.window.iconbitmap(f'{self.get_assets_path()}\\favicon.ico')

        self.create_widgets()

        self.window.resizable(False, False)
        self.window.mainloop()

    def get_assets_path(self):
        current_dir = Path(__file__).parent
        assets_path = current_dir / 'assets'
        return assets_path
    
    def centralize(self):
        from .app import App

        App.centralize_app(self.window)

    def create_widgets(self):
        self.create_canvas()
        self.create_entry()
        self.create_buttons()

    def create_canvas(self):
        background_image = PhotoImage(
            file=self.assets_path / 'esqueci_senha_image_1.png'
        )
        self.canvas.create_image(503.0, 320.0, image=background_image)
        self.canvas.background = background_image

        second_image = PhotoImage(
            file=self.assets_path / 'esqueci_senha_image_2.png'
        )
        self.canvas.create_image(503.0, 27.0, image=second_image)
        self.canvas.second_image = second_image

    def create_entry(self):
        entry_image = PhotoImage(
            file=self.assets_path / 'esqueci_senha_entry_1.png'
        )
        entry_bg = self.canvas.create_image(504.0, 330.5, image=entry_image)
        self.entry = Entry(
            bd=0, bg='#FFFFFF', fg='#000716', highlightthickness=0
        )
        self.entry.place(x=295.0, y=307.0, width=418.0, height=45.0)

        self.canvas.create_text(
            306.0,
            287.0,
            anchor='nw',
            text='EMAIL:',
            fill='#FFFFFF',
            font=('HammersmithOne Regular', 15 * -1),
        )

    def create_buttons(self):
        button_info = [
            (
                378.0,
                387.0,
                252.0,
                61.0,
                'esqueci_senha_button_1.png',
                self.button_1_clicked,
            ),
            (
                17.0,
                17.0,
                20.0,
                20.0,
                'esqueci_senha_button_2.png',
                self.button_2_clicked,
            ),
        ]
        for info in button_info:
            self.create_button(*info)

    def create_button(self, x, y, width, height, image_path, command):
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
        button.place(x=x, y=y, width=width, height=height)

    def button_2_clicked(self):
        self.window.destroy()
        from .login import LoginApp

        login_tela = LoginApp()

    def button_1_clicked(self):
        print('button_2 clicked')


if __name__ == '__main__':
    app = EsqueciSenhaApp()
