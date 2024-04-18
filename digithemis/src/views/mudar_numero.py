from tkinter import Tk, Canvas, Entry, Button, PhotoImage
from pathlib import Path

class AplicativoMudadorNumero:
    def __init__(self,user:bool):
        super().__init__()
        self.user = user
        self.janela = Tk()
        self.janela.geometry("1007x641")
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

        self.create_images()
        self.create_entry()
        self.create_buttons()

        self.janela.resizable(False, False)
        self.janela.mainloop()

    def _caminho_relativo_assets(self, path):
        diretorio_atual = Path(__file__).parent
        assets_dir = diretorio_atual / "assets"
        return assets_dir / path

    def create_images(self):
        posicoes_imagens = [
            (503.0, 320.0),  # Imagem 1
            (503.0, 27.0)    # Imagem 2
        ]
        arquivos_imagens = [
            "mudar_numero_image_1.png",
            "mudar_numero_image_2.png"
        ]
        self.imagens = []
        for posicao, caminho_imagem in zip(posicoes_imagens, arquivos_imagens):
            imagem = PhotoImage(file=self.caminho_relativo_assets(caminho_imagem))
            self.imagens.append(imagem)
            self.canvas.create_image(*posicao, image=imagem)

    def create_entry(self):
        imagem_entrada = PhotoImage(file=self.caminho_relativo_assets("mudar_numero_entry_1.png"))
        fundo_entrada = self.canvas.create_image(504.0, 303.5, image=imagem_entrada)
        entrada = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        entrada.place(x=295.0, y=280.0, width=418.0, height=45.0)

        self.canvas.create_text(
            306.0,
            260.0,
            anchor="nw",
            text="NOVO NÚMERO:",
            fill="#FFFFFF",
            font=("HammersmithOne Regular", 15 * -1)
        )

    def create_buttons(self):
        informacoes_botoes = [
            (378.0, 414.0, "mudar_numero_button_1.png", self.botao_1_clicado),
            (17.0, 17.0, "mudar_numero_button_2.png", self.botao_2_clicado)
        ]
        for informacao in informacoes_botoes:
            self.create_button(*informacao)

    def create_button(self, x, y, caminho_imagem, comando):
        imagem_botao = PhotoImage(file=self.caminho_relativo_assets(caminho_imagem))
        botao = Button(
            self.janela,
            image=imagem_botao,
            command=comando,
            bd=0,
            highlightthickness=0,
            relief="flat"
        )
        botao.image = imagem_botao
        botao.place(x=x, y=y)

    # Funções associadas a cada botão
    def botao_1_clicado(self):
        print("Botão 1 clicado")

    def botao_2_clicado(self):
        self.janela.destroy()
        from editar_perfil import AplicativoEditorPerfil
        edit = AplicativoEditorPerfil(self.user)


if __name__ == "__main__":
    app = AplicativoMudadorNumero(1)
