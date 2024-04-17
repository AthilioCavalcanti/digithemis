import re


class ValidacaoEntradas:
    @staticmethod
    def valida_email(email):
        # Regex para validar endereços de e-mail
        regex_email = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if re.match(regex_email, email):
            return True

        return False