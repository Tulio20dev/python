#Média de Vetores:
#Desenvolva um programa que calcule a média dos elementos de um vetor
vet = []
contador = 0
while contador < 5 :
    num = int(input('digite um numero: '))
    vet.append(num)
    contador += 1
print("O vetor é: ", vet)

soma = 0
contador = 0
while contador < 5:
    soma = soma + vet[contador]
    contador += 1
media = soma/5
print("A média é : ",media)



