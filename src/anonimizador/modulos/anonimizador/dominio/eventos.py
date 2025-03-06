from dataclasses import dataclass
import uuid
from anonimizador.seedwork.dominio.eventos import EventoDominio
from anonimizador.seedwork.infraestructura.utils import time_millis
from pulsar.schema import *

#@dataclass
class ImagenAnonimizada(Record):#TODO antes era EventoDominio
    id: str = None
    url: str = None
    token_paciente: str = None
    
#@dataclass
class ImagenAnonimizacionRevertida(Record):
    id: str = None
    url: str = None
    token_paciente: str = None

class EventoAnonimizador(Record):
    id = String(default=str(uuid.uuid4()))
    time = Long()
    ingestion = Long(default=time_millis())
    specversion = String(default="v1")
    type = String(default="EventoAnonimizador")
    datacontenttype = String()
    service_name = String(default="anonimizador.saludTech")
    archivo_publicacion_revertida = ImagenAnonimizacionRevertida
    archivo_publicado = ImagenAnonimizada

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)