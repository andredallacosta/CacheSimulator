import random
import sys

file = open('addresses.txt', 'w')

#Converte o inteiro para uma string com seu valor em binario
def decimalToBinary(n):  
    return bin(n).replace("0b", "")

#A quantidade de enderecos gerados e o argumento passado na chamada do codigo
n = sys.argv[1] 
for i in range(int(n)/2):
	address = random.randint(0, 100)
	num = decimalToBinary(address)
	for j in range(32 - len(num)):
		num = '0' + num
	file.write(num + '\n')
for j in range(int(n)/2):
	address = random.randint(0, 10000)
	num = decimalToBinary(address)
	for j in range(32 - len(num)):
		num = '0' + num
	file.write(num + '\n')
file.close()
