import base64 # Importamos la librería para Base64 y los otros metodos de encriptado
import hashlib

def menu(): # Menu basico donde elegir el tipo de encriptado
    print("\n=== ENCRIPTADOR DE CONTRASEÑAS ===")
    print("1. Base64")
    print("2. SHA-256")
    print("3. SHA-512")
    print("4. MD5")
    print("5. Cifrado César")
    print("0. Salir")

def encrypt_base64(text): # Funcion para encriptar en Base64
    return base64.b64encode(text.encode()).decode()

def encrypt_sha256(text): # Funcion para encriptar en SHA-256
    return hashlib.sha256(text.encode()).hexdigest()

def encrypt_sha512(text): # Funcion para encriptar en SHA-512
    return hashlib.sha512(text.encode()).hexdigest()

def encrypt_md5(text): # Funcion para encriptar en MD5
    return hashlib.md5(text.encode()).hexdigest()

def encrypt_cesar(text, shift=3): # Funcion para encriptar con cifrado césar
    result = ""
    for char in text:
        result += chr((ord(char) + shift) % 256)
    return result

def main():
    while True: # Comprobamos que se ha seleccionado una opcion 
        menu()
        option = input("Selecciona un método: ")

        if option == "0": # Si ponen el 0 salimos del programa
            print("Saliendo...")
            break

        password = input("Introduce la contraseña a encriptar: ")

        # Relacionamos el menu con cada función correspondiente
        if option == "1":
            print("Base64 →", encrypt_base64(password))
        elif option == "2":
            print("SHA-256 →", encrypt_sha256(password))
        elif option == "3":
            print("SHA-512 →", encrypt_sha512(password))
        elif option == "4":
            print("MD5 →", encrypt_md5(password))
        elif option == "5":
            shift = int(input("Desplazamiento del cifrado césar (por defecto 3): ") or 3)
            print("Cifrado césar →", encrypt_cesar(password, shift))
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()
