from .autenticacao_error import CredenciaisInvalidaError
from .registro_error import RegistroExistenteError, RegistroNaoExistenteError
from .senha_error import (
    SenhaCurtaError,
    SenhaSemCaracterEspecialError,
    SenhaSemMaiusculaError,
    SenhaSemMinusculaError,
    SenhaSemNumeroError,
)
from .validacao_error import (
    EmailInvalidoError,
    CPFInvalidoError,
    CNPJInvalidoError,
    TelefoInvalidoError,
    OABInvalidaError,
    NumeroProcessoInvalidoError,
)
