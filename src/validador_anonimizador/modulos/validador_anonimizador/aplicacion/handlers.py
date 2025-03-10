from validador_anonimizador.seedwork.aplicacion.handlers import Handler
from validador_anonimizador.modulos.validador_anonimizador.infraestructura.despachadores import (
    Despachador,
)


class HandlerImagenMedicaIntegracion(Handler):

    @staticmethod
    def handle_archivo_publicado(comando):
        despachador = Despachador()
        despachador.publicar_comando(comando, "comandos-ejecutar-modelosIA")
