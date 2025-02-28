from anonimizador.seedwork.aplicacion.comandos import ComandoHandler
from anonimizador.modulos.anonimizador.infraestructura.fabricas import FabricaRepositorio
from anonimizador.modulos.anonimizador.dominio.fabricas import FabricaAnonimizarImagen

class CrearReservaBaseHandler(ComandoHandler):
    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_validar_anonimizado: FabricaValidarAnonimizado = FabricaValidarAnonimizado()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio
    
    @property
    def fabrica_validar_anonimizado(self):
        return self._fabrica_validar_anonimizado
    