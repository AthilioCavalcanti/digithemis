from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage


class EditProfileApp:
    def __init__(self):
        super().__init__()
        self.janela = Tk()
        self.centralize()
        self.janela.configure(bg="#81A69F")

        self.canvas = Canvas(
            self.janela,
            bg="#81A69F",
            height=641,
            width=1007,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.canvas.place(x=0, y=0)

        self.caminho_relativo_assets = self._caminho_relativo_assets

        self.janela.title('Buscar clientes')
        self.janela.iconbitmap(f'{self.caminho_relativo_assets('favicon.ico')}')

        self.create_images()
        self.create_buttons()

        self.janela.resizable(False, False)
        self.janela.mainloop()

    def _caminho_relativo_assets(self, path):
        diretorio_atual = Path(__file__).parent
        assets_dir = diretorio_atual / "assets"
        return assets_dir / path
    
    def centralize(self):
        from .app import App

        App.centralize_app(self.janela)

    def create_images(self):
        posicoes_imagens = [
            (503.0, 320.0),  # Imagem 1
            (503.0, 27.0)    # Imagem 2
        ]
        arquivos_imagens = [
            "editar_perfil_image_1.png",
            "editar_perfil_image_2.png"
        ]
        self.imagens = []
        for posicao, caminho_imagem in zip(posicoes_imagens, arquivos_imagens):
            imagem = PhotoImage(file=self.caminho_relativo_assets(caminho_imagem))
            self.imagens.append(imagem)
            self.canvas.create_image(*posicao, image=imagem)

    def create_buttons(self):
        self.create_button(437.0, 209.0, "editar_perfil_button_1.png", self.botao_1_clicado)
        self.create_button(598.0, 400.0, "editar_perfil_button_2.png", self.botao_2_clicado)
        self.create_button(283.0, 400.0, "editar_perfil_button_3.png", self.botao_3_clicado)
        self.create_button(127.0, 209.0, "editar_perfil_button_4.png", self.botao_4_clicado)
        self.create_button(747.0, 209.0, "editar_perfil_button_5.png", self.botao_5_clicado)
        self.create_button(17.0, 17.0, "editar_perfil_button_6.png", self.botao_6_clicado, width=25, height=30)

    def create_button(self, x, y, caminho_imagem, comando, width=134, height=125):
        imagem_botao = PhotoImage(file=self.caminho_relativo_assets(caminho_imagem))
        botao = Button(
            self.canvas,
            image=imagem_botao,
            borderwidth=0,
            highlightthickness=0,
            command=comando,
            relief="flat"
        )
        botao.image = imagem_botao
        botao.place(x=x, y=y, width=width, height=height)

    # Funções associadas a cada botão
    def botao_1_clicado(self):
        self.janela.destroy()
        from .mudar_email import ChangeEmailApp
        editar = ChangeEmailApp()

    def botao_2_clicado(self):
        self.janela.destroy()
        # from mudar_numero import AplicativoMudadorNumero
        # editar = AplicativoMudadorNumero(self.user)

    def botao_3_clicado(self):
        self.janela.destroy()
        from .mudar_oab import ChangeOABApp
        editar = ChangeOABApp()

    def botao_4_clicado(self):
        self.janela.destroy()
        from .mudar_nome import ChangeNameApp
        editar = ChangeNameApp()

    def botao_5_clicado(self):
        self.janela.destroy()
        from .mudar_senha import ChangePasswordApp
        editar = ChangePasswordApp()

    def botao_6_clicado(self):
        self.janela.destroy()
        from .app import App

        usuario = App.load_user_state()
        if usuario['admin']:
            from .menu_admin import AdminApp

            menu_admin = AdminApp()

        if not usuario['admin']:
            from .menu_advogado import Menu_advogadoapp

            menu_advogado = Menu_advogadoapp()


if __name__ == "__main__":
    pass