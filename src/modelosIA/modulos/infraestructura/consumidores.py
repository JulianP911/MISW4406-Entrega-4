from pulsar import Client
from pulsar.schema import AvroSchema
import logging
import traceback


from modelosIA.modulos.infraestructura.schemas.v1.eventos import (
    EventoDataframeGuardado,
)
from saludTech.seedwork.infraestructura import utils


def suscribirse_a_eventos():
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


def suscribirse_a_comandos():
    cliente = None
    try:
        cliente = Client(f"pulsar://{utils.broker_host()}:6650")
        consumidor = cliente.subscribe(
            "comandos-ejecutar-modelosIA",
            subscription_name="modelosIA-sub-comandos",
            schema=AvroSchema(EventoDataframeGuardado),
        )

        while True:
            mensaje = consumidor.receive()
            print(f"Comando recibido: {mensaje.value().data}")

            consumidor.acknowledge(mensaje)
    except:
        logging.error("ERROR: Suscribiendose al tópico de comandos!")
        traceback.print_exc()
        if cliente:
            cliente.close()
