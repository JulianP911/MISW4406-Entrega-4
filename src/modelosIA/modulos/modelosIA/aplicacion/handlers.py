from modelosIA.seedwork.aplicacion.handlers import Handler
from modelosIA.modulos.modelosIA.infraestructura.despachadores import Despachador


class HandlerModeloIAIntegracion(Handler):

    @staticmethod
    def handle_dataframe_generado(comando):
        print("===========HANDLER DATAFRAME INTEGRACION===========")
        print(comando)
        print("===========HANDLER DATAFRAME INTEGRACION===========")

        despachador = Despachador()
        despachador.publicar_comando(comando, "comandos-guardar-dataframe")
