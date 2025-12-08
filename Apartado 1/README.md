# Apartado 1
---
En este apartado vamos a realizar un programa simple en python. 
Este esta orientado en el encriptado de contraseñas, es un script simple el cual desplega un menú donde podemos elegir el tipo de encriptado que queremos realizar a nuestra contraseña:

```
=== ENCRIPTADOR DE CONTRASEÑAS ===
1. Base64
2. SHA-256
3. SHA-512
4. MD5
5. Cifrado César
0. Salir
Selecciona un método: 
```
Mediante números podemos seleccionar el tipo de crifrado y acto seguido nos permite introducir la contraseña.

```
=== ENCRIPTADOR DE CONTRASEÑAS ===
1. Base64
2. SHA-256
3. SHA-512
4. MD5
5. Cifrado César
0. Salir
Selecciona un método: 1
Introduce la contraseña a encriptar: Pau Margaix
Base64 → UGF1IE1hcmdhaXg=
```

En el caso del código cesar debemos de agregar el número de desplazamiento:
```
=== ENCRIPTADOR DE CONTRASEÑAS ===
1. Base64
2. SHA-256
3. SHA-512
4. MD5
5. Cifrado César
0. Salir
Selecciona un método: 5
Introduce la contraseña a encriptar: Pau Margaix
Desplazamiento del cifrado César (por defecto 3): 12
Cifrado César → \m,Ym~smu
```
---
## Test unitarios

Para el correcto funcionamiento del programa se han generado varios test unitarios en pro de asegurar que las conversiones están funcionando de forma correcta.
Para estos test se ha usado mi apellido, para hacer todas las comprobaciones se han desarollado 7 test unitarios, cada uno de ellos comprueba la codificación y decodificación de la misma palabra y comprobamos que sea el resultado esperado.

---
### Comandos usados
*Estos comandos han sido ejecutados desde la terminal del editor de código VSCode, estando en el directorio donde se encuentran los 2 archivos .py*

Ejecución del programa: 
`python3 programa.py`

Ejecución de los test unitarios: 
`python3 -m unitest`
