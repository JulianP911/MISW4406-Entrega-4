from pydispatch import dispatcher

from .handlers import HandlerModeloIAIntegracion

from modelosIA.modulos.dominio.eventos import (
    ImagenAnonimizadaValidada,
)

dispatcher.connect(
    HandlerModeloIAIntegracion.handle_archivo_publicado,
    signal=f"{ImagenAnonimizadaValidada.__name__}Integracion",
)
