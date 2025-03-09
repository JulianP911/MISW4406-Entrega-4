from fastapi import APIRouter
from pydantic import BaseModel
import requests
from dataclasses import dataclass
from uuid import uuid4 as uuid
from bff.despachadores import Despachador
from bff import utils
import asyncio


class MetadataDTO(BaseModel):
    tipo: str
    formato: str


class ImagenMedicaDTO(BaseModel):
    url: str
    metadata: MetadataDTO
    id_paciente: str


router = APIRouter(
    prefix="/imagen_medica",
)


@router.post("/", status_code=202)
async def crear_imagen_medica(imagen_medica: ImagenMedicaDTO):
    payload = dict(
        url=imagen_medica.url,
        metadata=imagen_medica.metadata.__dict__,
        id_paciente=imagen_medica.id_paciente,
    )
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
            "comandos-crear-imagen",
            "public/default/comandos-crear-imagen",
        )
    )

    return {"mensaje": "Creando imagen"}


@router.get("/")
async def dar_imagenes_medicas():
    imagenes_medicas_json = requests.get(
        f"http://localhost:5000/gestor_archivos/imagen_medica"
    ).json()
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
