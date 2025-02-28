from pulsar.schema import *
from dataclasses import dataclass, field
from anonimizador.seedwork.infraestructura.schema.v1.comandos import ComandoIntegracion


class ComandoValidarAnonimizadoPayload(ComandoIntegracion):
    id = String()
    token_paciente = String()
    url = String()


class ComandoValidarAnonimizado(ComandoIntegracion):
    data = ComandoAnonimizarImagenPayload()

class ComandoAnonimizarImagenPayload(ComandoIntegracion):
    id = String()
    id_paciente = String()
    url = String()


class ComandoAnonimizarImagen(ComandoIntegracion):
    data = ComandoAnonimizarImagenPayload()