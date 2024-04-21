from config import ConexaoDB
from errors import RegistroNaoExistenteError
from models import Documento, Cliente


class DocumentoService:
    def __init__(self) -> None:
        self.conexao = ConexaoDB()

    def insere_documento(self, id_cliente, titulo, categoria, arquivo):
        with self.conexao as con:
            try:
                cliente = (
                    con.session.query(Cliente)
                    .filter_by(id_cliente=id_cliente)
                    .first()
                )
                if cliente:
                    documento = Documento(
                        id_cliente=id_cliente,
                        titulo=titulo,
                        categoria=categoria,
                        arquivo=arquivo,
                    )
                    con.session.add(documento)
                    con.session.commit()
                else:
                    raise Exception('Cliente não existe')
            except Exception as erro:
                con.session.rollback()
                raise erro

    def busca_documentos(self, **kwargs):
        with self.conexao as con:
            chave, valor = next(iter(kwargs.items()))

            if chave == 'id_cliente' or chave == 'categoria':
                documentos = (
                    con.session.query(Documento)
                    .filter(
                        Documento.id_cliente == valor
                        if chave == 'id_cliente'
                        else Documento.categoria == valor
                    )
                    .all()
                )
                if documentos:
                    return documentos
                else:
                    raise Exception(
                        'Não foram encontrados documentos para o cliente pesquisado'
                    )

            atributo = Documento.titulo

            if chave == 'id_documento':
                atributo = Documento.id_documento

            documento = (
                con.session.query(Documento).filter(atributo == valor).all()
            )

            if documento:
                return documento
            else:
                raise Exception(
                    'Não foi encontrato nenhum documento com o valor informado'
                )

    def lista_documentos(self):
        with self.conexao as con:
            documentos = con.session.query(Documento).all()
            return documentos

    def atualiza_documento(self, id_documento, campo, valor):
        with self.conexao as con:
            try:
                documento = self.busca_documentos(id_documento=id_documento)
                campos = ['id_cliente', 'titulo']
                if documento[0]:
                    if campo in campos:
                        con.session.query(Documento).filter(
                            Documento.id_documento == id_documento
                        ).update({campo: valor})
                    else:
                        raise ValueError('Campo inválido')
                    con.session.commit()
                else:
                    raise RegistroNaoExistenteError(
                        'Documento não foi encontrado'
                    )
            except Exception as erro:
                con.session.rollback()
                raise erro

    def remove_documento(self, id_documento):
        with self.conexao as con:
            try:
                documento = self.busca_documentos(id_documento=id_documento)
                if documento:
                    con.session.query(Documento).filter(
                        Documento.id_documento == id_documento
                    ).delete()
                    con.session.commit()
                else:
                    raise RegistroNaoExistenteError(
                        'Documento não foi encontrado'
                    )
            except Exception as erro:
                con.session.rollback()
                raise erro
            
    def buscar_documento_por_titulo(self, titulo):
        with self.conexao as con:
            try:
                documento = con.session.query(Documento).filter(Documento.titulo == titulo).first()
                return documento
            except Exception as e:
                return None