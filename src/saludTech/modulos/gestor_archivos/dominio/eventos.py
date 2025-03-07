from dataclasses import dataclass
from saludTech.seedwork.dominio.eventos import EventoDominio
import uuid
from saludTech.seedwork.infraestructura.schema.v1.eventos import EventoIntegracion

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

