from __future__ import annotations
from dataclasses import dataclass, field
import uuid
import time
from anonimizador.seedwork.dominio.entidades import AgregacionRaiz
from .eventos import ImagenAnonimizada
from datetime import datetime

@dataclass
class ImagenMedica(AgregacionRaiz):
    id: uuid.UUID = field(hash=True, default=None)
    url: str = field(default=None)
    fecha_recepcion: int = field(default_factory=lambda: int(time.time()))
    accion: str = field(default=None)

    def crear_imagen_medica(self, imagenMedica: ImagenMedica, accion: str):
        self.id = imagenMedica.id
        self.url = imagenMedica.url
        #self.fecha_recepcion = datetime.now().timestamp()
        self.accion = accion
        self.agregar_evento(ImagenAnonimizada(id=self.id, url=self.url))
