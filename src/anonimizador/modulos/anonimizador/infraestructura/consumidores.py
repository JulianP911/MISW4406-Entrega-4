from pulsar import Client
from pulsar.schema import AvroSchema
import logging
import traceback


from anonimizador.modulos.anonimizador.infraestructura.schemas.v1.comandos import (
    ComandoAnonimizarImagen, ComandoValidarAnonimizado
)
from anonimizador.seedwork.infraestructura import utils

def suscribirse_a_comandos():
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
            print(f"Comando recibido: {mensaje.value().data}")

            consumidor.acknowledge(mensaje)
    except:
        logging.error("ERROR: Suscribiendose al tópico de comandos!")
        traceback.print_exc()
        if cliente:
            cliente.close()
