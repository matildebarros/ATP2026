minimo = 0
maximo = 100
i = 0

while minimo <= maximo:
    num = (minimo + maximo) // 2
    res = input(f"O seu número é {num}? (escreva acertou/maior/menor) ")
    i = i + 1

    if res == "acertou":
        print(f"O seu número é {num} e o número de tentativas é {i}")
    elif res == "maior":
        minimo = num + 1
    elif res == "menor":
        maximo = num - 1
    else:
        print("erro - escreva apenas maior/menor/acertou")

