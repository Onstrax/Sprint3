# utils.py
# pip install pycryptodome
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from hashlib import sha256
from base64 import b64encode, b64decode
import binascii


class AESCipher:
    def __init__(self, key):
        self.block_size = 16
        self.key = sha256(key.encode()).digest()[:32]
        self.pad = lambda s: s + (self.block_size - len(s) % self.block_size) * chr(self.block_size - len(s) % self.block_size)
        self.unpad = lambda s: s[:-ord(s[len(s) - 1:])]

    def encrypt(self, data):
        plain_text = self.pad(data)
        iv = get_random_bytes(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_OFB, iv)
        encrypted_data = iv + cipher.encrypt(plain_text.encode())
        return b64encode(encrypted_data).decode()

    def decrypt(self, enc_data):
     try:
          # Asegúrate de que el padding base64 sea correcto
          padding = len(enc_data) % 4
          if padding != 0:
               enc_data += '=' * (4 - padding)  # Añadir relleno necesario

          # Decodificar base64
          enc_data = b64decode(enc_data)

          # Extraer el IV (los primeros 16 bytes)
          iv = enc_data[:self.block_size]
          if len(iv) != self.block_size:
               raise ValueError("El IV debe ser de 16 bytes.")

          # Desencriptar los datos
          cipher = AES.new(self.key, AES.MODE_OFB, iv)
          decrypted_data = cipher.decrypt(enc_data[self.block_size:])
          
          # Desencriptar el texto y eliminar el padding
          data = self.unpad(decrypted_data.decode())

          return data

     except (binascii.Error, ValueError) as e:
          print(f"Error durante la desencriptación: {e}")
          raise ValueError("Error al desencriptar los datos") from e


   
# encripted = AESCipher("Esto es una prueba","Esto es una llave arbitraria 32B").encrypt()
# decripted = AESCipher(encripted,"Esto es una llave arbitraria").decrypt()
# print("Encriptado:",encripted)
# print("Desencriptado:",decripted)
# print(len("Esto es una llave arbitraria 32B"))