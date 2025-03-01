from anonimizador.seedwork.aplicacion.dto import Mapeador as AppMap
from anonimizador.seedwork.dominio.repositorios import Mapeador as RepMap
from anonimizador.modulos.anonimizador.dominio.entidades import ImagenMedica
from .dto import ImagenMedicaDTO
import time

class MapeadorAnonimizadorDTOJson(AppMap):
    def externo_a_dto(self, externo: dict) -> ImagenMedicaDTO:
        #print("externo a dto: "+externo)
        imagen_medica_dto = ImagenMedicaDTO(
            url=externo["url"],
            id=externo["id"]
        )

        return imagen_medica_dto

    def dto_a_externo(self, dto: ImagenMedicaDTO) -> dict:
        return dto.__dict__


class MapeadorImagenMedica(RepMap):

    def obtener_tipo(self) -> type:
        return ImagenMedica.__class__

    def entidad_a_dto(self, entidad: ImagenMedica) -> ImagenMedicaDTO:
        print("=========DESDE MAPEADOR IMAGEN MEDICA==========")
        print(entidad)
        print("=========DESDE MAPEADOR IMAGEN MEDICA==========")
        return ImagenMedicaDTO(
            entidad.id,
            entidad.url
        )

    def dto_a_entidad(self, dto: ImagenMedicaDTO) -> ImagenMedica:
        return ImagenMedica(
            id=dto.id,
            url=dto.url,
            fecha_recepcion=time.time()
        )
