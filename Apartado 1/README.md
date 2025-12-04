# Apartado 1

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


