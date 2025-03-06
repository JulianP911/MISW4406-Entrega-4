from pulsar.schema import *
from .utils import time_millis
import uuid

class CargarImagenMedicaPayload(Record):
    id=String()
    url=String()
    id_paciente=String()
 
class RevertirCargaImagenMedicaPayload(Record):
    id=String()
    url=String()
    id_paciente=String()

class ComandoCargarImagenMedica(Record):
    id = String(default=str(uuid.uuid4()))
    time = Long()
    ingestion = Long(default=time_millis())
    specversion = String(default="v1")
    type = String(default="ComandoCargarImagenMedica")
    datacontenttype = String()
    service_name = String(default="gestor_archivos.saludTech")
    data = CargarImagenMedicaPayload

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class ComandoRevertirCargaImagenMedica(Record):
    id = String(default=str(uuid.uuid4()))
    time = Long()
    ingestion = Long(default=time_millis())
    specversion = String(default="v1")
    type = String(default="ComandoRevertirCargaImagenMedica")
    datacontenttype = String()
    service_name = String(default="gestor_archivos.saludTech")
    data = RevertirCargaImagenMedicaPayload

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)