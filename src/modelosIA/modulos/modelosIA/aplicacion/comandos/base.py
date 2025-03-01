from modelosIA.seedwork.aplicacion.comandos import ComandoHandler
from modelosIA.modulos.modelosIA.infraestructura.fabricas import FabricaRepositorio
from modelosIA.modulos.modelosIA.dominio.fabricas import FabricaDataframe

class CrearDataframeBaseHandler(ComandoHandler):
    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_dataframe: FabricaDataframe = FabricaDataframe()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio

    @property
    def fabrica_dataframe(self):
        return self._fabrica_dataframe
