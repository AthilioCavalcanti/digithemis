class NumeroProcessoInvalidoError(ValueError):
    def __init__(self, message='Número de processo inválido.'):
        self.mensagem = message
        super().__init__(self.mensagem)


class CPFInvalidoError(ValueError):
    def __init__(self, message='Número de CPF inválido.'):
        self.mensagem = message
        super().__init__(self.mensagem)


class CNPJInvalidoError(ValueError):
    def __init__(self, message='Número de CNPJ inválido.'):
        self.mensagem = message
        super().__init__(self.mensagem)


class EmailInvalidoError(ValueError):
    def __init__(self, message='Formato de e-mail inválido.'):
        self.mensagem = message
        super().__init__(self.mensagem)


class OABInvalidaError(ValueError):
    def __init__(self, message='OAB inválida.'):
        self.mensagem = message
        super().__init__(self.mensagem)


class TelefoInvalidoError(ValueError):
    def __init__(self, message='Número de telefone inválido.'):
        self.mensagem = message
        super().__init__(self.mensagem)
