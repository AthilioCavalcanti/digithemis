from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage, Scrollbar, Text


class AplicativoPerfilAdvogado:
    def __init__(self):
        self.janela = Tk()
        self.centralize()
        self.janela.configure(bg='#81A69F')

        self.canvas = Canvas(
            self.janela,
            bg='#81A69F',
            height=650,
            width=600,
            bd=0,
            highlightthickness=0,
            relief='ridge',
        )
        self.canvas.place(x=0, y=0)

        self.caminho_relativo_assets = self._caminho_relativo_assets

        self.janela.title('Perfil')
        self.janela.iconbitmap(f'{self.caminho_relativo_assets('favicon.ico')}')

        self.criar_imagens()
        self.criar_botoes()
        self.criar_quadro_informacoes()
        self.exibir_informacoes()

        self.janela.resizable(False, False)
        self.janela.mainloop()

    def _caminho_relativo_assets(self, path):
        diretorio_atual = Path(__file__).parent
        assets_dir = diretorio_atual / 'assets'
        return assets_dir / path

    def centralize(self):
        from .app import App

        App.centralize_app(self.janela, 600, 650)

    def criar_imagens(self):
        posicoes_imagens = [
            (300.0, 21.0),  # Imagem 1
            (300.0, 334.0),  # Imagem 2
        ]
        arquivos_imagens = [
            'perfil_advogado_image_1.png',
            'perfil_advogado_image_2.png',
        ]
        self.imagens = []
        for posicao, caminho_imagem in zip(posicoes_imagens, arquivos_imagens):
            imagem = PhotoImage(
                file=self.caminho_relativo_assets(caminho_imagem)
            )
            self.imagens.append(imagem)
            self.canvas.create_image(*posicao, image=imagem)

    def criar_botoes(self):
        info_botoes = [
            (18.0, 14.0, 'perfil_advogado_button_1.png', self.botao_1_clicado),
            (
                352.0,
                561.0,
                'perfil_advogado_button_2.png',
                self.botao_2_clicado,
            ),
        ]
        for informacao in info_botoes:
            self.criar_botao(*informacao)

    def criar_botao(self, x, y, caminho_imagem, comando):
        imagem_botao = PhotoImage(
            file=self.caminho_relativo_assets(caminho_imagem)
        )
        botao = Button(
            self.janela,
            image=imagem_botao,
            borderwidth=0,
            highlightthickness=0,
            command=comando,
            relief='flat',
        )
        botao.image = imagem_botao
        botao.place(
            x=x, y=y, width=imagem_botao.width(), height=imagem_botao.height()
        )

    # Funções associadas a cada botão
    def botao_1_clicado(self):
        self.janela.destroy()
        from .app import App

        usuario = App.load_user_state()
        if usuario['admin']:
            from .menu_admin import AdminApp

            menu_admin = AdminApp()

        if not usuario['admin']:
            from .menu_advogado import Menu_advogadoapp

            menu_advogado = Menu_advogadoapp()

    def botao_2_clicado(self):
        self.janela.destroy()
        from .editar_perfil import EditProfileApp

        editar = EditProfileApp()

    def criar_quadro_informacoes(self):
        self.informacoes_frame = Canvas(
            self.janela, bg='white', bd=0, highlightthickness=0
        )
        self.informacoes_frame.place(x=50, y=100, width=500, height=400)

        self.scrollbar = Scrollbar(
            self.informacoes_frame,
            orient='vertical',
            command=self.informacoes_frame.yview,
        )
        self.scrollbar.pack(side='right', fill='y')

        self.informacoes_texto = Text(
            self.informacoes_frame,
            wrap='word',
            yscrollcommand=self.scrollbar.set,
            font=('Arial', 20),
        )
        self.informacoes_texto.pack(side='left', fill='both', expand=True)

    def exibir_informacoes(self):
        from .app import App

        usuario_infos = App.load_user_state()

        self.informacoes_texto.tag_configure(
            'bold', font=('Arial', 25, 'bold')
        )

        titulos = ['Nome:', 'Email:', 'OAB:', 'Telefone:', 'CPF:']
        infos = [
            usuario_infos['nome'],
            usuario_infos['email'],
            usuario_infos['oab'],
            usuario_infos['contato'],
            usuario_infos['cpf'],
        ]
        for titulo, info in zip(titulos, infos):
            self.informacoes_texto.insert('end', titulo, 'bold')
            self.informacoes_texto.insert('end', f' {info}\n\n')


if __name__ == '__main__':
    app = AplicativoPerfilAdvogado()
