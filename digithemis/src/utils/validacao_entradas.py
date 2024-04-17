import re


class ValidacaoEntradas:
    @staticmethod
    def valida_email(email):
        # Regex para validar endereços de e-mail
        regex_email = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if re.match(regex_email, email):
            return True

        return False
    
    @staticmethod
    def valida_senha(senha):
        if len(senha) < 6:
            raise Exception('A senha deve ter no mínimo 6 caracteres')

        if not re.search(r'[A-Z]', senha):
            raise Exception(
                'A senha deve conter pelo menos uma letra maiúscula'
            )

        if not re.search(r'[a-z]', senha):
            raise Exception(
                'A senha deve conter pelo menos uma letra minúscula'
            )

        if not re.search(r'\d', senha):
            raise Exception('A senha deve conter pelo menos um dígito')

        if not re.search(r'[^\w\s]', senha):
            raise Exception(
                'A senha deve conter pelo menos um caractere especial'
            )

        return True