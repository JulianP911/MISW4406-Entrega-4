from pulsar.schema import *
from dataclasses import dataclass, field
from saludTech.seedwork.infraestructura.schema.v1.comandos import ComandoIntegracion


class MetadataPayload(Record):
    tipo = String()
    formato = String()


class CargarImagenMedicaPayload(ComandoIntegracion):
    url = String()
    metadata = MetadataPayload()
    id_paciente = String()


class CargarImagenMedica(ComandoIntegracion):
    data = CargarImagenMedicaPayload()


class ComandoAnonimizarImagenPayload(ComandoIntegracion):
    id = String()
    id_paciente = String()
    url = String()


class ComandoAnonimizarImagen(ComandoIntegracion):
    data = ComandoAnonimizarImagenPayload()


class RevertirCargaImagenMedicaPayload(ComandoIntegracion):
    id = String()
    id_paciente = String()
    url = String()


class ComandoRevertirCargaImagenMedica(ComandoIntegracion):
    data = RevertirCargaImagenMedicaPayload()
