from saludTech.seedwork.aplicacion.comandos import Comando
from saludTech.modulos.gestor_archivos.aplicacion.dto import (
    ImagenMedicaDTO,
    MetadataDTO,
)
from .base import CrearImagenMedicaBaseHandler
from dataclasses import dataclass, field
from saludTech.seedwork.aplicacion.comandos import ejecutar_commando as comando

from saludTech.modulos.gestor_archivos.dominio.entidades import ImagenMedica
from saludTech.seedwork.infraestructura.uow import UnidadTrabajoPuerto
from saludTech.modulos.gestor_archivos.aplicacion.mapeadores import MapeadorImagenMedica
from saludTech.modulos.gestor_archivos.infraestructura.repositorios import (
    RepositorioImagenMedica,
)


@dataclass
class CrearImagenMedica(Comando):
    fecha_creacion: str
    fecha_actualizacion: str
    id: str
    url: str
    metadata: dict
    id_paciente: str
    bucket_location: str


class CrearImagenMedicaHandler(CrearImagenMedicaBaseHandler):

    def handle(self, comando: CrearImagenMedica):
        imagen_medica_dto = ImagenMedicaDTO(
            fecha_creacion=comando.fecha_creacion,
            fecha_actualizacion=comando.fecha_actualizacion,
            id=comando.id,
            url=comando.url,
            bucket_location=comando.bucket_location,
            metadata=MetadataDTO(
                tipo=comando.metadata.tipo,
                formato=comando.metadata.formato,
            ),
        )

        imagen_medica: ImagenMedica = self.fabrica_imagen_medica.crear_objeto(
            imagen_medica_dto, MapeadorImagenMedica()
        )

        imagen_medica.crear_imagen_medica(imagen_medica, comando.id_paciente)

        repositorio = self.fabrica_repositorio.crear_objeto(
            RepositorioImagenMedica.__class__
        )
        UnidadTrabajoPuerto.clean()
        UnidadTrabajoPuerto.registrar_batch(repositorio.agregar, imagen_medica)
        UnidadTrabajoPuerto.savepoint()
        UnidadTrabajoPuerto.commit()


@comando.register(CrearImagenMedica)
def ejecutar_comando_crear_imagen_medica(comando: CrearImagenMedica):
    handler = CrearImagenMedicaHandler()
    handler.handle(comando)
