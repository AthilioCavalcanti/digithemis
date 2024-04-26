import json
import os
from tkinter import Tk
from .login import LoginApp
from .menu_advogado import Menu_advogadoapp
from .menu_admin import AdminApp
from utils import GerenciamentoDiretorios


class App:
    def __init__(self):
        if self.user_state_exists():
            self.show_menu_page()
        else:
            self.show_login_page()
        GerenciamentoDiretorios.criar_diretorio('digithemis')

    def show_login_page(self):
        LoginApp()

    def show_menu_page(self):
        usuario = self.load_user_state()
        if usuario['admin']:
            AdminApp()
        else:
            Menu_advogadoapp()

    @staticmethod
    def centralize_app(window, width=1007, height=641):
        window_width = width
        window_height = height

        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()

        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        window.geometry(f'{window_width}x{window_height}+{x}+{y}')

    @staticmethod
    def user_state_exists():
        file_name = './user_state.json'
        file_path = os.path.abspath(file_name)
        return True if os.path.exists(file_path) else False

    @staticmethod
    def delete_user_state():
        file_path = './user_state.json'
        if os.path.exists(file_path):
            os.remove(file_path)
        else:
            print("O arquivo 'user_state.json' não existe.")

    @staticmethod
    def load_user_state():
        file_name = './user_state.json'
        file_path = os.path.abspath(file_name)
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as file:
                usuario = json.load(file)
            return usuario
        else:
            return None

    @staticmethod
    def update_user_state(field, value):
        user_state = App.load_user_state()
        fields = ['nome', 'email', 'oab', 'contato']
        if user_state and field in fields:
            user_state[field] = value
            file_name = './user_state.json'
            file_path = os.path.abspath(file_name)
            with open(file_path, 'w', encoding='utf-8') as file:
                json.dump(user_state, file, ensure_ascii=False)
            return True
        else:
            return False


if __name__ == '__main__':
    app = Menu_advogadoapp()
    app.root.mainloop()
