from dataclasses import dataclass, field
from validador_anonimizador.seedwork.dominio.fabricas import Fabrica
from validador_anonimizador.seedwork.dominio.repositorios import Repositorio, EventPayload
from validador_anonimizador.modulos.validador_anonimizador.dominio.repositorios import (
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
