#Vetor Primo:
#Solicite aos alunos que criem um programa que verifique se um número é primo e, em seguida, adicione
#esse número a um vetor de números primos

vetor = []
contador = 0
contador2 = 0
qvfd = 0
while contador == 0 :
    num = int(input('digite um numero ou numero negativo para encerrar : ')) 
    if num < 0 :
        contador = 1
    else :
        while contador2 < num :
            if num %contador2 == 0 :
                qvfd += 1
            