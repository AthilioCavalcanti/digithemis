from pathlib import Path
import tkinter as tk
from tkinter import Canvas, Entry, Button, PhotoImage, Frame


class ChangeOABApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.centralize()
        self.configure(bg='#81A69F')
        self.output_path = Path(__file__).parent
        self.assets_path = self.output_path / 'assets'
        self.title('Mudar OAB')
        self.iconbitmap(f'{self.relative_to_assets('favicon.ico')}')

        self.create_widgets()
