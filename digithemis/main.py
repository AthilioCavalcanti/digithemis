import sys

sys.path.append('./src')
from config import ConexaoDB
from models import Base
from views import App


def connection(engine):
    Base.metadata.create_all(engine, checkfirst=True)


try:
    connection(ConexaoDB().engine)

    App()


except Exception as erro:
    print(erro)
