import random

f = open('tokens.json', 'a')

chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
for n in range(0, 1000):
    token =''
    for i in range(0, 100):
        token += random.choice(chars)
    f.write(f'"{token}",\n')

