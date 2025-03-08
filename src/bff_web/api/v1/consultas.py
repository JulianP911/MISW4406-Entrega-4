import strawberry
from .esquemas import *

@strawberry.type
class Query:
    imagenesMedicas: typing.List[ImagenMedica] = strawberry.field(resolver=obtener_imagenes)