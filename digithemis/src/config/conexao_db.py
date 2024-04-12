from dotenv import load_dotenv
from sqlalchemy import create_engine


env = load_dotenv()


class ConexaoDB:
    def __init__(self):
        self.__string_conexao = (
            f'postgresql://{env["DB_USER"]}:{env["DB_PASSWORD"]}'
            f'@{env["DB_HOST"]}:{env["DB_PORT"]}/{env["DB_NAME"]}'
        )
        self.__engine = self.__criar_engine()

    def __criar_engine(self):
        try:
            engine = create_engine(self.__string_conexao)
            return engine
        except Exception as erro:
            raise erro

    @property
    def engine(self):
        return self.__engine