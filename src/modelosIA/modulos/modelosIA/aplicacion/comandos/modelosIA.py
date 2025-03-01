from modelosIA.seedwork.aplicacion.comandos import Comando
from modelosIA.modulos.modelosIA.aplicacion.dto import DataframeDTO
from .base import CrearDataframeBaseHandler
from dataclasses import dataclass, field
from modelosIA.seedwork.aplicacion.comandos import ejecutar_commando as comando

from modelosIA.modulos.modelosIA.dominio.entidades import Dataframe
from modelosIA.seedwork.infraestructura.uow import UnidadTrabajoPuerto
from modelosIA.modulos.modelosIA.aplicacion.mapeadores import MapeadorDataframe
from modelosIA.modulos.modelosIA.infraestructura.repositorios import RepositorioDataframeSQLite

@dataclass
class CrearDataframe(Comando):
    id: str
    url: str
    dataframe: str

class CrearDataframeHandler(CrearDataframeBaseHandler):

    def handle(self, comando: CrearDataframe):
        dataframe_dto = DataframeDTO(
                id=comando.id
            ,   url=comando.url
            ,   dataframe=comando.dataframe)

        dataframe: Dataframe = self.fabrica_dataframe.crear_objeto(dataframe_dto, MapeadorDataframe())
        dataframe.crear_dataframe(dataframe)

        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioDataframeSQLite)

        UnidadTrabajoPuerto.registrar_batch(repositorio.agregar, dataframe)
        UnidadTrabajoPuerto.commit()


@comando.register(CrearDataframe)
def ejecutar_comando_crear_imagen_medica(comando: CrearDataframe):
    handler = CrearDataframeHandler()
    handler.handle(comando)
