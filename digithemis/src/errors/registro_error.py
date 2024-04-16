class RegistroExistenteError(Exception):
    def __init__(self, message='Registro já existente.'):
        self.mensagem = message
        super().__init__(self.mensagem)
