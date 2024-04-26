from config import ConexaoDB
from errors import RegistroExistenteError, RegistroNaoExistenteError
from models import Especialidade

class EspecialidadeService:
    def __init__(self) -> None:
        self.conexao = ConexaoDB()

    def cadastra_especialidade(self, tipo):
        with self.conexao as con:
            try:
                especialidade_existente = (
                    con.session.query(Especialidade)
                    .filter_by(tipo=tipo)
                    .first()
                )
                if especialidade_existente:
                    raise RegistroExistenteError('Especialidade já está cadastrada')
                else:
                    especialidade = Especialidade(tipo=tipo)
                    con.session.add(especialidade)
                    con.session.commit()
            except Exception as erro:
                con.session.rollback()
                raise erro

    def busca_especialidade(self, tipo):
        with self.conexao as con:
            especialidade = (
                con.session.query(Especialidade)
                .filter_by(tipo=tipo)
                .first()
            )
            return especialidade

    def lista_especialidades(self):
        with self.conexao as con:
            especialidades = con.session.query(Especialidade).all()
            return especialidades

    def remove_especialidade(self, tipo):
        with self.conexao as con:
            try:
                especialidade = (
                    con.session.query(Especialidade)
                    .filter_by(tipo=tipo)
                    .first()
                )
                if especialidade:
                    con.session.delete(especialidade)
                    con.session.commit()
                else:
                    raise RegistroNaoExistenteError('Especialidade não foi encontrada')
            except Exception as erro:
                con.session.rollback()
                raise erro
    
     # Método para viabilizar facilmente um usuário para teste
    def verificar_e_adicionar_especialidades_teste(self):
        with self.conexao as con:
            if con.session.query(Especialidade).count() == 0:
                tipos_especialidades = ['Civil', 'Penal', 'Previdenciário', 'Trabalhista']
                especialidades = []
                for especialidade in tipos_especialidades:
                    especialidades.append(Especialidade(tipo=especialidade))
                try:
                    con.session.add_all(especialidades)
                    con.session.commit()
                except Exception:
                    con.session.rollback()
