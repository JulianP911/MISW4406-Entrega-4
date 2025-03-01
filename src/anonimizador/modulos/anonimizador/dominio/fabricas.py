from .entidades import ImagenMedica
from .excepciones import NoEsPosibleAnonimizarExcepcion
from anonimizador.seedwork.dominio.repositorios import Mapeador, Repositorio
from anonimizador.seedwork.dominio.fabricas import Fabrica
from anonimizador.seedwork.dominio.entidades import Entidad
from dataclasses import dataclass


@dataclass
class _FabricaImagenMedica(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if isinstance(obj, Entidad):
            return mapeador.entidad_a_dto(obj)
        else:
            imagen_medica: ImagenMedica = mapeador.dto_a_entidad(obj)

            return imagen_medica


@dataclass
class FabricaImagenMedica(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if mapeador.obtener_tipo() == ImagenMedica.__class__:
            fabrica_imagen_medica = _FabricaImagenMedica()
            return fabrica_imagen_medica.crear_objeto(obj, mapeador)
        else:
            raise NoEsPosibleAnonimizarExcepcion()

    def __call__(self, obj: any, mapeador: Mapeador) -> any:
        return self.crear_objeto(obj, mapeador)
