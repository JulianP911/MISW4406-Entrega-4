import typing
import strawberry
import uuid
import requests
import os

from datetime import datetime


SALUDTECH_HOST = os.getenv("SALUDTECH_ADDRESS", default="localhost")

def obtener_imagenes(root) -> typing.List["ImagenMedica"]:
    imagenes_medicas_json = requests.get(f'http://{SALUDTECH_HOST}:5000/imagen_medica').json()
    imagenesMedicas = []

    for imagenMedica in imagenes_medicas_json:
        imagenesMedicas.append(
            ImagenMedica(
                url=imagenMedica.get('url', ''),
                id_paciente=imagenMedica.get('id_paciente', ''),
            )
        )

    return imagenesMedicas

@strawberry.type
class ImagenMedica:
    url: str
    id_paciente

@strawberry.type
class ImagenMedicaRespuesta:
    mensaje: str
    codigo: int






