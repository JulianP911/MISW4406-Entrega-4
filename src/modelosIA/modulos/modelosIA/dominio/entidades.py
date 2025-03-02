from __future__ import annotations
from dataclasses import dataclass, field
import uuid
import time
from modelosIA.seedwork.dominio.entidades import AgregacionRaiz

@dataclass
class Dataframe(AgregacionRaiz):
    id: uuid.UUID = field(hash=True, default=None)
    url: str = field(default=None)
    dataframe: str = field(default=None)

    def crear_dataframe(self, dataframe: Dataframe):
        self.id = dataframe.id
        self.url = dataframe.url
        self.dataframe = dataframe.dataframe

