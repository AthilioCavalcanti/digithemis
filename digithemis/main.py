import sys

sys.path.append('./src')
from config import ConexaoDB
from models import Base
from views import App
from services import AdvogadoService, EspecialidadeService


def connection(engine):
    Base.metadata.create_all(engine, checkfirst=True)


try:
    connection(ConexaoDB().engine)

    # Métodos para viabilizar um usuário e especilidades para
    # testes, apenas para fins didáticos
    EspecialidadeService().verificar_e_adicionar_especialidades_teste()
    AdvogadoService().verificar_e_adicionar_usuario_teste()

    App()


except Exception as erro:
    print(erro)
