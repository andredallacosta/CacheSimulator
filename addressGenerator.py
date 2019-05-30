import random
import sys

file = open('addresses.txt', 'w')

#Converte o inteiro para uma string com seu valor em binário
def decimalToBinary(n):  
    return bin(n).replace("0b", "")

#A quantidade de endereços gerados é o argumento passado na chamada do código
n = sys.argv[1] 
for i in range(int(n)):
	address = random.randint(0, 4294967295)
	num = decimalToBinary(address)
	for j in range(32 - len(num)):
		num = '0' + num 
	file.write(num + '\n')