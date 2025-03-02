from pulsar import Client
from pulsar.schema import AvroSchema
import logging
import traceback


from modelosIA.modulos.modelosIA.infraestructura.schemas.v1.eventos import (
    EventoDataframeGuardado,
)
from modelosIA.modulos.modelosIA.infraestructura.schemas.v1.comandos import (
    ComandoGuardarDataframes,
)
from modelosIA.modulos.modelosIA.aplicacion.mapeadores import (
    MapeadorDataframeDTOJson,
)
from modelosIA.modulos.modelosIA.aplicacion.servicios import ServicioImagenMedica

from modelosIA.seedwork.infraestructura import utils


def suscribirse_a_eventos(app):
    cliente = None
    try:
        cliente = Client(f"pulsar://{utils.broker_host()}:6650")
        consumidor = cliente.subscribe(
            "eventos-ejecutar-modelosIA",
            subscription_name="modelosIA-sub-eventos",
            schema=AvroSchema(EventoDataframeGuardado),
        )

        while True:
            mensaje = consumidor.receive()
            print(f"Evento recibido: {mensaje.value().data}")

            consumidor.acknowledge(mensaje)
    except:
        logging.error("ERROR: Suscribiendose al tópico de eventos!")
        traceback.print_exc()
        if cliente:
            cliente.close()


def suscribirse_a_comandos(app):
    cliente = None
    try:
        cliente = Client(f"pulsar://{utils.broker_host()}:6650")
        consumidor = cliente.subscribe(
            "comandos-ejecutar-modelosIA",
            subscription_name="modelosIA-sub-comandos",
            schema=AvroSchema(ComandoGuardarDataframes),
        )

        while True:
            mensaje = consumidor.receive()
            consumidor.acknowledge(mensaje)
            with app.test_request_context():
                imagen_medica_dict = mensaje.value().data.__dict__

                map_imagen_medica = MapeadorDataframeDTOJson()
                imagen_medica_dto = map_imagen_medica.externo_a_dto(imagen_medica_dict)

                servicio_imagen_medica = ServicioImagenMedica()
                servicio_imagen_medica.crear_imagen_medica(imagen_medica_dto)

    except:
        logging.error("ERROR: Suscribiendose al tópico de comandos!")
        traceback.print_exc()
        if cliente:
            cliente.close()
