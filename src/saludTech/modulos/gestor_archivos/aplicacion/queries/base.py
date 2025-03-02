from saludTech.seedwork.aplicacion.queries import QueryHandler
from saludTech.modulos.gestor_archivos.infraestructura.fabricas import (
    FabricaRepositorio,
)
from saludTech.modulos.gestor_archivos.dominio.fabricas import FabricaImagenMedica


class ImagenesMedicasQueryBaseHandler(QueryHandler):
    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_imagen_medica: FabricaImagenMedica = FabricaImagenMedica()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio

    @property
    def fabrica_imagen_medica(self):
        return self._fabrica_imagen_medica
