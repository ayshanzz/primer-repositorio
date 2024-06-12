import random

x = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
y = int(input("Introduce la longitud de la contraseña: "))
password = ""
for i in range(y):
    password += random.choice(x)



print("La contraseña generada es:", password)
