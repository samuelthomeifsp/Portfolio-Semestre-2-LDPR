nomes =[]
idades =[]
num_pessoas=3

for i in range(num_pessoas):
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    nomes.append(nome)
    idades.append(idade)

for j in range(num_pessoas):
    if idades[j]>=18:
        print(f"{nomes[j]} é maior de idade")
    else:
        print(f"{nomes[j]} não é menor de idade")
