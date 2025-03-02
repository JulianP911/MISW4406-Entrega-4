# Entrega 4 - Prueba de concepto (experimentación)

## Entrega 4 - Video prueba de concepto (experimentación)

En el siguiente enlace encontrará el video con los requerimientos solicitados en la entrega 3:
- [Video - Entrega 4]()

## Entrega 4 - Estructura del proyecto

La estructura del proyecto esta basada de la siguiente forma:

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
