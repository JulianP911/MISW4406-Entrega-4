from pulsar.schema import *
from .utils import time_millis
import uuid
#TODO probablemente eliminar archivo 
class AnonimizarImagenMedicaPayload(Record):
    id=String()
    url=String()
    token_paciente=String()
 
class RevertirAnonimizacionImagenMedicaPayload(Record):
    id=String()
    url=String()
    token_paciente=String()

class ComandoAnonimizarImagenMedica(Record):
    id = String(default=str(uuid.uuid4()))
    time = Long()
    ingestion = Long(default=time_millis())
    specversion = String(default="v1")
    type = String(default="ComandoAnonimizarImagenMedica")
    datacontenttype = String()
    service_name = String(default="anonimizador.saludTech")
    data = AnonimizarImagenMedicaPayload

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class ComandoRevertirAnonimizacionImagenMedica(Record):
    id = String(default=str(uuid.uuid4()))
    time = Long()
    ingestion = Long(default=time_millis())
    specversion = String(default="v1")
    type = String(default="ComandoRevertirAnonimizacionImagenMedica")
    datacontenttype = String()
    service_name = String(default="anonimizador.saludTech")
    data = RevertirAnonimizacionImagenMedicaPayload

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)