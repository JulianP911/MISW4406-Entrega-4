from .entidades import Dataframe
from .excepciones import NoEsPosibleAnonimizarExcepcion
from modelosIA.seedwork.dominio.repositorios import Mapeador, Repositorio
from modelosIA.seedwork.dominio.fabricas import Fabrica
from modelosIA.seedwork.dominio.entidades import Entidad
from dataclasses import dataclass


@dataclass
class _FabricaDateframe(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if isinstance(obj, Entidad):
            return mapeador.entidad_a_dto(obj)
        else:
            dataframe: Dataframe = mapeador.dto_a_entidad(obj)

            return dataframe


@dataclass
class FabricaDateframe(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if mapeador.obtener_tipo() == Dataframe.__class__:
            fabrica_dataframe = _FabricaDateframe()
            return fabrica_dataframe.crear_objeto(obj, mapeador)
        else:
            raise NoEsPosibleAnonimizarExcepcion()

    def __call__(self, obj: any, mapeador: Mapeador) -> any:
        return self.crear_objeto(obj, mapeador)
