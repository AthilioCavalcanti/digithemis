import sys

sys.path.append('./src')
from config import ConexaoDB
from models import Base
from views import App
from services import AdvogadoService


def connection(engine):
    Base.metadata.create_all(engine, checkfirst=True)


try:
    connection(ConexaoDB().engine)

    # Método para viabilizar um usuário para testes, apenas para fiz didáticos
    AdvogadoService().verificar_e_adicionar_usuario_teste()

    App()


except Exception as erro:
    print(erro)
