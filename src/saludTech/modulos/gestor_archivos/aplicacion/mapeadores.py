from saludTech.seedwork.aplicacion.dto import Mapeador as AppMap
from saludTech.seedwork.dominio.repositorios import Mapeador as RepMap
from saludTech.modulos.gestor_archivos.dominio.entidades import ImagenMedica
from saludTech.modulos.gestor_archivos.dominio.objeto_valor import Metadata
from .dto import MetadataDTO, ImagenMedicaDTO
import uuid
from saludTech.config.rules import get_bucket_location


class MapeadorImagenMedicaDTOJson(AppMap):
    def externo_a_dto(self, externo: dict) -> ImagenMedicaDTO:
        bucket_location = get_bucket_location(externo["url"])
        imagen_medica_dto = ImagenMedicaDTO(
            url=externo["url"],
            id=str(uuid.uuid4()),
            bucket_location=bucket_location,
            metadata=MetadataDTO(
                tipo=externo["metadata"]["tipo"],
                formato=externo["metadata"]["formato"],
            ),
        )

        return imagen_medica_dto

    def dto_a_externo(self, dto: ImagenMedicaDTO) -> dict:
        return dto.__dict__


class MapeadorImagenMedica(RepMap):
    _FORMATO_FECHA = "%Y-%m-%dT%H:%M:%SZ"

    def _procesar_metadata(self, metadata_dto: MetadataDTO) -> Metadata:
        return Metadata(metadata_dto.tipo, metadata_dto.formato)

    def obtener_tipo(self) -> type:
        return ImagenMedica.__class__

    def entidad_a_dto(self, entidad: ImagenMedica) -> ImagenMedicaDTO:
        fecha_creacion = None
        fecha_actualizacion = entidad.fecha_actualizacion.strftime(self._FORMATO_FECHA)

        return ImagenMedicaDTO(
            entidad.id,
            entidad.url,
            metadata=entidad.metadata,
            fecha_actualizacion=fecha_actualizacion,
            fecha_creacion=fecha_creacion,
            bucket_location=entidad.bucket_location,
        )

    def dto_a_entidad(self, dto: ImagenMedicaDTO) -> ImagenMedica:
        return ImagenMedica(
            id=dto.id,
            url=dto.url,
            bucket_location=dto.bucket_location,
            metadata=MetadataDTO(
                dto.metadata.tipo,
                dto.metadata.formato,
            ),
        )
