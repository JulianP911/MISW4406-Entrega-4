from flask import redirect, render_template, request, session, url_for
from flask import Response
import json

from saludTech.seedwork.aplicacion.comandos import ejecutar_commando
import saludTech.seedwork.presentacion.api as api
from saludTech.seedwork.dominio.excepciones import ExcepcionDominio
from saludTech.modulos.gestor_archivos.aplicacion.mapeadores import (
    MapeadorImagenMedicaDTOJson,
)
from saludTech.modulos.gestor_archivos.aplicacion.comandos.crear_imagen_medica import CrearImagenMedica

bp = api.crear_blueprint("gestor_archivos", "/gestor_archivos")


@bp.route("/imagen_medica", methods=("POST",))
def crear_imagen_medica():
    try:
        imagen_medica_dict = request.json
        print("===========dict===========")
        print(imagen_medica_dict)
        print("===========dict===========")

        map_imagen_medica = MapeadorImagenMedicaDTOJson()

        imagen_medica_dto = map_imagen_medica.externo_a_dto(imagen_medica_dict)

        print("===========map_imagen_medica===========")
        print(imagen_medica_dto)
        print("===========map_imagen_medica===========")

        comando = CrearImagenMedica(
            fecha_creacion=imagen_medica_dto.fecha_creacion,
            fecha_actualizacion=imagen_medica_dto.fecha_actualizacion,
            id=imagen_medica_dto.id,
            url=imagen_medica_dto.url,
            metadata=imagen_medica_dto.metadata,
            id_paciente=imagen_medica_dict["id_paciente"],
        )

        ejecutar_commando(comando)

        return Response('{}', status=202, mimetype='application/json')

    except ExcepcionDominio as e:
        return Response(
            json.dumps(dict(error=str(e))), status=400, mimetype="application/json"
        )
