from pulsar.schema import *
from dataclasses import dataclass, field
from saludTech_anonimizador.seedwork.infraestructura.schema.v1.comandos import ComandoIntegracion


class ComandoAnonimizarImagenPayload(ComandoIntegracion):
    id = String()
    id_paciente = String()
    url = String()


class ComandoAnonimizarImagen(ComandoIntegracion):
    data = ComandoAnonimizarImagenPayload()
