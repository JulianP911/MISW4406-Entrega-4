from __future__ import annotations
from dataclasses import dataclass, field
import uuid

import anonimizador.modulos.anonimizador.dominio.objeto_valor as ov
from anonimizador.seedwork.dominio.entidades import AgregacionRaiz
from .eventos import ImagenAnonimizada


@dataclass
class ImagenMedica(AgregacionRaiz):
    id: uuid.UUID = field(hash=True, default=None)
    url: str = field(default=None)

    def crear_imagen_medica(self, imagenMedica: ImagenMedica):
        self.id = imagenMedica.id
        self.url = imagenMedica.url

        self.agregar_evento(ImagenAnonimizada(id=self.id, url=self.url))
