from anonimizador.seedwork.aplicacion.dto import Mapeador as AppMap
from anonimizador.seedwork.dominio.repositorios import Mapeador as RepMap
from anonimizador.modulos.anonimizador.dominio.entidades import ImagenMedica
from .dto import ImagenMedicaDTO


class MapeadorAnonimizadorDTOJson(AppMap):
    def externo_a_dto(self, externo: dict) -> ImagenMedicaDTO:
        #print("externo a dto: "+externo)
        imagen_medica_dto = ImagenMedicaDTO(
            url=externo["url"],
            id=externo["id"],
            id_paciente=externo["id_paciente"]
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
        fecha_creacion = None
        fecha_actualizacion = entidad.fecha_actualizacion.strftime(self._FORMATO_FECHA)

        return ImagenMedicaDTO(
            entidad.id,
            entidad.id_paciente,
            entidad.url
        )

    def dto_a_entidad(self, dto: ImagenMedicaDTO) -> ImagenMedica:
        return ImagenMedica(
            id=dto.id,
            url=dto.url
        )
