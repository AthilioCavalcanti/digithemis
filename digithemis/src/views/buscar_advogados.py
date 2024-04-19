from pathlib import Path
import tkinter as tk
from tkinter import (
    Canvas,
    Entry,
    Button,
    Scrollbar,
    PhotoImage,
    Listbox,
    messagebox,
    Frame,
)
from controllers import AdvogadoController


class SearchApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.centralize()
        self.configure(bg='#81A69F')
        self.output_path = Path(__file__).parent
        self.assets_path = self.output_path / 'assets'
        self.title('Buscar advogados')
        self.iconbitmap(f'{self.relative_to_assets('favicon.ico')}')
        self.controlador = AdvogadoController()

        # Altera lista aqui ou talvez fazer no método que lida com o enter
        self.advogados = self.controlador.listar_advogados()

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
            file=self.relative_to_assets('buscar_advogados_image_1.png')
        )
        self.canvas.create_image(0, 0, anchor=tk.NW, image=background_image)
        self.canvas.background = (
            background_image  # Mantém a referência à imagem de fundo
        )

        # Adiciona a segunda imagem ao canvas
        second_image = PhotoImage(
            file=self.relative_to_assets('buscar_advogados_image_2.png')
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
            295.0, 228.0, 418.0, 45.0, 'BUSCAR ADVOGADOS:'
        )
        self.bind_entry(self.entry_1)

    def create_entry(self, x, y, width, height, label_text):
        entry_image = PhotoImage(
            file=self.relative_to_assets('buscar_advogados_entry_1.png')
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
            'buscar_advogados_button_1.png',
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
        self.results_frame = tk.Frame(self.canvas, bg='#FFFFFF')
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
        # Aqui você pode pesquisar na lista de advogados e seus clientes associados
        results = [
            advogado
            for advogado in self.advogados
            if query.lower() in advogado['nome'].lower()
        ]
        self.display_results(results)

    def display_results(self, results):
        # Limpa os resultados anteriores
        self.result_listbox.delete(0, tk.END)

        # Exibe os resultados na lista
        for advogado in results:
            self.result_listbox.insert(tk.END, advogado['nome'])

    def handle_result_double_click(self, event):
        # Obtém o item clicado na lista
        index = self.result_listbox.curselection()[0]
        advogado = self.result_listbox.get(index)

        # Encontra os clientes associados ao advogado clicado
        for a in self.advogados:
            if a['nome'] == advogado:
                clientes = a['clientes']
                break

        # Exibe os clientes em uma nova janela
        self.show_clients_window(advogado, clientes)

    def show_clients_window(self, advogado, clientes):
        clients_window = tk.Toplevel(self)
        clients_window.title(f'Clientes do advogado {advogado}')
        clients_window.iconbitmap(f'{self.relative_to_assets('favicon.ico')}')
        from .app import App
        App.centralize_app(clients_window, 400, 300)
        clients_window.configure(bg='#81A69F')

        advogado_label = tk.Label(
            clients_window,
            text=f'Nome do Advogado: {advogado}',
            bg='#81A69F',
            fg='white',
            font=('Arial', 12, 'bold'),
        )
        advogado_label.pack(pady=10)

        # Adiciona uma barra de rolagem para a lista de clientes
        scrollbar = Scrollbar(clients_window)
        scrollbar.pack(side='right', fill='y')

        # Cria uma lista para os clientes com rolagem
        client_listbox = Listbox(
            clients_window,
            bg='#FFFFFF',
            bd=0,
            fg='#000000',
            font=('Arial', 10),
            yscrollcommand=scrollbar.set,
        )
        for cliente in clientes:
            client_listbox.insert(tk.END, cliente) # Aqui _________________________________________
        client_listbox.pack(side='left', fill='both', expand=True)

        scrollbar.config(command=client_listbox.yview)

        # Adiciona o evento de clique para cada cliente
        if clientes:
            client_listbox.bind(
                '<Double-Button-1>',
                lambda event, adv=advogado, cli=client_listbox: self.handle_client_click(
                    adv, cli
                ),
            )

    def handle_client_click(self, advogado, cliente):
        # Aqui você pode adicionar a lógica para exibir detalhes específicos do cliente
        selected_index = cliente.curselection()[0]
        selected_cliente = cliente.get(selected_index)
        messagebox.showinfo(
            'Detalhes do cliente',
            f'Detalhes do cliente {selected_cliente} do advogado {advogado}',
        )
    
    

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


if __name__ == '__main__':
    app = SearchApp()
    app.mainloop()
