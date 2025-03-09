from pulsar.schema import Record, String
from saludTech.seedwork.infraestructura.schema.v1.comandos import ComandoIntegracion


class MetadataPayload(Record):
    tipo = String()
    formato = String()


# Define payloads
class CargarImagenMedicaPayload(Record):
    url = String()
    metadata = MetadataPayload()
    id_paciente = String()


# Define commands
class CargarImagenMedica(ComandoIntegracion):
    data = CargarImagenMedicaPayload()

    def __str__(self):
        return f"CargarImagenMedica(id={self.data.id}, url={self.data.url})"


class EliminarImagenMedica(ComandoIntegracion): ...
