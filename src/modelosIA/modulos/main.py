import pulsar, _pulsar
from pulsar.schema import *
import uuid
import time
import os


def time_millis():
    return int(time.time() * 1000)


class EventoIntegracion(Record):
    id = String(default=str(uuid.uuid4()))
    time = Long()
    ingestion = Long(default=time_millis())
    specversion = String()
    type = String()
    datacontenttype = String()
    service_name = String()


class ComandoAnonimizarImagenPayload(Record):
    id = String()
    id_paciente = String()
    url = String()


class ComandoAnonimizarImagen(EventoIntegracion):
    data = ComandoAnonimizarImagenPayload()


HOSTNAME = os.getenv("PULSAR_ADDRESS", default="localhost")

client = pulsar.Client(f"pulsar://{HOSTNAME}:6650")
consumer = client.subscribe(
    "comandos-ejecutar-modelosIA",
    consumer_type=_pulsar.ConsumerType.Shared,
    subscription_name="modelosIA-sub-eventos-ejecutar-modelosIA",
    schema=AvroSchema(Comando),
)

while True:
    msg = consumer.receive()
    consumer.acknowledge(msg)

client.close()
