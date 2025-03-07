from dataclasses import dataclass
from saludTech.seedwork.dominio.eventos import (EventoDominio)

class EventoModelosIA(EventoDominio):
    ...
@dataclass
class ImagenAnonimizadaValidada(EventoModelosIA):
    id: str = None
    url: str = None
    valida: bool = None

@dataclass
class ImagenAnonimizadaValidacionFallida(EventoModelosIA):
    id: str = None
    url: str = None
    valida: bool = None

@dataclass
class ImagenAnonimizadaValidacionRevertida(EventoModelosIA):
    id: str = None
    url: str = None
    valida: bool = None