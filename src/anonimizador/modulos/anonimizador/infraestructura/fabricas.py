from dataclasses import dataclass, field
from anonimizador.seedwork.dominio.fabricas import Fabrica
from anonimizador.seedwork.dominio.repositorios import Repositorio, EventPayload
from anonimizador.modulos.anonimizador.dominio.repositorios import (
    RepositorioImagenMedica,
)
from .repositorios import RepositorioImageneMedicaSQLite
from .excepciones import ExcepcionFabrica
from .schemas.v1.comandos import ComandoValidarAnonimizadoPayload


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
        if obj == ComandoValidarAnonimizadoPayload.__class__:
            return ComandoValidarAnonimizadoPayload()
        else:
            raise ExcepcionFabrica()
