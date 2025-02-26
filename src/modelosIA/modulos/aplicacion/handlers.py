from modelosIA.seedwork.aplicacion.handlers import Handler
from modelosIA.modulos.infraestructura.despachadores import Despachador


class HandlerModeloIAIntegracion(Handler):

    @staticmethod
    def handle_dataframe_generado(comando):
        despachador = Despachador()
        despachador.publicar_comando(comando, "comandos-guardar-dataframe")
