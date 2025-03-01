from pulsar.schema import *
from dataclasses import dataclass, field
from modelosIA.seedwork.infraestructura.schema.v1.comandos import ComandoIntegracion


class ComandoGuardarDataframesPayload(ComandoIntegracion):
    id = String()
    url = String()
    data = Dict()


class ComandoGuardarDataframes(ComandoIntegracion):
    data = ComandoGuardarDataframesPayload()
