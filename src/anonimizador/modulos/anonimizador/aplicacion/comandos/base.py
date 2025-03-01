from anonimizador.seedwork.aplicacion.comandos import ComandoHandler
from anonimizador.modulos.anonimizador.infraestructura.fabricas import FabricaRepositorio
from anonimizador.modulos.anonimizador.dominio.fabricas import FabricaImagenMedica

class CrearImagenMedicaBaseHandler(ComandoHandler):
    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_imagen_medica: FabricaImagenMedica = FabricaImagenMedica()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio

    @property
    def fabrica_imagen_medica(self):
        return self._fabrica_imagen_medica
