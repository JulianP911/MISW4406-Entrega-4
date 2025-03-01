from anonimizador.seedwork.aplicacion.handlers import Handler
from anonimizador.modulos.anonimizador.infraestructura.despachadores import Despachador


class HandlerAnonimizadorIntegracion(Handler):

    @staticmethod
    def handle_anonimizador(comando):
        print("===========HANDLER ANONIMIZADOR INTEGRACION===========")
        print(comando)
        print("===========HANDLER ANONIMIZADOR INTEGRACION===========")

        despachador = Despachador()
        despachador.publicar_comando(comando, "comandos-validar-anonimizado")
