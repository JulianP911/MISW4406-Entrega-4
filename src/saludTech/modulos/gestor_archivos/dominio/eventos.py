from dataclasses import dataclass
from saludTech.seedwork.dominio.eventos import EventoDominio
import uuid


@dataclass
class ArchivoPublicado(EventoDominio):
    id: str = None
    url: str = None
    id_paciente: str = None

@dataclass
class ArchivoPublicacionFallida(EventoDominio):
    id: str = None
    url: str = None
    id_paciente: str = None

@dataclass
class ArchivoPublicacionRevertida(EventoDominio):
    id: str = None
    url: str = None
    id_paciente: str = None