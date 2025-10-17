pontos = int(input("Digite o seu número de pontos para saber a letra da sua classificação: "))

if pontos >= 0 and pontos  <=29 :
    print("E")
elif pontos >=30 and pontos  <=49 :
    print("D")
elif pontos >= 50 and pontos <=69 :
    print("C")
elif pontos >=70 and pontos <=89 :
    print("B")
elif pontos >= 90 and pontos <=100 :
    print("A")
else :
    print("Você não tem os pontos necessarios!")
