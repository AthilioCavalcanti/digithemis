class NumeroProcessoInvalido(ValueError):
    def __init__(self, message='Número de processo inválido.'):
        self.mensagem = message
        super().__init__(self.mensagem)


class CPFInvalido(ValueError):
    def __init__(self, message='Número de CPF inválido.'):
        self.mensagem = message
        super().__init__(self.mensagem)


class CNPJInvalido(ValueError):
    def __init__(self, message='Número de CNPJ inválido.'):
        self.mensagem = message
        super().__init__(self.mensagem)
