from dataclasses import dataclass
from saludTech.seedwork.dominio.eventos import (EventoDominio)

class EventoValidadorAnonimizador(EventoDominio):
    ...

@dataclass
class ArchivoPublicado(EventoValidadorAnonimizador):
    id: str = None
    url: str = None
    
@dataclass
class ArchivoPublicacionFallida(EventoValidadorAnonimizador):
    id: str = None
    url: str = None

@dataclass
class ArchivoPublicacionRevertida(EventoValidadorAnonimizador):
    id: str = None
    url: str = None