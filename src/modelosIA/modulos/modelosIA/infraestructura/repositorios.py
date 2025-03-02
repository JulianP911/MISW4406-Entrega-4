from modelosIA.config.db import db
from modelosIA.modulos.modelosIA.dominio.repositorios import (
    RepositorioDataframe,
)
from modelosIA.modulos.modelosIA.dominio.entidades import Dataframe
from modelosIA.modulos.modelosIA.dominio.fabricas import FabricaDataframe
from .dto import Dataframe as ImagenMedicaDTO
from .mapeadores import MapeadorDataframe
from uuid import UUID


class RepositorioDataframeSQLite(RepositorioDataframe):

    def __init__(self):
        self._fabrica_dataframe: FabricaDataframe = FabricaDataframe()

    @property
    def fabrica_dataframe(self):
        return self._fabrica_dataframe

    def agregar(self, entity: Dataframe):
        dataframe_dto = self._fabrica_dataframe(entity, MapeadorDataframe())
        db.session.add(dataframe_dto)

    def obtener_todos(self) -> list[Dataframe]:
        pass

    def obtener_por_id(self, id: UUID) -> Dataframe:
        pass

    def actualizar(self, entity: Dataframe):
        pass

    def eliminar(self, entity_id: UUID):
        pass
