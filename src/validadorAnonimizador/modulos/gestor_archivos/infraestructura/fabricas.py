from dataclasses import dataclass, field
from validadorAnonimizador.seedwork.dominio.fabricas import Fabrica
from validadorAnonimizador.seedwork.dominio.repositorios import Repositorio, EventPayload
from validadorAnonimizador.modulos.gestor_archivos.dominio.repositorios import (
    RepositorioImagenMedica,
)
from .repositorios import RepositorioImageneMedicaSQLite
from .excepciones import ExcepcionFabrica
from .schemas.v1.comandos import ComandoAnonimizarImagenPayload


@dataclass
class FabricaRepositorio(Fabrica):
    def crear_objeto(self, obj: type, mapeador: any = None) -> Repositorio:
        if obj == RepositorioImagenMedica.__class__:
            return RepositorioImageneMedicaSQLite()
        else:
            raise ExcepcionFabrica()


@dataclass
class FabricaEventosPayload(Fabrica):
    def crear_objeto(self, obj, mapeador=None) -> EventPayload:
        if obj == ComandoAnonimizarImagenPayload.__class__:
            return ComandoAnonimizarImagenPayload()
        else:
            raise ExcepcionFabrica()
