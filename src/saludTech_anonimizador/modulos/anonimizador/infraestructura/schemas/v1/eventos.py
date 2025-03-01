from pulsar.schema import Record, String, Long
from saludTech_anonimizador.seedwork.infraestructura.schema.v1.eventos import EventoIntegracion


class ImagenCargadaPayload(Record):
    id = String()
    id_paciente = String()
    url = String()


class EventoImagenCargada(EventoIntegracion):
    data = ImagenCargadaPayload()

