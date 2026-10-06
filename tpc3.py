quem = input("Começo eu (computador) ou tu (jogador)? (computador/jogador) ")
if quem == "computador":
    print("Eu escolho o número 10")
    total = 10
    while total<100: 
        n1 = int(input("Qual é o teu número? "))
        if n1<1 or n1>10:
            print("Escreva um número de 1 a 10")
        total = total + n1
        n2 = 11 - n1
        if total > 88:
            n2 = 100-total
        print("Eu escolho o número ",n2)
        total = total + n2
        print("Total: ",total)
        if total == 100:
            print("Ganhei!")
elif quem == "jogador":
    total = 0 
    while total<100: 
        n1 = int(input("Qual é o teu número? "))
        if n1<1 or n1>10:
            print("Escreva um número de 1 a 10")
        total = total + n1
        if total == 100:
            print("Ganhaste!")
        n2 = 11 - n1
        if total > 90:
            n2 = 100-total
        if total != 100:
            print("Eu escolho o número ",n2)
        total = total + n2
        print("Total: ",total)
        if total == 100 and n2 != 0:
            print("Ganhei!")


else:
    print("erro: escreva apenas computador ou jogador")