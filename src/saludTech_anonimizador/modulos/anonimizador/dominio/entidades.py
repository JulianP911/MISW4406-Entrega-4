from __future__ import annotations
from dataclasses import dataclass, field
import uuid

from saludTech_anonimizador.seedwork.dominio.entidades import AgregacionRaiz
from .eventos import ArchivoPublicado


@dataclass
class ImagenMedica(AgregacionRaiz):
    id: uuid.UUID = field(hash=True, default=None)
    url: str = field(default=None)
    validated: bool = field(default=False)
    fecha_creacion: str = field(default=None)

    def crear_imagen_medica(self, imagenMedica: ImagenMedica):
        self.id = imagenMedica.id
        self.url = imagenMedica.url
        self.validated = imagenMedica.validated
        self.fecha_creacion = imagenMedica.fecha_creacion

        self.agregar_evento(ArchivoPublicado(id=self.id, url=self.url))
