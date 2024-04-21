from services import EspecialidadeService


class EspecialidadeController:
    def __init__(self):
        self.especialidade = EspecialidadeService()

    def lista_especialidades(self):
        especialidades = []
        for especialidade in self.especialidade.lista_especialidades():
            especialidades.append(especialidade.tipo)
        return especialidades
