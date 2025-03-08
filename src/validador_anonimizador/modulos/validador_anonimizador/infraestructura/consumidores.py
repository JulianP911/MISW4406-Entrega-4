from pulsar import Client
from pulsar.schema import AvroSchema
import logging
import traceback

from validador_anonimizador.modulos.validador_anonimizador.aplicacion.servicios import (
    ServicioImagenMedica,
)
from validador_anonimizador.modulos.validador_anonimizador.aplicacion.mapeadores import (
    MapeadorImagenMedicaDTOJson,
)

from validador_anonimizador.modulos.validador_anonimizador.infraestructura.schemas.v1.comandos import (
    ComandoValidarAnonimizado,ComandoRevertirValidacionAnonimizacionImagenMedica
)

from validador_anonimizador.seedwork.infraestructura import utils


def suscribirse_a_eventos(app):
    cliente = None
    try:
        cliente = Client(f"pulsar://{utils.broker_host()}:6650")
        consumidor = cliente.subscribe(
            "eventos-validar-anonimizado",
            subscription_name="validador_anonimizador-sub-eventos-validar",
            schema=AvroSchema(ComandoValidarAnonimizado),
        )

        while True:
            mensaje = consumidor.receive()
            print(f"Evento recibido: {mensaje.value().data}")

            consumidor.acknowledge(mensaje)
    except:
        logging.error("ERROR: Suscribiendose al tópico de eventos!")
        traceback.print_exc()
        if cliente:
            cliente.close()


def suscribirse_a_comandos(app):
    cliente = None
    try:
        cliente = Client(f"pulsar://{utils.broker_host()}:6650")
        consumidor = cliente.subscribe(
            "comandos-validar-anonimizado",
            subscription_name="saludTech_comandos-validar-anonimizado",
            schema=AvroSchema(ComandoValidarAnonimizado),
        )

        while True:
            mensaje = consumidor.receive()
            print(f"Comando recibido: {mensaje.value().data}")
            consumidor.acknowledge(mensaje)
            with app.test_request_context():
                imagen_medica_dict = mensaje.value().data.__dict__

                map_imagen_medica = MapeadorImagenMedicaDTOJson()

                imagen_medica_dto = map_imagen_medica.externo_a_dto(imagen_medica_dict)

                servicio_imagen_medica = ServicioImagenMedica()
                dto_final = servicio_imagen_medica.crear_imagen_medica(
                    imagen_medica_dto
                )

    except:
        logging.error("ERROR: Suscribiendose al tópico de comandos!")
        traceback.print_exc()
        if cliente:
            cliente.close()

def suscribirse_a_comandos_reversion(app):
    cliente = None
    try:
        cliente = Client(f"pulsar://{utils.broker_host()}:6650")
        consumidor = cliente.subscribe(
            "comandos-revertir-validacion-anonimizado",
            subscription_name="saludTech_comandos-validar-anonimizado",
            schema=AvroSchema(ComandoRevertirValidacionAnonimizacionImagenMedica),
        )

        while True:
            mensaje = consumidor.receive()
            print(f"Comando recibido: {mensaje.value().data}")
            consumidor.acknowledge(mensaje)
            #TODO: Implementar la lógica de revertir la validación de la imagen médica

    except:
        logging.error("ERROR: Suscribiendose al tópico de comandos!")
        traceback.print_exc()
        if cliente:
            cliente.close()