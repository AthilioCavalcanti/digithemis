class NumeroProcessoInvalido(ValueError):
    def __init__(self, message='Número de processo inválido.'):
        self.mensagem = message
        super().__init__(self.mensagem)