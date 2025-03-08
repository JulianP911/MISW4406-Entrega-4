from abc import ABC, abstractmethod
from saludTech.seedwork.aplicacion.comandos import Comando
from saludTech.seedwork.dominio.eventos import EventoDominio
from dataclasses import dataclass
from .comandos import ejecutar_commando
import uuid
import datetime

class CoordinadorSaga(ABC):
    id_correlacion: uuid.UUID

    @abstractmethod
    def persistir_en_saga_log(self, mensaje):
        ...

    @abstractmethod
    def construir_comando(self, evento: EventoDominio, tipo_comando: type) -> Comando:
        ...

    def publicar_comando(self,evento: EventoDominio, tipo_comando: type):
        print('publicar_comando-------------------------')
        print(evento)
        print(tipo_comando)
        comando = self.construir_comando(evento, tipo_comando)
        print('comando-------------------------')
        print(comando)

    @abstractmethod
    def inicializar_pasos(self):
        ...
    
    @abstractmethod
    def procesar_evento(self, evento: EventoDominio):
        ...

    @abstractmethod
    def iniciar():
        ...
    
    @abstractmethod
    def terminar():
        ...

class Paso():
    id_correlacion: uuid.UUID
    fecha_evento: datetime.datetime
    index: int

@dataclass
class Inicio(Paso):
    index: int = 0

@dataclass
class Fin(Paso):
    index: int

@dataclass
class Transaccion(Paso):
    index: int
    comando: Comando
    evento: EventoDominio
    error: EventoDominio
    compensacion: Comando
   # exitosa: bool


class CoordinadorOrquestacion(CoordinadorSaga, ABC):
    pasos: list[Paso]
    index: int
    
    def obtener_paso_dado_un_evento(self, evento: EventoDominio):
        print('evento----------------------------')
        print(evento)
        for i, paso in enumerate(self.pasos):
            if not isinstance(paso, Transaccion):
                continue

            if isinstance(evento, paso.evento) or isinstance(evento, paso.error):
                return paso, i
        raise Exception("Evento no hace parte de la transacción")
    def es_primera_transaccion(self, index):
        return index == 0

    def es_ultima_transaccion(self, index):
        print('ultima transaccion-----------------')
        print(index)
        print(len(self.pasos))
        #return len(self.pasos) - 1
        return index == len(self.pasos) - 1

    def procesar_evento(self, evento: EventoDominio):
        print('evento-------------------------procesar---')
        print(evento)
        print(type(evento))
        print('pasos-------------------------')
        print(self.pasos)
        paso, index = self.obtener_paso_dado_un_evento(evento)
        print('obtener_paso_dado_un_evento-------------------------')
        print(paso)
        print(index)
        if self.es_ultima_transaccion(index+1) and not isinstance(evento, paso.error):
            self.terminar()
        elif self.es_primera_transaccion(index) and not isinstance(evento, paso.error):
            self.iniciar()
        elif isinstance(evento, paso.error):
            print('pasos--------error-----------------')
            print(paso)
            print(paso.error)
            self.publicar_comando(evento, self.pasos[index-1].compensacion)
        elif isinstance(evento, paso.evento):
            print('pasos--------evento-----------------')
            print(paso)
            print(paso.evento)
            self.publicar_comando(evento, self.pasos[index+1].compensacion)