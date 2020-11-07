
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

def AESEncrypt(key, plaintext ):
  cipher =AES.new(key, AES.MODE_CBC)
  ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))
  return ciphertext

def AESDecrypt(key, ciphertext):
  cipher =AES.new(key, AES.MODE_CBC)
  cipher = AES.new(key, AES.MODE_CBC, cipher.iv)
  plaintext=cipher.decrypt(ciphertext)
  print plaintext

  