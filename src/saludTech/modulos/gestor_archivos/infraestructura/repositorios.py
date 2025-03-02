from saludTech.config.db import db
from saludTech.modulos.gestor_archivos.dominio.repositorios import (
    RepositorioImagenMedica,
)
from saludTech.modulos.gestor_archivos.dominio.entidades import ImagenMedica
from saludTech.modulos.gestor_archivos.dominio.fabricas import FabricaImagenMedica
from .dto import ImagenMedica as ImagenMedicaDTO
from .mapeadores import MapeadorImagenMedica
from uuid import UUID


class RepositorioImageneMedicaSQLite(RepositorioImagenMedica):

    def __init__(self):
        self._fabrica_imagen_medica: FabricaImagenMedica = FabricaImagenMedica()

    @property
    def fabrica_imagen_medica(self):
        return self._fabrica_imagen_medica

    def agregar(self, entity: ImagenMedica):
        imagen_medica_dto = self.fabrica_imagen_medica(entity, MapeadorImagenMedica())
        db.session.add(imagen_medica_dto)

    def obtener_todos(self) -> list[ImagenMedica]:
        imagenes_medicas = db.session.query(ImagenMedicaDTO).all()
        imagenes_medicas_dto = []
        for imagen_medica in imagenes_medicas:
            imagenes_medicas_dto.append(
                self.fabrica_imagen_medica(imagen_medica, MapeadorImagenMedica())
            )
        return imagenes_medicas_dto

    def obtener_por_id(self, id: UUID) -> ImagenMedica:
        pass

    def actualizar(self, entity: ImagenMedica):
        pass

    def eliminar(self, entity_id: UUID):
        pass
