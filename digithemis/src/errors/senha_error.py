class SenhaCurta(ValueError):
    def __init__(self, message='A senha deve ter no mínimo 6 caracteres.'):
        self.mensagem = message
        super().__init__(self.mensagem)


class SenhaSemNumero(ValueError):
    def __init__(self, message='A senha deve conter pelo menos um dígito numérico.'):
        self.mensagem = message
        super().__init__(self.mensagem)


class SenhaSemMaiuscula(ValueError):
    def __init__(self, message='A senha deve conter pelo menos uma letra maiúscula.'):
        self.mensagem = message
        super().__init__(self.mensagem)