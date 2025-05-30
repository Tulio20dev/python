#Ordenação de Vetores:
#Construa um programa que ordene os elementos de um vetor em ordem crescente

vetor = [90,7,2,78]
contador = 0
contador2 = 0
while contador2 < len(vetor) : 
    while contador < len(vetor) - 1 :
        p1 = vetor[contador] 
        p2 = vetor[contador + 1]

        if p1 > p2 :
            vetor[contador] = p2
            vetor[contador + 1] = p1
        contador += 1
    contador2 += 1
    contador = 0
print(vetor)

