from anonimizador.seedwork.dominio.excepciones import ExcepcionFabrica

class NoEsPosibleAnonimizarExcepcion(ExcepcionFabrica):
    def __init__(self, mensaje='La imagen no cumple con lo esperado para ser anonimizada'):
        self.__mensaje = mensaje
    def __str__(self):
        return str(self.__mensaje)