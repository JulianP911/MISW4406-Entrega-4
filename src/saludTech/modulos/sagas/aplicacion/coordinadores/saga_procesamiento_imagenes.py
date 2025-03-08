import uuid
from anonimizador.modulos.anonimizador.aplicacion.handlers import HandlerAnonimizadorIntegracion
from saludTech.modulos.sagas.infraestructura.repositorios import SagaLogSQLRepositorio
from saludTech.seedwork.aplicacion.sagas import CoordinadorOrquestacion, Transaccion, Inicio, Fin
from saludTech.seedwork.aplicacion.comandos import Comando
from saludTech.seedwork.dominio.eventos import EventoDominio
from saludTech.modulos.gestor_archivos.infraestructura.schemas.v1.eventos import EventoImagenCargada
from anonimizador.modulos.anonimizador.infraestructura.schemas.v1.comandos import ComandoAnonimizarImagen
from saludTech.seedwork.infraestructura import utils
from saludTech.seedwork.infraestructura.schema.v1.eventos import EventoIntegracion
from saludTech.modulos.sagas.aplicacion.comandos.anonimizador import AnonimizarImagenMedica, DeshacerAnonimizacionImagenMedica
from saludTech.modulos.sagas.aplicacion.comandos.gestor_archivos import CargarImagenMedica, EliminarImagenMedica
from saludTech.modulos.gestor_archivos.dominio.comandos import ComandoCargarImagenMedica
from saludTech.modulos.sagas.aplicacion.comandos.modelosIA import GenerarDataframeImagenMedica, EliminarDataframeImagenMedica
from saludTech.modulos.sagas.aplicacion.comandos.validador_anonimizador import ValidarAnonimizacionImagenMedica,DeshacerValidacionAnonimizacionImagenMedica
from saludTech.modulos.gestor_archivos.aplicacion.comandos.crear_imagen_medica import CrearImagenMedica
from saludTech.modulos.gestor_archivos.dominio.eventos import ArchivoPublicado as ArchivoPublicadoGestorArchivos,ArchivoPublicacionFallida as ArchivoPublicacionFallidaGestorArchivos,ArchivoPublicacionRevertida as ArchivoPublicacionRevertidaGestorArchivos
from saludTech.modulos.sagas.dominio.eventos.anonimizador import ImagenAnonimizada,ImagenAnonimizacionFallida,ImagenAnonimizacionRevertida
from saludTech.modulos.sagas.dominio.eventos.modelosIA import ImagenAnonimizadaValidada,ImagenAnonimizadaValidacionFallida,ImagenAnonimizadaValidacionRevertida
from saludTech.modulos.sagas.dominio.eventos.validador_anonimizador import ArchivoPublicado,ArchivoPublicacionFallida,ArchivoPublicacionRevertida
from pulsar.schema import Record,AvroSchema
from pydispatch import dispatcher
import pulsar

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
            # Transaccion(index=2, comando=ComandoAnonimizarImagen, evento=ImagenAnonimizada, error=ImagenAnonimizacionFallida, compensacion=DeshacerAnonimizacionImagenMedica),
            # Transaccion(index=3, comando=ValidarAnonimizacionImagenMedica, evento=ImagenAnonimizadaValidada, error=ImagenAnonimizadaValidacionFallida, compensacion=DeshacerValidacionAnonimizacionImagenMedica),
            # Transaccion(index=4, comando=GenerarDataframeImagenMedica, evento=ArchivoPublicado, error=ArchivoPublicacionFallida, compensacion=EliminarDataframeImagenMedica),
            Fin(index=2)
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
        # Buscar el paso en la lista que tenga el evento recibido
        paso = next((p for p in self.pasos if isinstance(p, Transaccion) and p.evento == type(evento)), None)

        if not paso:
            raise ValueError(f"No se encontró un comando asociado al evento {type(evento).__name__}")

        
        tipo_comando = paso.comando  # Obtener la clase del comando

        # Mapeo de eventos a comandos con atributos específicos
        if isinstance(evento, EventoImagenCargada) and tipo_comando == CargarImagenMedica:
            comando= ComandoAnonimizarImagen(
            id=evento.data.id,
            url=evento.data.url,
            id_paciente=evento.data.id_paciente,
        )
            dispatcher.connect(
                HandlerAnonimizadorIntegracion.handle_anonimizador,
                signal=f"{ImagenAnonimizada.__name__}Integracion",
            )
            return
        elif isinstance(evento, ImagenAnonimizada) and tipo_comando == ValidarAnonimizacionImagenMedica:
            return ValidarAnonimizacionImagenMedica(id_imagen=evento.id_imagen)
        elif isinstance(evento, ImagenAnonimizadaValidada) and tipo_comando == GenerarDataframeImagenMedica:
            return GenerarDataframeImagenMedica(id_imagen=evento.id_imagen)
        elif isinstance(evento, ArchivoPublicadoGestorArchivos) and tipo_comando == AnonimizarImagenMedica:
            return AnonimizarImagenMedica(id_imagen=evento.id_imagen)

        raise ValueError(f"No se puede construir el comando {tipo_comando.__name__} a partir del evento {type(evento).__name__}")
        # TODO Transforma un evento en la entrada de un comando
        # Por ejemplo si el evento que llega es ReservaCreada y el tipo_comando es PagarReserva
        # Debemos usar los atributos de ReservaCreada para crear el comando PagarReserva
        # if tipo_comando == CargarImagenMedica and isinstance(evento, EventoImagenCargada):
        #     return CargarImagenMedica(id_imagen=evento.id_imagen, ruta=evento.ruta)
        # elif tipo_comando == AnonimizarImagenMedica and isinstance(evento, ArchivoPublicadoGestorArchivos):
        #     return AnonimizarImagenMedica(id_imagen=evento.id_imagen)
        # elif tipo_comando == ValidarAnonimizacionImagenMedica and isinstance(evento, ImagenAnonimizada):
        #     return ValidarAnonimizacionImagenMedica(id_imagen=evento.id_imagen)
        # elif tipo_comando == GenerarDataframeImagenMedica and isinstance(evento, ImagenAnonimizadaValidada):
        #     return GenerarDataframeImagenMedica(id_imagen=evento.id_imagen)
        # else:
        #     raise ValueError(f"No se puede construir el comando {tipo_comando} a partir del evento {evento}")

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