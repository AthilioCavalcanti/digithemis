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
