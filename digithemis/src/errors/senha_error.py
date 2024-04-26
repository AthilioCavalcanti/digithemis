class SenhaCurtaError(ValueError):
    def __init__(self, message='A senha deve ter no mínimo 6 caracteres.'):
        self.mensagem = message
        super().__init__(self.mensagem)


class SenhaSemNumeroError(ValueError):
    def __init__(
        self, message='A senha deve conter pelo menos um dígito numérico.'
    ):
        self.mensagem = message
        super().__init__(self.mensagem)


class SenhaSemMaiusculaError(ValueError):
    def __init__(
        self, message='A senha deve conter pelo menos uma letra maiúscula.'
    ):
        self.mensagem = message
        super().__init__(self.mensagem)


class SenhaSemMinusculaError(ValueError):
    def __init__(
        self, message='A senha deve conter pelo menos uma letra minúscula.'
    ):
        self.mensagem = message
        super().__init__(self.mensagem)


class SenhaSemCaracterEspecialError(ValueError):
    def __init__(
        self, message='A senha deve conter pelo menos um caractere especial.'
    ):
        self.mensagem = message
        super().__init__(self.mensagem)
