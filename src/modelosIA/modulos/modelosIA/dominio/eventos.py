from dataclasses import dataclass
from modelosIA.seedwork.dominio.eventos import EventoDominio
import uuid


@dataclass
class ImagenAnonimizadaValidada(EventoDominio):
    id: str = None
    url: str = None
    valida: bool = None
