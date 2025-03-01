from pulsar import Client
from pulsar.schema import AvroSchema
import logging
import traceback
import json

from anonimizador.modulos.anonimizador.infraestructura.schemas.v1.comandos import (
    ComandoAnonimizarImagen, ComandoValidarAnonimizado
)
from anonimizador.seedwork.infraestructura import utils
from anonimizador.modulos.anonimizador.dominio.entidades import ImagenMedica
from anonimizador.modulos.anonimizador.aplicacion.servicios import ServicioImagenMedica
from anonimizador.modulos.anonimizador.aplicacion.mapeadores import (
    MapeadorAnonimizadorDTOJson,
)

def suscribirse_a_eventos(app):
    cliente = None
    try:
        cliente = Client(f"pulsar://{utils.broker_host()}:6650")
        consumidor = cliente.subscribe(
            "comandos-validar-anonimizado",
            subscription_name="validar-saludTech-sub-comandos",
            schema=AvroSchema(ComandoValidarAnonimizado),
        )

        
    except Exception as e:
        print(e)
        logging.error("ERROR: Suscribiendose al tópico de comandos!")
        traceback.print_exc()
        if cliente:
            cliente.close()

def suscribirse_a_comandos(app):
    cliente = None
    try:
        cliente = Client(f"pulsar://{utils.broker_host()}:6650")
        consumidor = cliente.subscribe(
            "comandos-anonimizar-imagen",
            subscription_name="anonimizador-saludTech-sub-comandos",
            schema=AvroSchema(ComandoAnonimizarImagen),
        )

        while True:
            mensaje = consumidor.receive()
            print(f"Comando recibido: {mensaje.value().data}")
            with app.test_request_context():
                map_imagen_medica = MapeadorAnonimizadorDTOJson()
                
                imagen_medica_dto = map_imagen_medica.externo_a_dto(mensaje.value().data.__dict__)

                print("===========map_imagen_medica===========")
                print(imagen_medica_dto)
                print("===========map_imagen_medica===========")

                servicio_imagen_medica = ServicioImagenMedica()
                dto_final = servicio_imagen_medica.crear_imagen_medica(imagen_medica_dto)

                print("===========dto_final===========")
                print(dto_final)
                print("===========dto_final===========")

                consumidor.acknowledge(mensaje)
    except Exception as e:
        print(e)
        logging.error("ERROR: Suscribiendose al tópico de comandos!")
        traceback.print_exc()
        if cliente:
            cliente.close()
