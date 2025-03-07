import uuid
from saludTech.modulos.sagas.infraestructura.repositorios import SagaLogSQLRepositorio
from saludTech.seedwork.aplicacion.sagas import CoordinadorOrquestacion, Transaccion, Inicio, Fin
from saludTech.seedwork.aplicacion.comandos import Comando
from saludTech.seedwork.dominio.eventos import EventoDominio
from saludTech.modulos.gestor_archivos.infraestructura.schemas.v1.eventos import EventoImagenCargada
from saludTech.seedwork.infraestructura.schema.v1.eventos import EventoIntegracion
from saludTech.modulos.sagas.aplicacion.comandos.anonimizador import AnonimizarImagenMedica, DeshacerAnonimizacionImagenMedica
from saludTech.modulos.sagas.aplicacion.comandos.gestor_archivos import CargarImagenMedica, EliminarImagenMedica
from saludTech.modulos.sagas.aplicacion.comandos.modelosIA import GenerarDataframeImagenMedica, EliminarDataframeImagenMedica
from saludTech.modulos.sagas.aplicacion.comandos.validador_anonimizador import ValidarAnonimizacionImagenMedica,DeshacerValidacionAnonimizacionImagenMedica
from saludTech.modulos.gestor_archivos.aplicacion.comandos.crear_imagen_medica import CrearImagenMedica
from saludTech.modulos.gestor_archivos.dominio.eventos import ArchivoPublicado as ArchivoPublicadoGestorArchivos,ArchivoPublicacionFallida as ArchivoPublicacionFallidaGestorArchivos,ArchivoPublicacionRevertida as ArchivoPublicacionRevertidaGestorArchivos
from saludTech.modulos.sagas.dominio.eventos.anonimizador import ImagenAnonimizada,ImagenAnonimizacionFallida,ImagenAnonimizacionRevertida
from saludTech.modulos.sagas.dominio.eventos.modelosIA import ImagenAnonimizadaValidada,ImagenAnonimizadaValidacionFallida,ImagenAnonimizadaValidacionRevertida
from saludTech.modulos.sagas.dominio.eventos.validador_anonimizador import ArchivoPublicado,ArchivoPublicacionFallida,ArchivoPublicacionRevertida
from pulsar.schema import Record

class CoordinadorProcesamientoImagenes(CoordinadorOrquestacion):
    def __init__(self):
        super().__init__()
        self.saga_log_repo = SagaLogSQLRepositorio()
        self.id_correlacion = uuid.uuid4()
        self.inicializar_pasos()

    def inicializar_pasos(self):
        self.pasos = [
            Inicio(index=0),
            Transaccion(index=1, comando=CargarImagenMedica, evento=EventoImagenCargada, error=ArchivoPublicacionFallidaGestorArchivos, compensacion=EliminarImagenMedica),
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
        print(f"Guardando estado de paso {mensaje.index}")
        print(f"mensaje--------{mensaje}")
        self.saga_log_repo.guardar_estado(
            id_saga=self.id_correlacion,
            paso=mensaje.index,
            estado="Completado" if isinstance(mensaje, Fin) else "En Progreso"
        )

    def construir_comando(self, evento: EventoDominio, tipo_comando: type):
        if tipo_comando == CargarImagenMedica and isinstance(evento, ArchivoPublicadoGestorArchivos):
            return CargarImagenMedica(id_imagen=evento.id_imagen, ruta=evento.ruta)
        elif tipo_comando == AnonimizarImagenMedica and isinstance(evento, ArchivoPublicadoGestorArchivos):
            return AnonimizarImagenMedica(id_imagen=evento.id_imagen)
        elif tipo_comando == ValidarAnonimizacionImagenMedica and isinstance(evento, ImagenAnonimizada):
            return ValidarAnonimizacionImagenMedica(id_imagen=evento.id_imagen)
        elif tipo_comando == GenerarDataframeImagenMedica and isinstance(evento, ImagenAnonimizadaValidada):
            return GenerarDataframeImagenMedica(id_imagen=evento.id_imagen)
        else:
            raise ValueError(f"No se puede construir el comando {tipo_comando} a partir del evento {evento}")

def oir_mensaje(mensaje):
    print(f"Mensaje recibido en oir mensaje: {mensaje}")
    print(type(mensaje))
    print(isinstance(mensaje, Record))
    if isinstance(mensaje, EventoIntegracion):
        print(f"Evento recibido en oir mensaje: {mensaje}")
        coordinador = CoordinadorProcesamientoImagenes()
        coordinador.procesar_evento(mensaje)
    else:
        raise NotImplementedError("El mensaje no es evento de Dominio")