from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage


class EsqueciSenhaApp:
    def __init__(self):
        self.window = Tk()
        self.window.geometry('1007x641')
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

        self.create_widgets()

        self.window.resizable(False, False)
        self.window.mainloop()

    