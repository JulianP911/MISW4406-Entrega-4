from dataclasses import dataclass
from anonimizador.seedwork.dominio.eventos import EventoDominio


@dataclass
class ImagenAnonimizada(EventoDominio):
    id: str = None
    url: str = None
    token_paciente: str = None
