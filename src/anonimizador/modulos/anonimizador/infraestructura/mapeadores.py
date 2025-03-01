from anonimizador.seedwork.dominio.repositorios import Mapeador
from anonimizador.modulos.anonimizador.dominio.entidades import ImagenMedica
from uuid import UUID
from .despachadores import unix_time_millis
from .dto import ImagenMedica as ImagenMedicaDTO
import datetime


class MapeadorImagenMedica(Mapeador):
    def obtener_tipo(self) -> type:
        return ImagenMedica.__class__

    def entidad_a_dto(self, entidad: ImagenMedica) -> ImagenMedicaDTO:
        imagen_medica_dto = ImagenMedicaDTO()
        imagen_medica_dto.id = entidad.id
        imagen_medica_dto.url = entidad.url
        imagen_medica_dto.fecha_recepcion = entidad.fecha_recepcion
        imagen_medica_dto.accion = entidad.accion

        return imagen_medica_dto

    def dto_a_entidad(self, dto: ImagenMedicaDTO) -> ImagenMedica:
        return ImagenMedica(
            id=dto["id"],
            url=dto["url"],
        )
