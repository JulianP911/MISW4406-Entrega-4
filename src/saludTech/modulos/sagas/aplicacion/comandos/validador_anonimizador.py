from pulsar.schema import *
from dataclasses import dataclass, field
from anonimizador.seedwork.infraestructura.schema.v1.comandos import ComandoIntegracion

# Define payloads
class ValidarAnonimizacionImagenMedicaPayload(Record):
    id = String()
    url = String()
    token_paciente = String()

# Define commands
class ValidarAnonimizacionImagenMedica(ComandoIntegracion):
    data = ValidarAnonimizacionImagenMedicaPayload()

class DeshacerValidacionAnonimizacionImagenMedica():
    ...