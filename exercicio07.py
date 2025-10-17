nome = input("Digite seu nome: ")
sexo = input("Digite o seu sexo (F) ou (M): ")
civil = input("Digite o seu estado civil: ")
casade = int(input("Informe quanto tempo você tem de casada: "))
if civil == "casada" and sexo == "F" :
    print("Quanto tempo de casada?")
elif casade >=1 and casade <=50:
    print("Parabens!")
else:
    print("Ok, estaremos encaminhando suas informações.")
