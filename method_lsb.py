#!/bin/python

#
#fuentes:
#https://towardsdatascience.com/hiding-data-in-an-image-image-steganography-using-python-e491b68b1372
#https://medium.com/swlh/lsb-image-steganography-using-python-2bbbee2c69a2
#https://www.thepythoncode.com/article/hide-secret-data-in-images-using-steganography-python
#


import numpy as np
from PIL import Image

print("""
      -----------------------------------------------------
      Script para encontrar mensajes utilizando
      el metodo lsb (bits menos significativo) para
      imagenes tipo RGBA, en el caso de una imagen RGB
      el valor de n es 3, se puede hacer un IF comprobando
      el valor de imagen.mode
      ----------------------------------------------------
      """)


imagen = input("\n\nIngrese la ruta de la imagen y el nombre: ")
#imagen = "desafio.png" #Definir la ubicación de la imagen

print(f"[*] Abrimos la imagen {imagen}")
img = Image.open(imagen, 'r') #Abrimos la imagen en modo lectura



print("[*] Creando la matriz de pixles")
array = np.array(list(img.getdata())) # convertimos en una array de numpy
n=4 #RGBA si es RGB sería 3, pero nuestra imagen es n4
total_pixels = array.size//n # dividimos el tamaño de la matriz, 
#por la cantidad de canales que tiene la imagen 
# en nuestro caso es 4, y es // porque necesitamos que no tenga decimales.

hidden_bits = "" # creamos una variable hidden_bits
#Vamos a recorrer todos los pixeles.

print("[*] Recolectando los bits menos significativos")
for p in range(total_pixels):
    for q in range(0, 3): # una vez entro de los pixeles vamos a recorrer las tuplas internas 
        #que contienen lo valor (r),(g),(b),(a)
        hidden_bits += (bin(array[p][q])[-1]) # de cada una de esas posiciones tomamos el 
        #ultimo bit solamente.

#hacemos un bucle anidado que recorrar un rango de 0 hasta el largo de la cadena
# de hidden_bits saltando de 8 espacios, luego iremos tomando esos valor y colocando 
# nuevamente en la variable pasando de bits a byte.
hidden_bits = [hidden_bits[i:i+8] for i in range(0, len(hidden_bits), 8)]


print("[*] Comprobando si existe mensajes")
message = "" #definimos variable para volcar los valores encontrados.
#ahora recorremos toda la lista de bytes y los iremos decodificando
for i in range(len(hidden_bits)):
    message +=chr(int(hidden_bits[i],2)) #pasamos de binario a decimal y luego a caracter

print(f'[*] El mensaje encontrado fue: {message}') #Aquí nos quedará el mensaje.


