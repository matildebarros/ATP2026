
import random
lista = [1,2,5,6]

def menu():
    print("\n(1) Criar Lista \n(2) Ler Lista\n(3) Soma\n(4) Média\n(5) Maior\n(6) Menor\n(7) estaOrdenada por ordem crescente\n(8) estaOrdenada por ordem decrescente\n(9) Procura um elemento\n(0) Sair\n")




def criaLista():
    lista = []
    n = int(input("Quantos números quer na lista? "))
    for i in range(n):
        elem = random.randint(1, 100)
        lista.append(elem)
    return lista

def leLista(N):
    lista = []
    while N > 0:
        N = N - 1
        num = int(input("Insira um número: "))
        lista.append(num)
    return lista


def somaLista(lista):
    soma = 0
    for elem in lista:
        soma = soma + elem
    return soma

def mediaLista(lista):
    return somaLista(lista)/len(lista)

def maiorLista(lista):
    maior = lista[0]
    for elem in lista:
        if maior < elem:
            maior = elem
    return maior

def menorLista(lista):
    menor = lista[0]
    for elem in lista:
            if menor > elem:
                menor = elem
    return menor

def estaOrdenada(lista):
    res = "Sim"
    i=0
    while i < len(lista)-1 and res == "Sim":
        if lista[i] > lista[i+1]:
            res = "Não"
        i = i+1
    return res

def estaOrdenadaDec(lista):
    res = "Sim"
    i=0
    while i < len(lista)-1 and res == "Sim":
        if lista[i] < lista[i+1]:
            res = "Não"
        i = i+1
    return res


def procura(lista,elem):
    i = 0
    res = -1
    while i < len(lista) and elem != lista[i]:
        i=i+1
    if i < len(lista):
        res = i
    return res



op = ""
while op != "0":
    menu()
    op = input("Escolha uma opção: ")
    if op == "1":
        lista = criaLista()
        print(lista)
    elif op == "2":
        N = int(input("Quantos números quer pôr na lista?"))
        lista = leLista(N)
        print(lista)
    elif op == "3":
        print("A soma é ",somaLista(lista))
    elif op == "4":
        print("A média é ",mediaLista(lista))
    elif op == "5":
        print("O maior elemento é ",maiorLista(lista))
    elif op == "6":
        print("O menor elemento é ",menorLista(lista))    
    elif op == "7":
        print(estaOrdenada(lista))
    elif op == "8":
        print(estaOrdenadaDec(lista))
    elif op == "9":
        n = int(input("Que número quer procurar? "))
        print(procura(lista,n))
    elif op != "0":
        print("Escreva um número de 0 a 9")

if op == "0":
    print("O programa irá sair")
    print(lista)
