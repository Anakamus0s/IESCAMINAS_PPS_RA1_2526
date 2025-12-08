# Apartado 2 
---
En esta apartdo se ha desarollado un script con la intención de recopilar información del sistema. La información recopilada debe de ser: la MAC, el sistema operativo, hostname de la maquina, el usuario que ha ejecutado el script. Como bonus también se ha agregado la información del kernel.

Para la ejecución de este script se ha realizado en un entorno linux ya en el directorio donde se encuentra el script.
El archivo debe de tener permisos de ejecución, en caso que no tenga se lo deberemos de otorgar con el siguiente comando:
`sudo chmod +x script.sh`

Para la ejecución del script debemos de usar el comando: `./script.sh`

Ejemplo de ejecución:
```
./script.sh
Información del sistema:
- MAC: 04:42:1a:d6:a0:6f
- Sistema Operativo y Kernel: Kali GNU/Linux Rolling 
- Kernel: 6.16.8+kali-amd64
- Hostname: kali
- Usuario: pau
```