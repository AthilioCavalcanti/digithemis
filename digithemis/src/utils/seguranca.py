import bcrypt


class Seguranca:
    @staticmethod
    def criptografa_senha(senha):
        sal = bcrypt.gensalt()
        hashed_senha = bcrypt.hashpw(senha.encode('utf-8'), sal)
        return hashed_senha

    @staticmethod
    def verifica_senha(senha, hashed_senha):
        return bcrypt.checkpw(senha.encode('utf-8'), hashed_senha)
