import pulsar
from pulsar.schema import AvroSchema

from validador_anonimizador.modulos.validador_anonimizador.infraestructura.schemas.v1.comandos import (
    ComandoAnonimizarImagen,
    ComandoAnonimizarImagenPayload,
    ComandoGuardarDataframesPayload,
    ComandoGuardarDataframes,
)
from validador_anonimizador.seedwork.infraestructura import utils

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
        payload = ComandoGuardarDataframesPayload(id=comando.id, url=comando.url)
        comando_integracion = ComandoGuardarDataframes(data=payload)

        self._publicar_mensaje(
            comando_integracion, topico, AvroSchema(ComandoGuardarDataframes)
        )
