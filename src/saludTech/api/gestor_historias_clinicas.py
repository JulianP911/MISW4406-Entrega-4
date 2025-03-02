from flask import redirect, render_template, request, session, url_for
from flask import Response
import json

from saludTech.seedwork.aplicacion.comandos import ejecutar_commando
from saludTech.seedwork.aplicacion.queries import ejecutar_query
import saludTech.seedwork.presentacion.api as api
from saludTech.seedwork.dominio.excepciones import ExcepcionDominio
from saludTech.modulos.gestor_archivos.aplicacion.mapeadores import (
    MapeadorImagenMedicaDTOJson,
)
from saludTech.modulos.gestor_archivos.aplicacion.comandos.crear_imagen_medica import (
    CrearImagenMedica,
)

from saludTech.modulos.gestor_archivos.aplicacion.queries.obtener_imagenes_medicas import (
    ObtenerImagenesMedicas,
)

bp = api.crear_blueprint("gestor_archivos", "/gestor_archivos")


@bp.route("/imagen_medica", methods=("POST",))
def crear_imagen_medica():
    try:
        imagen_medica_dict = request.json

        map_imagen_medica = MapeadorImagenMedicaDTOJson()

        imagen_medica_dto = map_imagen_medica.externo_a_dto(imagen_medica_dict)

        comando = CrearImagenMedica(
            fecha_creacion=imagen_medica_dto.fecha_creacion,
            fecha_actualizacion=imagen_medica_dto.fecha_actualizacion,
            id=imagen_medica_dto.id,
            url=imagen_medica_dto.url,
            metadata=imagen_medica_dto.metadata,
            bucket_location=imagen_medica_dto.bucket_location,
            id_paciente=imagen_medica_dict["id_paciente"],
        )

        ejecutar_commando(comando)

        return Response("{}", status=202, mimetype="application/json")

    except ExcepcionDominio as e:
        return Response(
            json.dumps(dict(error=str(e))), status=400, mimetype="application/json"
        )


@bp.route("/imagen_medica", methods=("GET",))
def dar_imagenes_medicas():
    query_resultado = ejecutar_query(ObtenerImagenesMedicas())
    map_imagen_medica = MapeadorImagenMedicaDTOJson()
    resultado = []

    for res in query_resultado.resultado:
        resultado.append(map_imagen_medica.dto_a_externo(res))

    res_dict = []
    for res in resultado:
        del res["metadata"]
        res_dict.append(res)

    return res_dict
