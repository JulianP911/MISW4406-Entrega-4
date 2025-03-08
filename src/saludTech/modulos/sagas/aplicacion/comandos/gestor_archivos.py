from pulsar.schema import Record, String
from saludTech.seedwork.infraestructura.schema.v1.comandos import ComandoIntegracion

# Define payloads
class CargarImagenMedicaPayload(Record):
    id = String()
    url = String()
    id_paciente = String()

# Define commands
class CargarImagenMedica(ComandoIntegracion):
    data = CargarImagenMedicaPayload()

    def __str__(self):
        return f"CargarImagenMedica(id={self.data.id}, url={self.data.url})"
    
class EliminarImagenMedica(ComandoIntegracion):
    ...