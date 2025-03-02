from dataclasses import dataclass
from .base import ImagenesMedicasQueryBaseHandler
from saludTech.modulos.gestor_archivos.infraestructura.repositorios import (
    RepositorioImagenMedica,
)
from saludTech.seedwork.aplicacion.queries import QueryResultado, Query
from saludTech.seedwork.aplicacion.queries import ejecutar_query as query
from saludTech.modulos.gestor_archivos.aplicacion.mapeadores import MapeadorImagenMedica


@dataclass
class ObtenerImagenesMedicas(Query):
    pass


class ObtenerImagenesMedicasHandler(ImagenesMedicasQueryBaseHandler):

    def handle(self, quey: ObtenerImagenesMedicas):
        repositorio = self.fabrica_repositorio.crear_objeto(
            RepositorioImagenMedica.__class__
        )

        imagenes_medicas_raw = repositorio.obtener_todos()
        imagenes_medicas = []

        for imagen_medica in imagenes_medicas_raw:
            imagenes_medicas.append(
                self.fabrica_imagen_medica.crear_objeto(
                    imagen_medica, MapeadorImagenMedica()
                )
            )

        return QueryResultado(resultado=imagenes_medicas)

    @query.register(ObtenerImagenesMedicas)
    def ejecutar_query_obtener_todos(query: ObtenerImagenesMedicas):
        handler = ObtenerImagenesMedicasHandler()
        return handler.handle(query)
