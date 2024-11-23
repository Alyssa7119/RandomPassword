import random

datos = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

longitud = int(input("¿Qué tan larga deseas tu contraseña?: "))

password = ""

for i in range(longitud):
    p = random.choice(datos)
    password += p     
print(password)    