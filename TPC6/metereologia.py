tabMeteo1 = [((2022,1,20), 2, 16, 0),((2022,1,21), 1, 13, 0.2), ((2022,1,22), 7, 17, 0.01)]

def medias(tabMeteo):
    res = []
    for registo in tabMeteo:
        data, tmin, tmax, _ = registo
        res.append ({data, (tmax+tmin)/2})
    return res 

def guardaTabMeteo(t, fnome):
    f = open ( fnome, "w")
    for registo in t:
        f.write (f"{registo[0][0]}|{registo[0][1]}|{registo[0][2]},{registo[1]}, {registo[2]}, {registo[3]}\n")
    f.close()
    return
guardaTabMeteo(tabMeteo1, "meteorologia.txt")

def carregaTabMeteo(fnome):
    res = []
    f = open (fnome)
    for linha in f:
        campos = linha.split(',')
        data = campos[0].split('|')
        ndata= (int(data[0]), int(data[1]), int(data[2]))
        res.append ( (ndata, float(campos[1]), float(campos[2]), float(campos[3]))) 
    return res
tabMeteo2 = carregaTabMeteo("meteorologia.txt")

def minMin(tabMeteo):
    minima = tabMeteo [0][1]
    for registo in tabMeteo[1:]:
        if minima > registo [1]:
            minima = registo [1]
    return minima

def amplTerm(tabMeteo):
    res = []
    for registo in tabMeteo:
        data, tmin, tmax, _ = registo
        res.append ({data, (tmax-tmin)})
    return res 

def maxChuva(tabMeteo):
    res = []
    precimax = tabMeteo [0][3]
    datamax = tabMeteo [0][0]
    for data, _, _, preci in tabMeteo [1:]:
        if precimax < preci:
            precimax = preci
            datamax = data
    return (datamax, precimax)

def diasChuvosos(tabMeteo, p):
    res = []
    for data, _, _, preci in tabMeteo:
        if preci > p :
            res.append ((data.preci))
    return res

def maxPeriodoCalor(tabMeteo, p):
    maximo = 0
    i = 0
    for registo in tabMeteo1:
        preci = registo [3]
        if preci < p:
            i = i + 1
            if i> maximo:
                maximo = i
            else:
                i = 0
    return maximo

def grafTabMeteo(t):
    y_min = [tmin for data, tmin, *_ in t]
    y_max = [tmax for data, tmin,tmax, *_ in t]
    x = [f"{data[0]} - {data[1]} - {data[2]}" for data, *_ in t]
    print (y_min)
    print(x)

    plt.plot(x, y_min, color="purple", marker="o", label="Temperatura mínima ºC")
    plt.plot(x, y_max, color="pink", marker="o", label="Temperatura máxima ºC")
    plt.legend()
    plt.grid()
    plt.show()
    return
grafTabMeteo(tabMeteo1)

while opcao != 0:
    print("Menu")
    print ("Opção 1: Temperatura media diária.")
    print ("Opção 2: Guardar dados meteorelógicos.")
    print ("Opção 3: Carregar dados meteorelógicos.")
    print ("Opção 4: Temperatura mínima.")
    print ("Opção 5: Amplitude Média diária.")
    print ("Opção 6: Precipitação máxima, respetiva data.")
    print ("Opção 7: Nº de dias com precipitação menor a valor escolhido.")
    print ("Opção 8: Maior número consecutivo de dias com precipitação abaixo de valor escolhido.")
    print ("Opção 9: Gráfico com temperatura máxima e mínima e pluviosidade.")
    print ("Opção 0: Sair da aplicação.")
    opcao = int (input("Opção: "))

    if opcao == 1:
        medias(tabMeteo)
        print(medias(tabMeteo1))
      
    elif opcao == 2:
        guardaTabMeteo(t, fnome)
      
    elif opcao == 3:
        carregaTabMeteo(fnome)
        print(tabMeteo2)
      
    elif opcao == 4:
        minMin(tabMeteo)
        print(minMin(tabMeteo1))

    elif opcao == 5:
        maxChuva(tabMeteo)
        print(amplTerm(tabMeteo1))

    elif opcao == 6:
        p = float(input("Escolha um valor máximo para a precipitação."))
        maxChuva(tabMeteo)
        print(maxChuva(tabMeteo1))

    elif opcao == 7:
        p = float(input("Escolha um valor máximo para a precipitação: "))
        diasChuvosos(tabMeteo, p)
        print (diasChuvosos(tabMeteo, p))

    elif opcao == 8:
        maxPeriodoCalor(tabMeteo, p)
        print (maxPeriodoCalor(tabMeteo1, p))

    elif opcao == 9:
        grafTabMeteo(t)

    elif opcao == 0:
        print("Aplicação terminada.")

    else:
        print("Opção inválida.")