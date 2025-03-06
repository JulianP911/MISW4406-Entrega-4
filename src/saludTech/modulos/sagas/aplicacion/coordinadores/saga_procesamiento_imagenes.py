from saludTech.seedwork.aplicacion.sagas import CoordinadorOrquestacion, Transaccion, Inicio, Fin
from saludTech.seedwork.aplicacion.comandos import Comando
from saludTech.seedwork.dominio.eventos import EventoDominio

from saludTech.modulos.sagas.aplicacion.comandos.anonimizador import AnonimizarImagenMedica, DeshacerAnonimizacionImagenMedica
from saludTech.modulos.sagas.aplicacion.comandos.gestor_archivos import CargarImagenMedica, EliminarImagenMedica
from saludTech.modulos.sagas.aplicacion.comandos.modelosIA import GenerarDataframeImagenMedica, EliminarDataframeImagenMedica
from saludTech.modulos.sagas.aplicacion.comandos.validador_anonimizador import ValidarAnonimizacionImagenMedica,DeshacerValidacionAnonimizacionImagenMedica
from saludTech.modulos.gestor_archivos.aplicacion.comandos.crear_imagen_medica import CrearImagenMedica
from saludTech.modulos.gestor_archivos.dominio.eventos import ArchivoPublicado as ArchivoPublicadoGestorArchivos,ArchivoPublicacionFallida as ArchivoPublicacionFallidaGestorArchivos,ArchivoPublicacionRevertida as ArchivoPublicacionRevertidaGestorArchivos
from saludTech.modulos.sagas.dominio.eventos.anonimizador import ImagenAnonimizada,ImagenAnonimizacionFallida,ImagenAnonimizacionRevertida
from saludTech.modulos.sagas.dominio.eventos.modelosIA import ImagenAnonimizadaValidada,ImagenAnonimizadaValidacionFallida,ImagenAnonimizadaValidacionRevertida
from saludTech.modulos.sagas.dominio.eventos.validador_anonimizador import ArchivoPublicado,ArchivoPublicacionFallida,ArchivoPublicacionRevertida


class CoordinadorProcesamientoImagenes(CoordinadorOrquestacion):
    def inicializar_pasos(self):
        self.pasos = [
            Inicio(index=0),
            Transaccion(index=1, comando=CargarImagenMedica, evento=ArchivoPublicadoGestorArchivos, error=ArchivoPublicacionFallidaGestorArchivos, compensacion=EliminarImagenMedica),
            Transaccion(index=2, comando=AnonimizarImagenMedica, evento=ImagenAnonimizada, error=ImagenAnonimizacionFallida, compensacion=DeshacerAnonimizacionImagenMedica),
            Transaccion(index=3, comando=ValidarAnonimizacionImagenMedica, evento=ImagenAnonimizadaValidada, error=ImagenAnonimizadaValidacionFallida, compensacion=DeshacerValidacionAnonimizacionImagenMedica),
            Transaccion(index=4, comando=GenerarDataframeImagenMedica, evento=ArchivoPublicado, error=ArchivoPublicacionFallida, compensacion=EliminarDataframeImagenMedica),
            Fin(index=5)
        ]

    def iniciar(self):
        self.persistir_en_saga_log(self.pasos[0])
    
    def terminar(self):
        self.persistir_en_saga_log(self.pasos[-1])

    def persistir_en_saga_log(self, mensaje):
        # TODO Persistir estado en DB
        # Probablemente usted podría usar un repositorio para ello
        ...

    def construir_comando(self, evento: EventoDominio, tipo_comando: type):
        # TODO Transforma un evento en la entrada de un comando
        # Por ejemplo si el evento que llega es ReservaCreada y el tipo_comando es PagarReserva
        # Debemos usar los atributos de ReservaCreada para crear el comando PagarReserva
        ...

# TODO Agregue un Listener/Handler para que se puedan redireccionar eventos de dominio
def oir_mensaje(mensaje):
    if isinstance(mensaje, EventoDominio):
        coordinador = CoordinadorProcesamientoImagenes()
        coordinador.procesar_evento(mensaje)
    else:
        raise NotImplementedError("El mensaje no es evento de Dominio")