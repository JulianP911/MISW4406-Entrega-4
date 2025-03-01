from modelosIA.seedwork.dominio.repositorios import Mapeador
from modelosIA.modulos.modelosIA.dominio.entidades import Dataframe
from uuid import UUID
from .despachadores import unix_time_millis
from .dto import Dataframe as DataframeDTO
import datetime


class MapeadorDataframe(Mapeador):
    def obtener_tipo(self) -> type:
        return Dataframe.__class__

    def entidad_a_dto(self, entidad: Dataframe) -> DataframeDTO:
        imagen_medica_dto = DataframeDTO()
        imagen_medica_dto.id = entidad.id
        imagen_medica_dto.url = entidad.url
        imagen_medica_dto.dataframe = entidad.dataframe

        return imagen_medica_dto

    def dto_a_entidad(self, dto: DataframeDTO) -> Dataframe:
        return Dataframe(
            id=dto["id"],
            url=dto["url"],
            dataframe=dto["dataframe"]
        )
