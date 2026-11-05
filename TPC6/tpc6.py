


def medias(tabMeteo):
    res = []
    for dia, tmin, tmax, prec in tabMeteo:
        media = (tmin + tmax) / 2
        res.append((dia, media))
    return res


def guardaTabMeteo(t, fnome):
    file = open(fnome, "w")
    for data, tmin, tmax, prec in t:
        ano, mes, dia = data
        file.write(f"{ano}-{mes}-{dia} | {tmin} | {tmax} | {prec} | \n")    
    file.close()   
    return

def carregaTabMeteo(fnome):
    res = []
    file = open(fnome, "r")
    for line in file:
        data, tmin, tmax, prec, _ = line.split("|")           #como vai haver um \n ao fazer o split entre tracos mete-mos o underscore para o sistema saber q e inutil
        ano, mes, dia = data.split("-")
        tuplo = ((ano, mes, dia), tmin, tmax, prec)
        res.append(tuplo)
    file.close()
    return res

def minMin(tabMeteo):
    minima = tabMeteo[0][1]
    for data,tmin,tmax,prec in tabMeteo:
        if tmin < minima:
            minima = tmin
    return minima

def amplTerm(tabMeteo):
    res = []
    for data, tmin, tmax, prec in tabMeteo:
        ampl = tmax - tmin
        res.append((data, ampl))
    return res 

def maxChuva(tabMeteo):
    max_prec = tabMeteo[0][3]
    max_data = tabMeteo[0][0]
    for data,tmin,tmax,prec in tabMeteo:
        if prec > max_prec:
            max_prec = prec
            max_data = data
    return (max_data, max_prec)


def diasChuvosos(tabMeteo, p):
    res = []
    for data,tmin,tmax,prec in tabMeteo:
        if prec > p:
            res.append((data,prec))
    return res


def maxPeriodoCalor(tabMeteo, p):
    max_dias = 0
    dias = 0
    for data, tmin, tmax, prec in tabMeteo:
        if prec < p:
            dias = dias + 1
            if dias > max_dias:
                max_dias = dias
        else:
            dias = 0
    return max_dias


from matplotlib import pyplot as plt
def grafTabMeteo(t):
    y_min = [ tmin for data, tmin, tmax, prec in t]
    y_max = [ tmax for data, tmin, tmax, prec in t]
    x=[f"{data[0]}-{data[1]}-{data[2]}" for data, *_ in t]



    #grafico de linhas - temperaturas
    plt.plot(x,y_min, color="pink", marker="o", label ="Tmin ºC")
    plt.plot(x,y_max, color="blue", marker="o", label ="Tmax ºC")
    plt.title("Temperatura mínima e máxima")
    plt.legend()
    plt.grid()
    plt.show()


    #grafico de barras - precipitaçao
    y_prec = [ prec for data, tmin, tmax, prec in t]
    plt.bar(x,y_prec, color="green",label="Precipitação")
    plt.title("Precipitação")
    plt.legend()
    plt.grid()
    plt.show()
    return



op = " "
tabMeteo1 = [((2022,1,20), 2, 16, 0),((2022,1,21), 1, 13, 0.2), ((2022,1,22), 7, 17, 0.01)]

while op != "0":
    print("---- MENU ----")
    print("1: Calcular a temperatura média de cada dia")
    print("2: Guardar a tabela meteorológica num ficheiro de texto")
    print("3: Carregar a tabela meteorológica de um ficheiro de texto")
    print("4: Calcular a temperatura mínima mais baixa registada na tabela")
    print("5: Calcular a amplitude térmica de cada dia")
    print("6: Calcular o dia em que a precipitação registada teve o seu valor máximo")
    print("7: Dias em que a precipitação foi superior a um valor p")
    print("8: Maior número consecutivo de dias com precipitação abaixo de um limite p")
    print("9: Desenhar gráficos das temperaturas mínimas, máximas e precipitação")
    print("0: Sair da aplicação")
    
    op = input("Insira a sua opção: ")
    if op == "1":
        print(medias(tabMeteo1))
    elif op == "2":
        guardaTabMeteo(tabMeteo1, "meteorologia.txt")
    elif op == "3":
        tabMeteo2 = carregaTabMeteo("meteorologia.txt")
        print(tabMeteo2)
    elif op == "4":
        print(minMin(tabMeteo1))
    elif op == "5":
        print(amplTerm(tabMeteo1))
    elif op == "6":
        print(maxChuva(tabMeteo1))
    elif op == "7":
        p = float(input("Insira o valor de p: "))
        print(diasChuvosos(tabMeteo1, p))
    elif op == "8":
        p = float(input("Insira o valor de p: "))
        print(maxPeriodoCalor(tabMeteo1, p))
    elif op == "9":
        grafTabMeteo(tabMeteo1)
    else:
        print("\nOpção inválida")


print("A sair da aplicação...")