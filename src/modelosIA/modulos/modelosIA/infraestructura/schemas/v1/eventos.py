from pulsar.schema import Record, String, Long
from modelosIA.seedwork.infraestructura.schema.v1.eventos import EventoIntegracion


class DataframeGuardadoPayload(Record):
    id = String()
    id_paciente = String()


class EventoDataframeGuardado(EventoIntegracion):
    data = DataframeGuardadoPayload()
