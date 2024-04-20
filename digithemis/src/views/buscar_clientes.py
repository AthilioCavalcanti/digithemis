from pathlib import Path
import tkinter as tk
from tkinter import (
    Canvas,
    Entry,
    Button,
    PhotoImage,
    Frame,
    Scrollbar,
    Listbox,
    messagebox,
    Toplevel,
    Label,
)
from controllers import AdvogadoController, ClienteController


class SearchApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.centralize()
        self.configure(bg='#81A69F')
        self.output_path = Path(__file__).parent
        self.assets_path = self.output_path / 'assets'
        self.title('Buscar clientes')
        self.iconbitmap(f'{self.relative_to_assets('favicon.ico')}')

        self.controlador_adv = AdvogadoController()
        self.controlador_cliente = ClienteController()

        # Lista para pesquisa
        from .app import App
        # Quando limitar por especialidade
        # self.search_data = (
        #     self.controlador_cliente.listar_clientes_especialidade(
        #         self.controlador_adv.especialidade_advogado(
        #             App.load_user_state()['cpf']
        #         )
        #     )
        # )
        self.search_data = self.controlador_cliente.listar_clientes()

        self.create_widgets()

    def relative_to_assets(self, path: str) -> Path:
        return self.assets_path / Path(path)

    def centralize(self):
        from .app import App

        App.centralize_app(self)

    def create_widgets(self):
        self.create_canvas()
        self.create_entries()
        self.create_buttons()
        self.create_results_display()

    def create_canvas(self):
        self.canvas = Canvas(
            self,
            bg='#81A69F',
            height=641,
            width=1007,
            bd=0,
            highlightthickness=0,
            relief='ridge',
        )
        self.canvas.place(x=0, y=0)

        # Adiciona a imagem de fundo ao canvas
        background_image = PhotoImage(
            file=self.relative_to_assets('buscar_clientes_image_1.png')
        )
        self.canvas.create_image(0, 0, anchor=tk.NW, image=background_image)
        self.canvas.background = (
            background_image  # Mantém a referência à imagem de fundo
        )

        # Adiciona a segunda imagem ao canvas
        second_image = PhotoImage(
            file=self.relative_to_assets('buscar_clientes_image_2.png')
        )
        self.canvas.create_image(503.0, 27.0, image=second_image)
        self.canvas.second_image = (
            second_image  # Mantém a referência à segunda imagem
        )

        # Adiciona a caixa em branco
        self.canvas.create_rectangle(
            228.0, 302.0, 780.0, 592.0, fill='#FFFFFF', outline=''
        )

    def create_entries(self):
        self.entry_1 = self.create_entry(
            295.0, 228.0, 418.0, 45.0, 'BUSCAR CLIENTE:'
        )
        self.bind_entry(self.entry_1)

    def create_entry(self, x, y, width, height, label_text):
        entry_image = PhotoImage(
            file=self.relative_to_assets('buscar_clientes_entry_1.png')
        )
        entry_bg = self.canvas.create_image(504.0, 251.5, image=entry_image)
        entry_frame = Frame(self, bg='#FFFFFF', padx=10)
        entry_frame.place(x=x - 10, y=y, width=418.0, height=45.0)
        entry = Entry(
            self, bd=0, bg='#FFFFFF', fg='#000716', highlightthickness=0
        )
        entry.place(x=x, y=y, width=width, height=height)
        self.canvas.create_text(
            x,  # Offset para alinhar com a entrada
            y - 23,  # Offset para alinhar com a entrada
            anchor='nw',
            text=label_text,
            fill='#FFFFFF',
            font=('HammersmithOne Regular', 15 * -1),
        )
        return entry

    def bind_entry(self, entry):
        entry.bind('<Return>', lambda event: self.process_search())

    def create_buttons(self):
        self.create_button(
            22.0,
            12.0,
            25.0,
            30.0,
            'buscar_clientes_button_1.png',
            self.button_1_clicked,
        )

    def create_button(self, x, y, width, height, image_path, command):
        button_image = PhotoImage(file=self.relative_to_assets(image_path))
        button = Button(
            image=button_image,
            borderwidth=0,
            highlightthickness=0,
            command=command,
            relief='flat',
        )
        button.image = (
            button_image  # Garante que a imagem seja mantida em memória
        )
        button.place(x=x, y=y, width=width, height=height)

    def create_results_display(self):
        # Adiciona um frame para conter os resultados
        self.results_frame = Frame(self.canvas, bg='#FFFFFF')
        self.results_frame.place(x=250, y=350, width=530, height=240)

        # Adiciona uma lista para os resultados com uma barra de rolagem
        self.result_listbox = Listbox(
            self.results_frame,
            bg='#FFFFFF',
            bd=0,
            fg='#000000',
            font=('Arial', 12),
        )
        self.result_listbox.pack(side='left', fill='both', expand=True)

        # Adiciona uma barra de rolagem para a lista
        self.scrollbar = Scrollbar(
            self.results_frame,
            orient='vertical',
            command=self.result_listbox.yview,
        )
        self.scrollbar.pack(side='right', fill='y')

        # Configura a barra de rolagem para controlar a lista
        self.result_listbox.configure(yscrollcommand=self.scrollbar.set)

        # Adiciona o evento de clique para os resultados
        self.result_listbox.bind(
            '<Double-Button-1>', self.handle_result_double_click
        )

    def process_search(self):
        query = self.entry_1.get()  # Obtém o texto digitado
        # Aqui você pode pesquisar na lista
        results = [
            result
            for result in self.search_data
            if query.lower() in result['nome'].lower()
        ]
        self.display_results(results)

    def display_results(self, results):
        # Limpa os resultados anteriores
        self.result_listbox.delete(0, 'end')

        # Exibe os resultados na lista
        for result in results:
            self.result_listbox.insert('end', f'{result['nome']} - CPF/CNPJ: {result['cpf_cnpj']}')

    def handle_result_double_click(self, event):
        # Obtém o item clicado na lista
        index = self.result_listbox.curselection()[0]
        item = self.result_listbox.get(index)
        item_cpf_cnpj = item.split(' ')[-1]
        cliente = self.controlador_cliente.buscar_cliente(item_cpf_cnpj)

        self.destroy()
        from .detalhes_cliente import AplicativoPerfilCliente

        detalhes_cliente = AplicativoPerfilCliente(cliente)

    def button_1_clicked(self):
        self.destroy()
        from .app import App

        usuario = App.load_user_state()
        if usuario['admin']:
            from .menu_admin import AdminApp

            menu_admin = AdminApp()

        if not usuario['admin']:
            from .menu_advogado import Menu_advogadoapp

            menu_advogado = Menu_advogadoapp()

    # def button_add_docs_clicked(self):
    #     print('Buscando e cadastrando docs...')


if __name__ == '__main__':
    app = SearchApp()
    app.mainloop()
