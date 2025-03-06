from pulsar.schema import *
from .utils import time_millis
import uuid

class ValidarAnonimizacionImagenMedicaPayload(Record):
    id=String()
    url=String()
 
class RevertirValidacionAnonimizacionImagenMedicaPayload(Record):
    id=String()
    url=String()

class ComandoValidarAnonimizacionImagenMedica(Record):
    id = String(default=str(uuid.uuid4()))
    time = Long()
    ingestion = Long(default=time_millis())
    specversion = String(default="v1")
    type = String(default="ComandoValidarAnonimizacionImagenMedica")
    datacontenttype = String()
    service_name = String(default="validador_anonimizador.saludTech")
    data = ValidarAnonimizacionImagenMedicaPayload

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class ComandoRevertirValidacionAnonimizacionImagenMedica(Record):
    id = String(default=str(uuid.uuid4()))
    time = Long()
    ingestion = Long(default=time_millis())
    specversion = String(default="v1")
    type = String(default="ComandoRevertirValidacionAnonimizacionImagenMedica")
    datacontenttype = String()
    service_name = String(default="validador_anonimizador.saludTech")
    data = RevertirValidacionAnonimizacionImagenMedicaPayload

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)