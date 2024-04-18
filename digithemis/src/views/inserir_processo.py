from pathlib import Path
import tkinter as tk
from tkinter import Canvas, Button, PhotoImage, filedialog

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

    