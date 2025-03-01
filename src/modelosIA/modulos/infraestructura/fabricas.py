from dataclasses import dataclass, field
from modelosIA.seedwork.dominio.fabricas import Fabrica
from modelosIA.seedwork.dominio.repositorios import Repositorio, EventPayload
from .excepciones import ExcepcionFabrica
from .schemas.v1.comandos import ComandoGuardarDataframesPayload


@dataclass
class FabricaEventosPayload(Fabrica):
    def crear_objeto(self, obj, mapeador=None) -> EventPayload:
        if obj == ComandoGuardarDataframesPayload.__class__:
            return ComandoGuardarDataframesPayload()
        else:
            raise ExcepcionFabrica()
