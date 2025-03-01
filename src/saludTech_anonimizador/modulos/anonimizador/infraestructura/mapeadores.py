from saludTech_anonimizador.seedwork.dominio.repositorios import Mapeador
from saludTech_anonimizador.modulos.anonimizador.dominio.entidades import ImagenMedica
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
        imagen_medica_dto.fecha_creacion = entidad.fecha_creacion
        return imagen_medica_dto

    def dto_a_entidad(self, dto: ImagenMedicaDTO) -> ImagenMedica:
        return ImagenMedica(
            id=UUID(dto["id"]),
            url=dto["url"],
            fecha_creacion=dto["fecha_creacion"],
        )
