from pulsar.schema import *
from .utils import time_millis
import uuid

class GenerarDataframePayload(Record):
    id=String()
    url=String()
    valida=Bool()
 
class RevertirGeneracionDataframePayload(Record):
    id=String()
    url=String()
    valida=Bool()

class ComandoGenerarDataframe(Record):
    id = String(default=str(uuid.uuid4()))
    time = Long()
    ingestion = Long(default=time_millis())
    specversion = String(default="v1")
    type = String(default="ComandoGenerarDataframe")
    datacontenttype = String()
    service_name = String(default="modelosIA.saludTech")
    data = GenerarDataframePayload

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class ComandoRevertirGeneracionDataframe(Record):
    id = String(default=str(uuid.uuid4()))
    time = Long()
    ingestion = Long(default=time_millis())
    specversion = String(default="v1")
    type = String(default="ComandoRevertirGeneracionDataframe")
    datacontenttype = String()
    service_name = String(default="modelosIA.saludTech")
    data = RevertirGeneracionDataframePayload

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)