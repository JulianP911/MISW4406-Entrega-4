from pulsar import Client
from pulsar.schema import AvroSchema
import logging
import traceback
from flask import jsonify


from saludTech.modulos.gestor_archivos.infraestructura.schemas.v1.eventos import (
    EventoImagenCargada,
)
from saludTech.modulos.gestor_archivos.infraestructura.schemas.v1.comandos import (
    ComandoRevertirCargaImagenMedica,
    CargarImagenMedica,
)
from saludTech.seedwork.infraestructura import utils

from saludTech.modulos.sagas.aplicacion.coordinadores.saga_procesamiento_imagenes import (
    oir_mensaje,
)

from saludTech.modulos.gestor_archivos.aplicacion.comandos.crear_imagen_medica import (
    CrearImagenMedica,
)

from saludTech.modulos.gestor_archivos.aplicacion.mapeadores import (
    MapeadorImagenMedicaDTOJson,
)
from saludTech.seedwork.aplicacion.comandos import ejecutar_commando


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
            "comandos-crear-imagen",
            subscription_name="saludTech-sub-comandos",
            schema=AvroSchema(CargarImagenMedica),
        )

        while True:

            mensaje = consumidor.receive()
            with app.test_request_context():
                print(f"Comando recibido: {mensaje.value().data}")
                valor = mensaje.value()
                valor_json = vars(valor.data)
                del valor_json["metadata"]
                print("====================data_json====================")
                print(valor_json)
                print("====================data_json====================")

                print("====================metadata====================")
                print(valor.data.metadata)
                print("====================metadata====================")

                valor_json["metadata"] = vars(valor.data.metadata)
                map_imagen_medica = MapeadorImagenMedicaDTOJson()

                imagen_medica_dto = map_imagen_medica.externo_a_dto(valor_json)
                comando = CrearImagenMedica(
                    fecha_creacion=imagen_medica_dto.fecha_creacion,
                    fecha_actualizacion=imagen_medica_dto.fecha_actualizacion,
                    id=imagen_medica_dto.id,
                    url=imagen_medica_dto.url,
                    metadata=imagen_medica_dto.metadata,
                    bucket_location=imagen_medica_dto.bucket_location,
                    id_paciente=valor.data.id_paciente,
                )
                ejecutar_commando(comando)

                oir_mensaje(valor)
                consumidor.acknowledge(mensaje)
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
            "comandos-revertir-anonimizacion-imagen",
            subscription_name="saludTech-sub-comandos",
            schema=AvroSchema(ComandoRevertirCargaImagenMedica),
        )

        while True:
            mensaje = consumidor.receive()
            print(f"Comando recibido reversado: {mensaje.value().data}")
            # TODO: Implementar la lógica de negocio para revertir la carga de la imagen
            consumidor.acknowledge(mensaje)
    except:
        logging.error("ERROR: Suscribiendose al tópico de comandos!")
        traceback.print_exc()
        if cliente:
            cliente.close()
