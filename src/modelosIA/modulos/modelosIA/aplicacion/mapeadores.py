from modelosIA.seedwork.aplicacion.dto import Mapeador as AppMap
from modelosIA.seedwork.dominio.repositorios import Mapeador as RepMap
from modelosIA.modulos.modelosIA.dominio.entidades import Dataframe
from .dto import DataframeDTO
import time

class MapeadorDataframeDTOJson(AppMap):
    def externo_a_dto(self, externo: dict) -> DataframeDTO:
        imagen_medica_dto = DataframeDTO(
            url=externo["url"],
            id=externo["id"]
        )

        return imagen_medica_dto

    def dto_a_externo(self, dto: DataframeDTO) -> dict:
        return dto.__dict__


class MapeadorDataframe(RepMap):

    def obtener_tipo(self) -> type:
        return Dataframe.__class__

    def entidad_a_dto(self, entidad: Dataframe) -> DataframeDTO:
        print("=========DESDE MAPEADOR DATAFRAME==========")
        print(entidad)
        print("=========DESDE MAPEADOR DATAFRAME==========")
        return DataframeDTO(
            entidad.id,
            entidad.url
        )

    def dto_a_entidad(self, dto: DataframeDTO) -> Dataframe:
        return Dataframe(
            id=dto.id,
            url=dto.url,
            dataframe='aaaa'
        )
