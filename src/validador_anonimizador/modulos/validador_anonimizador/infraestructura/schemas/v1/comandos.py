from pulsar.schema import *
from dataclasses import dataclass, field
from validador_anonimizador.seedwork.infraestructura.schema.v1.comandos import ComandoIntegracion


class ComandoAnonimizarImagenPayload(ComandoIntegracion):
    id = String()
    id_paciente = String()
    url = String()


class ComandoAnonimizarImagen(ComandoIntegracion):
    data = ComandoAnonimizarImagenPayload()

class ComandoValidarAnonimizadoPayload(ComandoIntegracion):
    id = String()
    token_paciente = String()
    url = String()


class ComandoValidarAnonimizado(ComandoIntegracion):
    data = ComandoValidarAnonimizadoPayload()



class ComandoGuardarDataframesPayload(ComandoIntegracion):
    id = String()
    url = String()


class ComandoGuardarDataframes(ComandoIntegracion):
    data = ComandoGuardarDataframesPayload()


class RevertirValidacionAnonimizacionImagenMedicaPayload(ComandoIntegracion):
    id = String()
    url = String()


class ComandoRevertirValidacionAnonimizacionImagenMedica(ComandoIntegracion):
    data = RevertirValidacionAnonimizacionImagenMedicaPayload()