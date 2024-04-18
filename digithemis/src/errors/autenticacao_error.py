class CredenciaisInvalida(Exception):
    def __init__(self, message='Credenciais inválidas.'):
        self.mensagem = message
        super().__init__(self.mensagem)
