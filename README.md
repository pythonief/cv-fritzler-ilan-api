# Curriculum API
## Fritzler Ilan Emanuel >>> github: _pythonief_

Una API simple para consumir imformacion sobre mi curriculum, a su vez que es una manera interesante de darme a conocer a otros desarrolladores y compañias.

- Accede a la informacion relacionada de mi contacto
- Utilizala en Postman o el cliente que desees
- Mandame un mensaje mediante la api. Lo voy a recibir! 🙂  [WIP]

## Como consumirla:


#### _Verificar los endpoint disponibles_


 ```sh
[GET] "/" 
```
Da una vision clara de los endpoints disponible para consumo en la api

```
[POST] "/message/send" 
```
Capos de formulario requeridos: 
| FormFieldName | Description | Required |
| ------ | ------ | ------ |
| name | Nombre del remitente |✅|
| email | Email del remitente |✅|
| message | El mensaje a enviar |✅|
| phone | Telefono de contacto del remitente |❌


Recibe mediante peticion POST un formulario con los campos name, email, message y phone(opcional) el cual sera guardado como registro en la base de datos y enviara un email tanto remitente como al receptor

## Si se desea clonar el repositorio
### ¿Cómo lo configuro?

#### _En principio necesitaran tener un gestor de base de datos instalado_ 

## Windows:

Instalar y activar el entorno virtual
```sh
~$ python -m venv venv
~$ ./venv/Scripts/activate
```

Utilizar pip para instalar las dependencias asociadas
```sh
~(venv)$ pip install -r requirements/dev.txt
```

Ejecutar
```sh
~(venv)$ python run.apy
```

## Linux:

Instalar y activar el entorno virtual
```sh
~$ python3 -m venv venv
~$ source ./venv/bin/activate
```

Utilizar pip para instalar las dependencias asociadas
```sh
~(venv)$ pip install -r requirements/dev.txt
```

## Luego de la instalación
Crear archivo .env en el directorio raiz el cual almacenara tus variables de entorno de las cuales se alimentara el proyecto. 
_¡Esto es importante para mantener la seguridad de tus claves privadas!_
```sh
~(venv)$ touch .env
```

Dentro del archivo se necesitaran las siguientes configuraciones para funcionar

```sh
MODE="dev" | "prod" (Si ya fueron declaradas las configuraciones para producción)
DB_URI="" # Completar con la uri adecuada a tu DB
SECRET_KEY=""
```

## Ejecutar
```sh
~(venv)$ python3 run.apy
```

Verifica que tu servidor este corriendo navegando al siguiente enlace del servidor local en tu navegador preferido

```sh
127.0.0.1:8000
```
O mejor aún probalo con Postman!
