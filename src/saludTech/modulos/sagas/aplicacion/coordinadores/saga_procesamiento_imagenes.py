import uuid
from anonimizador.modulos.anonimizador.aplicacion.handlers import HandlerAnonimizadorIntegracion


from modelosIA.modulos.modelosIA.infraestructura.schemas.v1.comandos import ComandoGuardarDataframes
from modelosIA.modulos.modelosIA.infraestructura.schemas.v1.eventos import EventoDataframeGuardado
from saludTech.seedwork.aplicacion.sagas import CoordinadorOrquestacion, Transaccion, Inicio, Fin
from saludTech.seedwork.aplicacion.comandos import Comando
from saludTech.seedwork.dominio.eventos import EventoDominio
from saludTech.modulos.gestor_archivos.infraestructura.schemas.v1.eventos import EventoImagenCargada, ImagenCargadaPayload
from anonimizador.modulos.anonimizador.infraestructura.schemas.v1.comandos import ComandoAnonimizarImagen
from saludTech.seedwork.infraestructura import utils
from saludTech.seedwork.infraestructura.schema.v1.comandos import ComandoIntegracion
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
from validador_anonimizador.modulos.validador_anonimizador.aplicacion.handlers import HandlerImagenMedicaIntegracion
from validador_anonimizador.modulos.validador_anonimizador.infraestructura.schemas.v1.comandos import ComandoValidarAnonimizado

class CoordinadorProcesamientoImagenes(CoordinadorOrquestacion):
    def __init__(self):
        super().__init__()
        from saludTech.modulos.sagas.infraestructura.repositorios import SagaLogSQLRepositorio
        self.saga_log_repo = SagaLogSQLRepositorio()
        self.id_correlacion = uuid.uuid4()
        self.inicializar_pasos()
        self.paso_actual = 0  # Track the current step

    def inicializar_pasos(self):
        self.pasos = [
            Inicio(index=0),
            Transaccion(index=1, comando=CargarImagenMedica, evento=EventoImagenCargada, error=ArchivoPublicacionFallidaGestorArchivos, compensacion=EliminarImagenMedica),
            Transaccion(index=2, comando=ComandoAnonimizarImagen, evento=ImagenAnonimizada, error=ImagenAnonimizacionFallida, compensacion=DeshacerAnonimizacionImagenMedica),
            Transaccion(index=3, comando=ValidarAnonimizacionImagenMedica, evento=ImagenAnonimizadaValidada, error=ImagenAnonimizadaValidacionFallida, compensacion=DeshacerValidacionAnonimizacionImagenMedica),
            Fin(index=4)
        ]

    def iniciar(self):
        #self.persistir_en_saga_log(self.pasos[0])
        self.procesar_paso(self.pasos[1])  # Start the first step after initialization

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

    def procesar_paso(self, paso):
        """Process the current step and move to the next one."""
        if isinstance(paso, Transaccion):
            print(f"Procesando paso {paso.index}: {paso.comando.__name__}")
            # Execute the command for the current step
            comando = self.construir_comando(paso.evento, paso.comando)
            if comando:
                self.ejecutar_comando(comando)
            # Move to the next step
            self.paso_actual += 1
            if self.paso_actual < len(self.pasos):
                self.procesar_paso(self.pasos[self.paso_actual])
        elif isinstance(paso, Fin):
            print("Saga completada.")
            self.terminar()

    def construir_comando(self, evento: EventoDominio, tipo_comando: type):
        """Construct the appropriate command based on the event."""
        print(f"Construyendo comando {tipo_comando.__name__} a partir del evento {evento}")
        if hasattr(evento, "data") and isinstance(evento.data, ImagenCargadaPayload):
            return CargarImagenMedica
        elif tipo_comando == ComandoAnonimizarImagen:
            return ComandoAnonimizarImagen
        elif tipo_comando == ValidarAnonimizacionImagenMedica:
            return ValidarAnonimizacionImagenMedica
        else:
            raise ValueError(f"No se puede construir el comando {tipo_comando.__name__} a partir del evento {type(evento).__name__}")

    def ejecutar_comando(self, comando):
        """Execute the command and handle the result."""
        print(f"Ejecutando comando: {comando}")
        # Simulate command execution (replace with actual command execution logic)
        if isinstance(comando, CargarImagenMedica):
            print(f"Cargando imagen médica: {comando}")
            # Dispatch the next event (e.g., EventoImagenCargada)
            dispatcher.send(signal=f"{EventoImagenCargada.__name__}Integracion", evento=EventoImagenCargada(id_imagen=comando.data.id, url=comando.data.url))
        elif isinstance(comando, ComandoAnonimizarImagen):
            print(f"Anonimizando imagen: {comando}")
            # Dispatch the next event (e.g., ImagenAnonimizada)
            dispatcher.send(signal=f"{ImagenAnonimizada.__name__}Integracion", evento=ImagenAnonimizada(id_imagen=comando.id, url=comando.url))
        elif isinstance(comando, ValidarAnonimizacionImagenMedica):
            print(f"Validando anonimización de imagen: {comando}")
            # Dispatch the next event (e.g., ImagenAnonimizadaValidada)
            dispatcher.send(signal=f"{ImagenAnonimizadaValidada.__name__}Integracion", evento=ImagenAnonimizadaValidada(id_imagen=comando.id_imagen))

def oir_mensaje(mensaje):
    """Listen for events and process them."""
    print(f"Mensaje recibido en oir mensaje: {mensaje}")
    print(type(mensaje))
    try:
        coordinador = CoordinadorProcesamientoImagenes()
        if isinstance(mensaje, EventoImagenCargada):
            coordinador.iniciar()  # Start the saga when the first event is received
        coordinador.procesar_evento(mensaje)
    except Exception as e:
        print(f"Error al procesar el mensaje: {e}")
        raise NotImplementedError("El mensaje no es evento de Dominio")