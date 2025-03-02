# Entrega 4 - Prueba de concepto (experimentación)

## Entrega 4 - Video prueba de concepto (experimentación)

En el siguiente enlace encontrará el video con los requerimientos solicitados en la entrega 4:
- [Video - Entrega 4]()

## Entrega 4 - Documentación prueba de concepto (experimentación)

En el siguiente enlace encontrará la documentación con los requerimientos solicitados en la entrega 4:
- [Wiki - Entrega 4](https://github.com/JulianP911/MISW4406-Entrega-4/wiki)

## Entrega 4 - Estructura del proyecto

El proyecto se encuentra estructurado en directorios, cada uno de los cuales albergará un microservicio específico de la arquitectura definida, conforme a la siguiente distribución:

- saludTech
- anonimizador
- validador_anonimizador
- modelosIA

Asimismo, cada microservicio emplementa las siguientes capas arquitectónicas, con el propósito de adherirse a los principios del **Diseño Guiado por el Dominio (DDD)**:

- Dominio
- Infraestructura
- Aplicación
- Seedwork

**Importante:** La inclusión de todas estas capas dependerá de los requerimientos específicos de cada microservicio, por lo que, en algunos casos, es posible que no se implementen en su totalidad para algunos microservicios.

La estructura de un microservicio esta basada de la siguiente forma:

- src: En este directorio encuentra el código fuente del proyecto como se describea continuación utilizando una arquitectura hexagonal:
  - **NombreMicroservicio**
    - api
    - config
    - modulos
      - **NombreModulo**
        - aplicación
        - dominio
        - infraestructura
    - seedwork
      - aplicacion
      - dominio
      - infraestructura
      - presentacion
  - Anonimizador
- docs: Directorio con los archivos correspondiente de documentación.
- .gitignore: Archivo con la definición de archivos que se deben ignorar en el repositorio GIT.
- .gitpod.yml: Archivo que define las tareas/pasos a ejecutar para configurar su workspace en Gitpod.
- docker-compose.yml: Archivo que define el entorno de contenedores para Apache Pulsar, configurando servicios esenciales como ZooKeeper, BookKeeper y un broker para gestionar la mensajería distribuida.
- README.md: La documentación del proyecto de SaludTech.
- requirements.txt: Archivo con los requerimientos para el correcto funcionamiento del proyecto librerias Python.

## Entrega 5 - Ejecución del proyecto

> [!NOTE]  
> Se necesita para correr el proyecto tener instalado pip == 22.2.2 y python 3.10.7

A continuación, se describen los pasos iniciales para correr el proyecto:

1. Correr los siguientes comandos para crear el directorio data, en caso de que no exista:
   ```bash
    sudo mkdir -p ./data/zookeeper ./data/bookkeeper
    sudo chown -R 10000 data
   ```
2. Ejecutar el manejador de contenedoras con el siguiente comando: `docker compose up` para inicia Apache Pulsar y sus dependencias asociadas.
3. Instalar las dependencias con `pip install -r requirements.txt` necesarias para el proyecto.

### Microservicio saludTech

A continuación, se describen el comando para ejecutar el microservicio **saludTech**:

```bash
   flask --app src/saludTech/api/ run
```

**Importante:** Esta aplicación corre en el puerto 5000.

### Microservicio anonimizador

A continuación, se describen el comando para ejecutar el microservicio **anonimizador**:

```bash
   flask --app src/anonimizador/api/ run -p 5001
```

**Importante:** Esta aplicación corre en el puerto 5001.

### Microservicio validadorAnonimizador

A continuación, se describen el comando para ejecutar el microservicio **validador_anonimizador**:

```bash
   flask --app src/validador_anonimizador/api/ run -p 5002
```

**Importante:** Esta aplicación corre en el puerto 5002.

### Microservicio modelosIA

A continuación, se describen el comando para ejecutar el microservicio **modelosIA**:

```bash
   flask --app src/validador_anonimizador/api/ run -p 5003
```

**Importante:** Esta aplicación corre en el puerto 5003.
