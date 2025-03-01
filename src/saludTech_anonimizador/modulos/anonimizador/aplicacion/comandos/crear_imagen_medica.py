# from saludTech_anonimizador.seedwork.aplicacion.comandos import Comando
# from saludTech_anonimizador.modulos.anonimizador.aplicacion.dto import ItinerarioDTO, ReservaDTO
# from .base import CrearReservaBaseHandler
# from dataclasses import dataclass, field
# from saludTech_anonimizador.seedwork.aplicacion.comandos import ejecutar_commando as comando

# from saludTech_anonimizador.modulos.anonimizador.dominio.entidades import Reserva
# from saludTech_anonimizador.seedwork.infraestructura.uow import UnidadTrabajoPuerto
# from saludTech_anonimizador.modulos.anonimizador.aplicacion.mapeadores import MapeadorReserva
# from saludTech_anonimizador.modulos.anonimizador.infraestructura.repositorios import (
#     RepositorioReservas,
# )


# @dataclass
# class AnonimizarImagen(Comando):
#     fecha_creacion: str
#     fecha_actualizacion: str
#     id: str
#     url: str
#     metadata: dict


# class AnonimizarImagenHandler(CrearReservaBaseHandler):

#     def handle(self, comando: AnonimizarImagen):
#         reserva_dto = ReservaDTO(
#             fecha_actualizacion=comando.fecha_actualizacion,
#             fecha_creacion=comando.fecha_creacion,
#             id=comando.id,
#             itinerarios=comando.itinerarios,
#         )

#         reserva: Reserva = self.fabrica_vuelos.crear_objeto(
#             reserva_dto, MapeadorReserva()
#         )
#         reserva.crear_reserva(reserva)

#         repositorio = self.fabrica_repositorio.crear_objeto(
#             RepositorioReservas.__class__
#         )

#         UnidadTrabajoPuerto.registrar_batch(repositorio.agregar, reserva)
#         UnidadTrabajoPuerto.savepoint()
#         UnidadTrabajoPuerto.commit()


# @comando.register(CrearReserva)
# def ejecutar_comando_crear_reserva(comando: CrearReserva):
#     handler = CrearReservaHandler()
#     handler.handle(comando)
