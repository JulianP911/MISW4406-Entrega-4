from modelosIA.seedwork.aplicacion.servicios import Servicio
from modelosIA.modulos.modelosIA.dominio.entidades import Dataframe
from modelosIA.modulos.modelosIA.infraestructura.repositorios import (
    RepositorioDataframe,
)
from modelosIA.modulos.modelosIA.dominio.fabricas import (
    FabricaDateframe,
)
from modelosIA.modulos.modelosIA.infraestructura.fabricas import (
    FabricaRepositorio,
)

from modelosIA.seedwork.infraestructura.uow import UnidadTrabajoPuerto as uow

from .dto import ImagenAnonimizadaValidadDTO
from .mapeadores import MapeadorDataframe

import asyncio

class ServicioImagenMedica(Servicio):

    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_dataframe: FabricaDateframe = FabricaDateframe()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio

    @property
    def fabrica_dataframe(self):
        return self._fabrica_dataframe

    def crear_imagen_medica(self, imagen_dto: ImagenAnonimizadaValidadDTO) -> ImagenAnonimizadaValidadDTO:

        print("===========imagen_dto===========")
        print(imagen_dto)
        print("===========imagen_dto===========")

        dataframe: Dataframe = self.fabrica_dataframe.crear_objeto(
            imagen_dto,
            MapeadorDataframe(),
        )

        print("===========dataframe===========")
        print(dataframe)
        print("===========dataframe===========")

        dataframe.crear_dataframe(dataframe)

        repositorio = self.fabrica_repositorio.crear_objeto(
            RepositorioDataframe.__class__
        )
        print("===========ANTES DE MORIR===========")
        print(dataframe)
        print("===========ANTES DE MORIR===========")
        uow.clean()  # TODO Eliminar cuando funcione todo
        uow.registrar_batch(repositorio.agregar, dataframe)
        uow.savepoint()
        uow.commit()

        return self.fabrica_dataframe.crear_objeto(
            dataframe, MapeadorDataframe()
        )
