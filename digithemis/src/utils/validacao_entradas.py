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
    
    @staticmethod
    def valida_cpf_cnpj(cpf_cnpj):
        documento = ''.join(filter(str.isdigit, cpf_cnpj))

        if len(documento) == 11:
            if documento == documento[0] * 11:
                raise Exception('Formato inválido')

            soma, multiplicador = 0, 10
            nove_primeiros_digitos = documento[:-2]

            for digito in nove_primeiros_digitos:
                soma += int(digito) * multiplicador
                multiplicador -= 1

            if soma % 11 < 2:
                dv1 = '0'
            else:
                dv1 = str(11 - soma % 11)

            dez_primeiros_digitos = nove_primeiros_digitos + dv1

            soma, multiplicador = 0, 11

            for digito in dez_primeiros_digitos:
                soma += int(digito) * multiplicador
                multiplicador -= 1

            if soma % 11 < 2:
                dv2 = '0'
            else:
                dv2 = str(11 - soma % 11)

            cpf = dez_primeiros_digitos + dv2

            if cpf == documento:
                return True
            else:
                raise Exception('Formato Inválido')

        if len(documento) == 14:
            if documento == documento[0] * 14:
                raise Exception('Formato inválido')

            soma, multiplicador = 0, 5
            doze_primeiros_digitos = documento[:-2]

            for digito in doze_primeiros_digitos:
                if multiplicador == 1:
                    multiplicador = 9
                soma += int(digito) * multiplicador
                multiplicador -= 1

            if soma % 11 < 2:
                dv1 = '0'
            else:
                dv1 = str(11 - soma % 11)

            treze_primeiros_digitos = doze_primeiros_digitos + dv1

            soma, multiplicador = 0, 6

            for digito in treze_primeiros_digitos:
                if multiplicador == 1:
                    multiplicador = 9
                soma += int(digito) * multiplicador
                multiplicador -= 1

            if soma % 11 < 2:
                dv2 = '0'
            else:
                dv2 = str(11 - soma % 11)

            cnpj = treze_primeiros_digitos + dv2

            if cnpj == documento:
                return True
            else:
                raise Exception('Formato inválido')

        raise Exception('Formato inválido')
    
    @staticmethod
    def formata_numero_processo(num_processo):
        match = re.match(
            r'^(\d{7})(\d{2})(\d{4})(\d)(\d{2})(\d{4})$', num_processo
        )
        if match:
            numero_formatado = '-'.join(
                [
                    match.group(1),
                    match.group(2)
                    + '.'
                    + match.group(3)
                    + '.'
                    + match.group(4)
                    + '.'
                    + match.group(5)
                    + '.'
                    + match.group(6),
                ]
            )
            return numero_formatado
        else:
            raise Exception('Formato inválido')