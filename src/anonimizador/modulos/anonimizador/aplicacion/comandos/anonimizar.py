from anonimizador.seedwork.aplicacion.comandos import Comando
from anonimizador.modulos.anonimizador.aplicacion.dto import ImagenMedicaDTO
from .base import CrearImagenMedicaBaseHandler
from dataclasses import dataclass, field
from anonimizador.seedwork.aplicacion.comandos import ejecutar_commando as comando

from anonimizador.modulos.anonimizador.dominio.entidades import ImagenMedica
from anonimizador.seedwork.infraestructura.uow import UnidadTrabajoPuerto
from anonimizador.modulos.anonimizador.aplicacion.mapeadores import MapeadorImagenMedica
from anonimizador.modulos.anonimizador.infraestructura.repositorios import RepositorioImageneMedicaSQLite

@dataclass
class CrearImagenMedica(Comando):
    id: str
    url: str
    id_paciente: str

class CrearImagenMedicaHandler(CrearImagenMedicaBaseHandler):
    
    def handle(self, comando: CrearImagenMedica):
        imagen_medica_dto = ImagenMedicaDTO(
                id=comando.id
            ,   id_paciente=comando.id_paciente
            ,   url=comando.url)

        imagen_medica: ImagenMedica = self.fabrica_imagen_medica.crear_objeto(imagen_medica_dto, MapeadorImagenMedica())
        imagen_medica.crear_imagen_medica(imagen_medica)

        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioImageneMedicaSQLite)

        UnidadTrabajoPuerto.registrar_batch(repositorio.agregar, imagen_medica)
        UnidadTrabajoPuerto.commit()


@comando.register(CrearImagenMedica)
def ejecutar_comando_crear_imagen_medica(comando: CrearImagenMedica):
    handler = CrearImagenMedicaHandler()
    handler.handle(comando)
    