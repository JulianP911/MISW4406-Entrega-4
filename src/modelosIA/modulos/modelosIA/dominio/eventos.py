from dataclasses import dataclass
from modelosIA.seedwork.dominio.eventos import EventoDominio
import uuid
from modelosIA.seedwork.infraestructura.utils import time_millis
from pulsar.schema import *

#@dataclass
class ImagenAnonimizadaValidada(Record):#TODO antes era EventoDominio
    id: str = None
    url: str = None
    valida: bool = None
    
#@dataclass
class ImagenAnonimizadaValidacionRevertida(Record):
    id: str = None
    url: str = None
    valida: bool = None

class EventoModelosIA(Record):
    id = String(default=str(uuid.uuid4()))
    time = Long()
    ingestion = Long(default=time_millis())
    specversion = String(default="v1")
    type = String(default="EventoModelosIA")
    datacontenttype = String()
    service_name = String(default="modelosIA.saludTech")
    archivo_publicacion_revertida = ImagenAnonimizadaValidacionRevertida
    archivo_publicado = ImagenAnonimizadaValidada

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)