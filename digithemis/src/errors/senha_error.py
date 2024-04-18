class SenhaCurta(ValueError):
    def __init__(self, message='A senha deve ter no mínimo 6 caracteres.'):
        self.mensagem = message
        super().__init__(self.mensagem)