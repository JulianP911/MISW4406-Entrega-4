from anonimizador.seedwork.aplicacion.servicios import Servicio
from anonimizador.modulos.anonimizador.dominio.entidades import ImagenMedica
from anonimizador.modulos.anonimizador.infraestructura.repositorios import (
    RepositorioImagenMedica,
)
from anonimizador.modulos.anonimizador.dominio.fabricas import (
    FabricaImagenMedica,
)
from anonimizador.modulos.anonimizador.infraestructura.fabricas import (
    FabricaRepositorio,
)

from anonimizador.seedwork.infraestructura.uow import UnidadTrabajoPuerto as uow

from .dto import ImagenMedicaDTO
from .mapeadores import MapeadorImagenMedica

import asyncio


class ServicioImagenMedica(Servicio):

    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_imagen_medica: FabricaImagenMedica = FabricaImagenMedica()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio

    @property
    def fabrica_imagenes_medicas(self):
        return self._fabrica_imagen_medica

    def crear_imagen_medica(self, imagen_dto: ImagenMedicaDTO) -> ImagenMedicaDTO:

        imagen_medica: ImagenMedica = self.fabrica_imagenes_medicas.crear_objeto(
            imagen_dto,
            MapeadorImagenMedica(),
        )

        imagen_medica.crear_imagen_medica(imagen_medica, "ANONIMIZAR")

        repositorio = self.fabrica_repositorio.crear_objeto(
            RepositorioImagenMedica.__class__
        )
        uow.clean()  # TODO Eliminar cuando funcione todo
        uow.registrar_batch(repositorio.agregar, imagen_medica)
        uow.savepoint()
        uow.commit()

        return self.fabrica_imagenes_medicas.crear_objeto(
            imagen_medica, MapeadorImagenMedica()
        )
