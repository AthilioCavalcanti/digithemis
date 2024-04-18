import re
from errors import validacao_error, senha_error


class ValidacaoEntradas:
    @staticmethod
    def valida_email(email):
        # Regex para validar endereços de e-mail
        regex_email = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if re.match(regex_email, email):
            return True
        raise validacao_error.EmailInvalidoError()

    @staticmethod
    def valida_senha(senha):
        if len(senha) < 6:
            raise senha_error.SenhaCurtaError()

        if not re.search(r'[A-Z]', senha):
            raise senha_error.SenhaSemMaiusculaError()

        if not re.search(r'[a-z]', senha):
            raise senha_error.SenhaSemMinusculaError()

        if not re.search(r'\d', senha):
            raise senha_error.SenhaSemNumeroError()

        if not re.search(r'[^\w\s]', senha):
            raise senha_error.SenhaSemCaracterEspecialError()

        return True

    @staticmethod
    def valida_cpf_cnpj(cpf_cnpj):
        documento = ''.join(filter(str.isdigit, cpf_cnpj))

        if len(documento) == 11:
            if documento == documento[0] * 11:
                raise validacao_error.CPFInvalidoError()

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
                raise validacao_error.CPFInvalidoError()

        if len(documento) == 14:
            if documento == documento[0] * 14:
                raise validacao_error.CNPJInvalidoError()

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
                raise validacao_error.CNPJInvalidoError()

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
            raise validacao_error.NumeroProcessoInvalidoError()

    @staticmethod
    def valida_num_processo(num_processo):
        regex_num_processo = r'^\d{7}-\d{2}\.\d{4}\.8\.19\.\d{4}$'
        if re.match(regex_num_processo, num_processo):
            return True
        raise validacao_error.NumeroProcessoInvalidoError()

    @staticmethod
    def valida_oab(oab):
        regex = r'^[A-Z]{2}\d{3}\.\d{3}$'

        estados = [
            'AC',
            'AL',
            'AP',
            'AM',
            'BA',
            'CE',
            'DF',
            'ES',
            'GO',
            'MA',
            'MT',
            'MS',
            'MG',
            'PA',
            'PB',
            'PR',
            'PE',
            'PI',
            'RJ',
            'RN',
            'RS',
            'RO',
            'RR',
            'SC',
            'SP',
            'SE',
            'TO',
        ]
        if re.match(regex, oab):

            if oab[:2] in estados:
                return True
            else:
                return False
        else:
            return False
