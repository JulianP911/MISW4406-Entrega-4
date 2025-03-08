from pulsar import Client
from pulsar.schema import AvroSchema
import logging
import traceback


from saludTech.modulos.gestor_archivos.infraestructura.schemas.v1.eventos import (
    EventoImagenCargada,
)
from saludTech.modulos.gestor_archivos.infraestructura.schemas.v1.comandos import (
    ComandoRevertirCargaImagenMedica,
)
from saludTech.seedwork.infraestructura import utils

from saludTech.modulos.sagas.aplicacion.coordinadores.saga_procesamiento_imagenes import oir_mensaje

def suscribirse_a_eventos():
    cliente = None
    try:
        cliente = Client(f"pulsar://{utils.broker_host()}:6650")
        consumidor = cliente.subscribe(
            "eventos-anonimizar-imagen",
            subscription_name="saludTech-sub-eventos",
            schema=AvroSchema(EventoImagenCargada),
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
            "comandos-anonimizar-imagen",
            subscription_name="saludTech-sub-comandos",
            schema=AvroSchema(EventoImagenCargada),
        )

        while True:
            
            mensaje = consumidor.receive()
            with app.test_request_context():
                print(f"Comando recibido: {type(mensaje.value())}")
                oir_mensaje(mensaje.value())
                consumidor.acknowledge(mensaje)
    except:
        logging.error("ERROR: Suscribiendose al tópico de comandos!")
        traceback.print_exc()
        if cliente:
            cliente.close()

def suscribirse_a_comandos_reversion():
    cliente = None
    try:
        cliente = Client(f"pulsar://{utils.broker_host()}:6650")
        consumidor = cliente.subscribe(
            "comandos-revertir-anonimizacion-imagen",
            subscription_name="saludTech-sub-comandos",
            schema=AvroSchema(ComandoRevertirCargaImagenMedica),
        )

        while True:
            mensaje = consumidor.receive()
            print(f"Comando recibido reversado: {mensaje.value().data}")
            #TODO: Implementar la lógica de negocio para revertir la carga de la imagen
            consumidor.acknowledge(mensaje)
    except:
        logging.error("ERROR: Suscribiendose al tópico de comandos!")
        traceback.print_exc()
        if cliente:
            cliente.close()
