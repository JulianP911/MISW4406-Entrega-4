import strawberry
import typing

from strawberry.types import Info
from bff_web import utils
from bff_web.despachadores import Despachador

from .esquemas import *

@strawberry.type
class Mutation:

    @strawberry.mutation
    async def cargar_imagen_medica(self, id_paciente: str, url: str, info: Info) -> ImagenMedicaRespuesta:
        payload = dict(
            id_paciente = id_paciente,
            url = url
            )
        comando = dict(
            id = str(uuid.uuid4()),
            time=utils.time_millis(),
            specversion = "v1",
            type = "ComandoCargarImagenMedica",
            ingestion=utils.time_millis(),
            datacontenttype="AVRO",
            service_name = "BFF Web",
            data = payload
        )
        despachador = Despachador()
        info.context["background_tasks"].add_task(despachador.publicar_mensaje, comando, "comando-cargar-imagen-medica", "public/default/comando-cargar-imagen-medica")
        
        return ImagenMedicaRespuesta(mensaje="Procesando Mensaje", codigo=203)