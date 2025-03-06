from dataclasses import dataclass
from validador_anonimizador.seedwork.dominio.eventos import EventoDominio
from pulsar.schema import *
import uuid

from validador_anonimizador.seedwork.infraestructura.utils import time_millis

#@dataclass
class ArchivoPublicado(Record):#TODO antes era EventoDominio
    id: str = None
    url: str = None

#@dataclass
class ArchivoPublicacionRevertida(Record):
    id: str = None
    url: str = None

class EventoValidadorAnonimizacion(Record):
    id = String(default=str(uuid.uuid4()))
    time = Long()
    ingestion = Long(default=time_millis())
    specversion = String(default="v1")
    type = String(default="EventoValidadorAnonimizacion")
    datacontenttype = String()
    service_name = String(default="validador_anonimizador.saludTech")
    archivo_publicacion_revertida = ArchivoPublicacionRevertida
    archivo_publicado = ArchivoPublicado

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)