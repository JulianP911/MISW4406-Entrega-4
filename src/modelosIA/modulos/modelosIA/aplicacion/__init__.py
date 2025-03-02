from pydispatch import dispatcher

from .handlers import HandlerModeloIAIntegracion

from modelosIA.modulos.modelosIA.dominio.eventos import (
    ImagenAnonimizadaValidada,
)

# dispatcher.connect(
#     HandlerModeloIAIntegracion.handle_dataframe_generado,
#     signal=f"{ImagenAnonimizadaValidada.__name__}Integracion",
# )
