from dataclasses import dataclass
from saludTech.seedwork.dominio.eventos import (EventoDominio)

class EventoAnonimizador(EventoDominio):
    ...

@dataclass
class ImagenAnonimizada(EventoAnonimizador):
    id: str = None
    url: str = None
    token_paciente: str = None

class ImagenAnonimizacionFallida(EventoAnonimizador):
    id: str = None
    url: str = None
    token_paciente: str = None

class ImagenAnonimizacionRevertida(EventoAnonimizador):
    id: str = None
    url: str = None
    token_paciente: str = None