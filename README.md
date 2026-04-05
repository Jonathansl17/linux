# Linux Commands — Cheatsheet Automático

_Generado automáticamente desde `linux-commands.txt`._

> Edita **solo** `linux-commands.txt`. El `README.md` se regenera en cada push (GitHub Actions) o al ejecutar el script.

## Índice

- [Comandos de archivos y sistema](#comandos-de-archivos-y-sistema)
- [Comandos para recuperar archivos borrados con sudo rm o sudo rm -rf](#comandos-para-recuperar-archivos-borrados-con-sudo-rm-o-sudo-rm-rf)
- [Comandos de firewall](#comandos-de-firewall)
- [Comandos de servicios](#comandos-de-servicios)
- [Comandos de alias y variables de entorno](#comandos-de-alias-y-variables-de-entorno)
- [Comandos de postgres](#comandos-de-postgres)
- [Comandos python](#comandos-python)
- [Comandos git](#comandos-git)
- [Comandos docker](#comandos-docker)
- [Comandos de Kubernetes (Kind)](#comandos-de-kubernetes-kind)

## Comandos de archivos y sistema

| Comando | Descripción |
|---|---|
| `pwd` | muestra la ruta actual |
| `realpath nombrearchivo` | muestra la ruta de un archivo |
| `cd` | se mueve de carpeta |
| `touch nombreArchivo` | crea un Archivo |
| `nano nombreArchivo` | abre un Archivo |
| `cat nombreArchivo` | muestra el contenido de un archivo |
| `rm nombreArchivo` | borra un archivo |
| `rm -rf nombreCarpeta` | borra una carpeta y su contenido |
| `cp archivo ruta` | copia un archivo en una carpeta |
| `cp -r carpeta ruta` | copia una carpeta y su contenido en otra carpeta |
| `mv archivo ruta` | mueve un archivo |
| `mv` | nombreviejo nuevonombre: renombra un archivo |
| `sudo apt update` | actualiza repositorios |
| `sudo apt upgrade` | actualiza paquetes |
| `chmod +x programa.sh` | da permisos de ejecutable a un script.sh |
| `sh script.sh` | ejecuta un sh |
| `ls` | lista el directorio actual |
| `ls -a` | lista el directorio actual y archivos ocultos |
| `sudo shutdown now` | apaga la computadora |
| `evince nombreArchivo.pdf` | abre un pdf |
| `libreoffice nombreArchivo` | abre cualquier archivo de office (excel, word, power point, etc) |
| `gtk-launch aplicacion` | lanza una app desde terminal |
| `sudo upgrade-grub` | reconstruir gestor de arranca |
| `ctrl+z` | termina un proceso de la consola que no se cierre con ctrl+c |
| `df -h /` | ver espacio utilizado/restante del disco principal |
| `du -sh nombre_carpeta` | ver el size de una carpeta |
| `xournalpp --create-pdf=outputName.pdf file.xopp` | Exporta un archivo xopp a pdf |
| `zip documentName.zip file1.txt file2.png *.js` | comprime archivos en un zip |
| `unzip zipFile.zip -d folderName` | descomprime un archivo zip en una carpeta nueva |
| `sudo kill pid` | detiene un proceso por pid |
| `sudo pkill nombre` | detiene un proceso por nombre |
| `sudo kill -9 pid` | detiene un proceso por pid forzado |
| `sudo pkill -9 nombre` | detiene un proceso por nombre forzado |
| `systemctl list-units --type=service --all` | ver todos los servicios del sistema |
| `mkdir nombrecarpeta` | crea una carpeta |
| `mkdir -p nombrecarpetaPADRE/nombrecarpetaHIJO1/nombrecarpetaHIJO2/...` | crea varias carpetas |

## Comandos para recuperar archivos borrados con sudo rm o sudo rm -rf

| Comando | Descripción |
|---|---|
| `sudo apt install testdisk` | instala testdisk y photorec para recuperar archivos |
| `sudo photorec` | abre el asistente para recuperar archivos borrados |

## Comandos de firewall

| Comando | Descripción |
|---|---|
| `sudo ufw status` | ver estatus del firewall |
| `sudo ufw status numbered` | ver estatus del firewall enumerado |
| `sudo ufw enable` | activar firewall |
| `sudo ufw disable` | desactivar firewall |
| `sudo ufw allow puerto/tcp` | crear regla de entrada en un puerto con tcp |
| `sudo ufw allow puerto/tcp out` | crear regla de salida en un puerto con tcp |
| `sudo lsof -i -P` | ver que procesos estan usando que puertos |
| `sudo lsof -i:puerto` | ver que proceso esta corriendo en un puerto especifico |
| `hostname -I` | ver ip, la primera es la ipv4 |

## Comandos de servicios

| Comando | Descripción |
|---|---|
| `systemctl status servicio` | ver si un servicio esta activo |
| `sudo systemctl enable servicio` | activar un servicio |
| `sudo systemctl disable servicio` | desactivar un servicio |
| `sudo systemctl start servicio` | iniciar un servicio |
| `sudo systemctl stop servicio` | parar un servicio |
| `sudo systemctl restart servicio` | reiniciar un servicio |
| `crontab -e` | editar los cronjobs |

## Comandos de alias y variables de entorno

| Comando | Descripción |
|---|---|
| `nano ~/.bashrc y luego alias nombre='comando'` | pone alias a comandos |
| `source ~/.bashrc` | para que surtan efecto las nuevas configuraciones |

## Comandos de postgres

| Comando | Descripción |
|---|---|
| `sudo -u postgres psql` | entrar la consola de psql como usuario postgres |
| `\l` | listar todas las bases de datos |
| `\c data_base_name` | conectarse a una base de datos o cambiar de una a otra |
| `\q` | retroceder o desconectarse de una base de datos |
| `\dt` | muestra todas las tablas de la base de datos actual |
| `\d table_name` | muestra la estructura de una tabla (columnas, tipos de datos, etc.) |

## Comandos python

| Comando | Descripción |
|---|---|
| `python3 -m venv env` | crear entorno virtual de python |
| `source env/bin/activate` | activar entorno virtual de python |
| `deactivate` | desactivar entorno virtual de python |
| `ps -ef \| grep c.py` | ver procesos de python activos |

## Comandos git

| Comando | Descripción |
|---|---|
| `git add .` | agregar todos los cambios al stage |
| `git commit -m "mensaje"` | crear un commit con los cambios del stage |
| `git push origin rama` | subir los commits a la rama remota |
| `git push -u origin nombrerama` | subir la rama local al repo remoto |
| `git checkout -b nombreRama` | crear una nueva rama |
| `git checkout nombreRama` | cambiar a una rama ya existente |
| `git checkout -b nombre-rama` | Crear y cambiarse a una nueva rama |
| `git switch nombre-rama` | Cambiarse de rama |
| `git reset --soft HEAD~1` | quitar los cambios del stage sin borrar los cambios locales |
| `gh repo create nombre --private/public --source=. --remote=origin --push` | crear un repo en github |
| `gh repo delete nombreRepo` | Eliminar repo desde terminal |

## Comandos docker

| Comando | Descripción |
|---|---|
| `docker --version` | ver version de docker |
| `docker info` | ver informacion general del sistema docker |
| `docker system df` | ver uso de espacio de docker |
| `docker images` | ver imagenes locales |
| `docker build -t nombre:tag .` | construir una imagen docker con nombre, tag default = latest |
| `docker rm contenedor` | borra un contenedor |
| `docker rm -f contenedor` | borra un contenedor forzosamente |
| `docker rmi contenedor` | borra una imagen |
| `docker rmi -f contenedor` | borra una imagen forzosamente |
| `docker ps` | ver contenedores en ejecucion |
| `docker ps -a` | ver todos los contenedores, en ejecucion y detenidos |
| `docker run contenedor` | crea y corre un contenedor a partir de una imagen |
| `docker start contenedor` | ejecuta un contenedor que ya existe |
| `docker stop contenedor` | para la ejecucion de un contenedor que ya existe |
| `docker restart contenedor` | reinicia un contenedor que ya existe |
| `docker inspect contenedor` | informacion completa del contenedor en formato json |
| `docker logs contenedor` | ver logs del contenedor |
| `docker logs -f` | ver logs del contenedor en tiempo real |
| `docker network ls` | listar redes de docker |
| `docker network inspect bridge` | en la parte de Gateway se ve la ip host de docker |
| `docker network connect mi_red mi_contenedor` | conectar contenedor a una red |
| `docker run -d -p puertohost:puertocontenedor --name alias imagendocker:latest` | ejecuta una imagen docker |
| `docker compose up --build` | construye un contenedor con docker compose y lo inicia |
| `docker compose down --rmi all` | borra un docker compose entero, util para no borrar 1 por 1 las images |
| `docker compose up` | inicia un docker compose file |
| `docker compose down` | parar un docker compose file |
| `docker image prune -f` | borra imagenes huerfanas <none> |

## Comandos de Kubernetes (Kind)

| Comando | Descripción |
|---|---|
| `kind create cluster --name nombre --config config.yaml` | crear un cluster de kind con un archivo de configuracion |
| `kind get clusters` | listar clusters de kind |
| `kind delete cluster --name nombre` | eliminar un cluster de kind |
| `kubectl get nodes` | ver nodos del cluster |
| `kubectl get pods -A` | ver todos los pods en todos los namespaces |
