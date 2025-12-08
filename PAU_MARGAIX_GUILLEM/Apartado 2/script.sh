#!/bin/bash

# Obtener MAC, usamos el awk para eliminar la opción que nos de la mac de loopback
MAC=$(ip link show | awk '/ether/ {print $2; exit}')

# Sacamos el nombre del sistema de /etc/os-release y eliminamos las comillas y el pretty_name
SO=$(grep "^PRETTY_NAME" /etc/os-release | cut -d= -f2 | tr -d '"')

# Versión del kernel
KERNEL=$(uname -r)

# Hostname
HOST=$(hostname)

# Obtener usuario
USUARIO=$(whoami)

# Mensaje con toda la información
echo "Información del sistema:
- MAC: $MAC
- Sistema Operativo y Kernel: $SO 
- Kernel: $KERNEL
- Hostname: $HOST
- Usuario: $USUARIO"
