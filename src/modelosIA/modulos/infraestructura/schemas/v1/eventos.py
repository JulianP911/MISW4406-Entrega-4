from pulsar.schema import Record, String, Long
from saludTech.seedwork.infraestructura.schema.v1.eventos import EventoIntegracion


class DataframeGuardadoPayload(Record):
    id = String()
    id_paciente = String()
    data = Dict()


class EventoDataframeGuardado(EventoIntegracion):
    data = DataframeGuardadoPayload()
