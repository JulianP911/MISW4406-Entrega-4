from pulsar import Client
from pulsar.schema import AvroSchema
import logging
import traceback

from saludTech.modulos.gestor_archivos.aplicacion.servicios import( ServicioImagenMedica)
from saludTech.modulos.gestor_archivos.aplicacion.mapeadores import (
    MapeadorImagenMedicaDTOJson,
)
from saludTech.modulos.gestor_archivos.infraestructura.schemas.v1.eventos import (
    EventoImagenCargada,
)
from saludTech.seedwork.infraestructura import utils


def suscribirse_a_eventos():
    cliente = None
    try:
        cliente = Client(f"pulsar://{utils.broker_host()}:6650")
        consumidor = cliente.subscribe(
            "eventos-anonimizar-imagen",
            subscription_name="saludTech-sub-eventos",
            schema=AvroSchema(EventoImagenCargada),
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
            "comando-cargar-imagen-medica",
            subscription_name="saludTech-comando-cargar-imagen-medica",
            schema=AvroSchema(EventoImagenCargada),
        )

        while True:
            mensaje = consumidor.receive()
            print(f"Comando recibido: {mensaje.value().data}")
            map_imagen_medica = MapeadorImagenMedicaDTOJson
            imagen_medica_dto = map_imagen_medica.externo_a_dto(
                mensaje.value().data.__dict__
            )
            servicio_imagen_medica = ServicioImagenMedica()
            dto_final = servicio_imagen_medica.crear_imagen_medica(imagen_medica_dto)

            consumidor.acknowledge(mensaje)
    except:
        logging.error("ERROR: Suscribiendose al tópico de comandos!")
        traceback.print_exc()
        if cliente:
            cliente.close()
