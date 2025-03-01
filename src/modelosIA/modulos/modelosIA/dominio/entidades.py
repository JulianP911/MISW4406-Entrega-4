from __future__ import annotations
from dataclasses import dataclass, field
import uuid
import time
from anonimizador.seedwork.dominio.entidades import AgregacionRaiz
from .eventos import ImagenAnonimizada
from datetime import datetime

@dataclass
class Dataframe(AgregacionRaiz):
    id: uuid.UUID = field(hash=True, default=None)
    url: str = field(default=None)
    dataframe: str = field(default=None)

    def crear_dataframe(self, dataframe: Dataframe, accion: str):
        self.id = dataframe.id
        self.url = dataframe.url
        self.dataframe = dataframe.dataframe
        self.agregar_evento(ImagenAnonimizada(id=self.id, url=self.url))
