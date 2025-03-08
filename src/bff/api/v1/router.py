from fastapi import APIRouter
import requests
from dataclasses import dataclass
from uuid import uuid4 as uuid
from bff.despachadores import Despachador
from bff import utils
import asyncio

router = APIRouter(
    prefix="/imagen_medica",
)


@router.post("/", status_code=202)
async def crear_imagen_medica():
    payload = dict(id=str(uuid()), id_paciente=str(uuid()), url="url")
    comando = dict(
        id=str(uuid()),
        time=utils.time_millis(),
        specversion="v1",
        type="ComandoCrearImagenMedica",
        ingestion=utils.time_millis(),
        datacontenttype="AVRO",
        service_name="bff",
        data=payload,
    )
    despachador = Despachador()

    asyncio.get_event_loop().create_task(
        despachador.publicador_mensaje(
            comando,
            "comandos-anonimizar-imagen",
            "public/default/eventos-anonimizar-imagen",
        )
    )

    return {"mensaje": "Creando imagen"}


@router.get("/")
async def dar_imagenes_medicas():
    imagenes_medicas_json = requests.get(
        f"http://localhost:5000/gestor_archivos/imagen_medica"
    ).json()
    print(imagenes_medicas_json)
    imagenes_medicas = []

    for imagen in imagenes_medicas_json:
        imagenes_medicas.append(
            ImagenMedica(
                id=imagen["id"],
                url=imagen["url"],
                fecha_creacion=imagen["fecha_creacion"],
                fecha_actualizacion=imagen["fecha_actualizacion"],
                bucket_location=imagen["bucket_location"],
            )
        )

    return imagenes_medicas


@dataclass
class ImagenMedica:
    id: str
    url: str
    fecha_creacion: str
    fecha_actualizacion: str
    bucket_location: str
