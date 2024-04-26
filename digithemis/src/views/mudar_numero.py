from tkinter import Tk, Canvas, Entry, Button, PhotoImage, Frame, messagebox
from pathlib import Path
from controllers import AdvogadoController
from errors import TelefoneInvalidoError


class AplicativoMudadorNumero:
    def __init__(self):
        super().__init__()
        self.janela = Tk()
        self.centralize()
        self.janela.configure(bg='#81A69F')

        self.controlador = AdvogadoController()

        self.canvas = Canvas(
            self.janela,
            bg='#81A69F',
            height=641,
            width=1007,
            bd=0,
            highlightthickness=0,
            relief='ridge',
        )
        self.canvas.place(x=0, y=0)

        self.caminho_relativo_assets = self._caminho_relativo_assets

        self.janela.title('Mudar número de telefone')
        self.janela.iconbitmap(f'{self.caminho_relativo_assets('favicon.ico')}')

        self.create_images()
        self.create_entry()
        self.create_buttons()

        self.janela.resizable(False, False)
        self.janela.mainloop()

    def _caminho_relativo_assets(self, path):
        diretorio_atual = Path(__file__).parent
        assets_dir = diretorio_atual / 'assets'
        return assets_dir / path

    def centralize(self):
        from .app import App

        App.centralize_app(self.janela)

    def create_images(self):
        posicoes_imagens = [
            (503.0, 320.0),  # Imagem 1
            (503.0, 27.0),  # Imagem 2
        ]
        arquivos_imagens = [
            'mudar_numero_image_1.png',
            'mudar_numero_image_2.png',
        ]
        self.imagens = []
        for posicao, caminho_imagem in zip(posicoes_imagens, arquivos_imagens):
            imagem = PhotoImage(
                file=self.caminho_relativo_assets(caminho_imagem)
            )
            self.imagens.append(imagem)
            self.canvas.create_image(*posicao, image=imagem)

    def create_entry(self):
        imagem_entrada = PhotoImage(
            file=self.caminho_relativo_assets('mudar_numero_entry_1.png')
        )
        fundo_entrada = self.canvas.create_image(
            504.0, 303.5, image=imagem_entrada
        )
        entrada_frame = Frame(self.janela, bg='#FFFFFF', padx=10)
        entrada_frame.place(x=285.0, y=280.0, width=418.0, height=45.0)
        entrada = Entry(bd=0, bg='#FFFFFF', fg='#000716', highlightthickness=0)
        entrada.place(x=295.0, y=280.0, width=418.0, height=45.0)

        self.canvas.create_text(
            295.0,
            260.0,
            anchor='nw',
            text='NÚMERO:',
            fill='#FFFFFF',
            font=('HammersmithOne Regular', 15 * -1),
        )

        from .app import App

        entrada.insert(0, App.load_user_state()['contato'])

        self.entrada_numero = entrada

    def create_buttons(self):
        informacoes_botoes = [
            (378.0, 414.0, 'mudar_numero_button_1.png', self.botao_1_clicado),
            (17.0, 17.0, 'mudar_numero_button_2.png', self.botao_2_clicado),
        ]
        for informacao in informacoes_botoes:
            self.create_button(*informacao)

    def create_button(self, x, y, caminho_imagem, comando):
        imagem_botao = PhotoImage(
            file=self.caminho_relativo_assets(caminho_imagem)
        )
        botao = Button(
            self.janela,
            image=imagem_botao,
            command=comando,
            bd=0,
            highlightthickness=0,
            relief='flat',
        )
        botao.image = imagem_botao
        botao.place(x=x, y=y)

    # Funções associadas a cada botão
    def botao_1_clicado(self):
        numero_telefone = self.entrada_numero.get()
        if numero_telefone:
            try:
                from .app import App

                if App.load_user_state()['contato'] == numero_telefone:
                    messagebox.showwarning(
                        'Notificação',
                        'Atualize seu número antes de tentar alterar.',
                    )
                else:
                    cpf = App.load_user_state()['cpf']
                    self.controlador.atualizar_telefone_advogado(
                        cpf, numero_telefone
                    )
                    messagebox.showinfo(
                        'Notificação', 'Número atualizado com sucesso!'
                    )
                    App.update_user_state('contato', numero_telefone)
            except TelefoneInvalidoError as erro:
                messagebox.showerror('Notificação', f'{erro}')
        else:
            messagebox.showwarning(
                'Notificação', 'Preencha o campo de número de telefone.'
            )

    def botao_2_clicado(self):
        self.janela.destroy()
        from .editar_perfil import EditProfileApp

        edit = EditProfileApp()


if __name__ == '__main__':
    app = AplicativoMudadorNumero(1)
