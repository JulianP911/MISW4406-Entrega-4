import pulsar
from pulsar.schema import AvroSchema

from anonimizador.modulos.anonimizador.infraestructura.schemas.v1.comandos import (
    ComandoValidarAnonimizado,
    ComandoValidarAnonimizadoPayload,
)
from anonimizador.seedwork.infraestructura import utils

import datetime

epoch = datetime.datetime.utcfromtimestamp(0)


def unix_time_millis(dt):
    return (dt - epoch).total_seconds() * 1000.0


class Despachador:
    def _publicar_mensaje(self, mensaje, topico, schema):

        cliente = pulsar.Client(f"pulsar://{utils.broker_host()}:6650")
        publicador = cliente.create_producer(topico, schema=schema)
        publicador.send(mensaje)
        cliente.close()

    def publicar_comando(self, comando, topico):

        payload = ComandoValidarAnonimizadoPayload(
            id=comando.id, url=comando.url, token_paciente=comando.id
        )
        print(payload)
        print("payload---------------------------------------------")
        comando_integracion = ComandoValidarAnonimizado(data=payload)

        self._publicar_mensaje(
            comando_integracion, topico, AvroSchema(ComandoValidarAnonimizado)
        )
