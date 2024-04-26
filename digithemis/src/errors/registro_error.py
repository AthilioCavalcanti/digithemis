class RegistroExistenteError(Exception):
    def __init__(self, message='Registro já existente.'):
        self.mensagem = message
        super().__init__(self.mensagem)


class RegistroNaoExistenteError(Exception):
    def __init__(self, message='Registro não foi encontrado.'):
        self.mensagem = message
        super().__init__(self.mensagem)
