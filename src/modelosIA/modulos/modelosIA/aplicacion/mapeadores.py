from modelosIA.seedwork.aplicacion.dto import Mapeador as AppMap
from modelosIA.seedwork.dominio.repositorios import Mapeador as RepMap
from modelosIA.modulos.modelosIA.dominio.entidades import Dataframe
from .dto import ImagenAnonimizadaValidadDTO
import time

class MapeadorDataframeDTOJson(AppMap):
    def externo_a_dto(self, externo: dict) -> ImagenAnonimizadaValidadDTO:
        imagen_medica_dto = ImagenAnonimizadaValidadDTO(
            url=externo["url"],
            id=externo["id"]
        )

        return imagen_medica_dto

    def dto_a_externo(self, dto: ImagenAnonimizadaValidadDTO) -> dict:
        return dto.__dict__


class MapeadorDataframe(RepMap):

    def obtener_tipo(self) -> type:
        return Dataframe.__class__

    def entidad_a_dto(self, entidad: Dataframe) -> ImagenAnonimizadaValidadDTO:
        print("=========DESDE MAPEADOR DATAFRAME==========")
        print(entidad)
        print("=========DESDE MAPEADOR DATAFRAME==========")
        return ImagenAnonimizadaValidadDTO(
            entidad.id,
            entidad.url
        )

    def dto_a_entidad(self, dto: ImagenAnonimizadaValidadDTO) -> Dataframe:
        return Dataframe(
            id=dto.id,
            url=dto.url,
            dataframe='dataframe'
        )
