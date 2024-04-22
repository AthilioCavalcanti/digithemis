from pathlib import Path
from tkinter import (
    Tk,
    Canvas,
    Button,
    PhotoImage,
    Scrollbar,
    Text,
    Label,
    Frame,
    filedialog,
    Toplevel,
    ttk,
)
from controllers import ClienteController
from utils import OCR


class AplicativoPerfilCliente:
    def __init__(self, cliente=None):
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

        self.janela.title('Detalhes Cliente')
        self.janela.iconbitmap(f'{self.caminho_relativo_assets('favicon.ico')}')

        self.cliente = cliente
        self.controlador_cliente = ClienteController()

        self.criar_imagens()
        self.criar_botoes()
        self.criar_quadro_informacoes()
        self.criar_quadro_docs()
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
                342.0,
                561.0,
                'cliente_atualizar_button.png',
                self.botao_2_clicado,
            ),
            (
                52.0,
                561.0,
                'cliente_carregar_docs_button.png',
                self.botao_3_clicado,
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
        print('Ir para janela de edição de dados de cliente')

    def criar_quadro_informacoes(self):
        self.informacoes_frame = Canvas(
            self.janela, bg='white', bd=0, highlightthickness=0
        )
        self.informacoes_frame.place(x=50, y=50, width=500, height=220)

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
            font=('Arial', 16),
        )
        self.informacoes_texto.pack(side='left', fill='both', expand=True)

    def criar_quadro_docs(self):
        label = Label(
            self.janela, text=f'Documentos de {self.cliente['nome']}:', bg='#80A59E', font=('Arial', 12, 'bold')
        )
        label.place(x=50, y=290)
        
        documentos = self.controlador_cliente.busca_documentos_cliente(
            self.cliente['cpf_cnpj']
        )

        frame = Frame(self.janela)
        frame.place(x=50, y=320, width=500, height=180)

        canvas = Canvas(frame, bg='white', bd=0, highlightthickness=0)
        canvas.pack(side='left', fill='both', expand=True)
        
        scrollbar = Scrollbar(frame, orient='vertical', command=canvas.yview)
        scrollbar.pack(side='right', fill='y')

        canvas.configure(yscrollcommand=scrollbar.set)

        inner_frame = Frame(canvas, bg='white')
        canvas.create_window((0, 0), window=inner_frame, anchor='nw')

        text = Text(
            inner_frame,
            wrap='word',
            width=80,
            height=10,
            cursor='arrow',
            font=('Arial', 12, 'bold'),
        )
        text.pack(fill='both', expand=True)

        if documentos:
            for documento in documentos:
                text.insert(
                    'end',
                    f"{documento['titulo']} ---- Data: {documento['insercao']}\n",
                    f"link_{documento['titulo']}",
                )
                text.tag_bind(
                    f"link_{documento['titulo']}",
                    '<Button-1>',
                    lambda event, doc=documento: self.document_clicked(doc),
                )
            text.config(fg='blue', state='disabled')
        else:
            text.insert('end', 'Sem documentos registrados')
            text.config(fg='gray', state='disabled')

        inner_frame.update_idletasks()
        canvas.config(scrollregion=canvas.bbox('all'))

    def exibir_informacoes(self):
        self.informacoes_texto.tag_configure(
            'bold', font=('Arial', 16, 'bold')
        )

        titulos = ['Nome:', 'CPF:', 'Email:', 'Telefone:', 'Empresa:']
        infos = [
            self.cliente['nome'],
            self.cliente['cpf_cnpj'],
            self.cliente['email'],
            self.cliente['contato'],
            'SIM' if self.cliente['empresa'] else 'NÃO',
        ]
        for titulo, info in zip(titulos, infos):
            self.informacoes_texto.insert('end', titulo, 'bold')
            self.informacoes_texto.insert('end', f' {info}\n')
        self.informacoes_texto.config(fg='black', state='disabled')

    def document_clicked(self, doc):
        import webbrowser
        import os
        caminho_base = os.path.expanduser('~/digithemis')
        diretorio_cliente = self.controlador_cliente._remover_acentos(self.cliente['nome']) 
        caminho_cliente = os.path.join(caminho_base, diretorio_cliente)
        caminho_arquivo = os.path.join(caminho_cliente, f'{doc['titulo']}{doc['categoria']}')

        try:
            webbrowser.open(caminho_arquivo)
        except Exception as e:
            print(f"Erro ao abrir o arquivo: {e}")

    def botao_3_clicado(self):
        import threading

        caminho_diretorio = filedialog.askdirectory()
        popup_carregamento = self.popup_carregamento('Carregando documentos...')

        def carregar_documentos():
            docs = OCR.buscar_palavra_em_pdf_imagens(caminho_diretorio, self.cliente['nome'].upper())
            self.controlador_cliente.salvar_documentos_cliente(
                self.cliente['cpf_cnpj'], docs
            )
            if docs:
                self.criar_quadro_docs()
            
            popup_carregamento.destroy()

        linha_execucao = threading.Thread(target=carregar_documentos)
        linha_execucao.start()

    def popup_carregamento(self, texto):
        popup = Toplevel(self.janela)
        popup.title("Aguarde")
        from .app import App
        App.centralize_app(popup, 400, 200)
        popup.iconbitmap(f'{self.caminho_relativo_assets('favicon.ico')}')
        
        label = ttk.Label(popup, text=texto, font=('Arial', 14))
        label.pack(pady=10)
        
        progress = ttk.Progressbar(popup, mode='indeterminate')
        progress.pack(pady=10)
        progress.start()
        
        popup.grab_set()
        return popup


if __name__ == '__main__':
    app = AplicativoPerfilCliente()
