import unittest # Librería para hacer los test
import base64 # Librería para Base64
import hashlib # Librería para SHA-256, SHA-512 y MD5
from programa import ( # Importamos las funciones a testear de nuestro programa
    encrypt_base64,
    encrypt_sha256,
    encrypt_sha512,
    encrypt_md5,
    encrypt_cesar
)

class TestPrograma(unittest.TestCase):

    def test_encrypt_base64(self):
        self.assertEqual(
            encrypt_base64("margaix"), # Testeamos con mi apellido para comprobar si encripta de forma adecuada
            base64.b64encode("margaix".encode()).decode()
        )

    def test_encrypt_sha256(self): # Test para SHA-256
        expected = hashlib.sha256("margaix".encode()).hexdigest()
        self.assertEqual(encrypt_sha256("margaix"), expected) 

    def test_encrypt_sha512(self): # Test para SHA-512
        expected = hashlib.sha512("margaix".encode()).hexdigest()
        self.assertEqual(encrypt_sha512("margaix"), expected)

    def test_encrypt_md5(self): # Test para MD5
        expected = hashlib.md5("margaix".encode()).hexdigest()
        self.assertEqual(encrypt_md5("margaix"), expected)

    def test_encrypt_cesar_1(self): # Test para Cifrado césar con desplazamiento de 3
        self.assertEqual(encrypt_cesar("abc", 3), "def")

    def test_encrypt_cesar_2(self): # Test para Cifrado césar con desplazamiento de 2
        self.assertEqual(encrypt_cesar("abc", 2), "cde")

    def test_encrypt_cesar_3(self): # Test para comprobar que el cifrado césar funciona correctamente con caracteres especiales
        original = chr(250)
        shifted = chr((250 + 10) % 256)
        self.assertEqual(encrypt_cesar(original, 10), shifted)

if __name__ == "__main__":
    unittest.main()
