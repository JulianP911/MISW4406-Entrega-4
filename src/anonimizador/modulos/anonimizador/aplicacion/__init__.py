from pydispatch import dispatcher

from .handlers import HandlerAnonimizadorIntegracion

from anonimizador.modulos.anonimizador.dominio.eventos import (
    ImagenAnonimizada,
)

dispatcher.connect(
    HandlerAnonimizadorIntegracion.handle_anonimizador,
    signal=f"{ImagenAnonimizada.__name__}Integracion",
)
