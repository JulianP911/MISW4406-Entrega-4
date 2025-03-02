from saludTech_anonimizador.seedwork.aplicacion.handlers import Handler
from saludTech_anonimizador.modulos.anonimizador.infraestructura.despachadores import Despachador


class HandlerImagenMedicaIntegracion(Handler):

    @staticmethod
    def handle_archivo_publicado(comando):
        print("===========HANDLER IMAGEN MEDICA INTEGRACION===========")
        print(comando)
        print("===========HANDLER IMAGEN MEDICA INTEGRACION===========")
        despachador = Despachador()
        despachador.publicar_comando(comando, "comandos-ejecutar-modelosIA")
