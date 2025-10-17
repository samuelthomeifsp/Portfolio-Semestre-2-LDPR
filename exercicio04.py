num_pessoas = int(input("Digite o número de pessoas: "))
qtde_jovens = 0
qtde_adultos = 0
qtde_idosos = 0

for i in range(num_pessoas):
    idade = int(input(f'Digite a idade da {i + 1}° pessoa: '))
    if idade < 0:
        print("Idade inválida!")
    elif idade < 18:
        print("Essa pessoa é um jovem.")
        qtde_jovens += 1
    elif idade < 60:
        print("Essa pessoa é um adulto.")
        qtde_adultos += 1
    else:
        print("Essa pessoa é um idoso.")
        qtde_idosos += 1

print("Qtde. de jovens:", qtde_jovens)
print("Qtde. de adultos:", qtde_adultos)
print("Qtde. de idosos:", qtde_idosos)

if qtde_jovens > qtde_adultos and qtde_jovens > qtde_idosos:
    print("O maior é a qtde. de jovens!")
elif qtde_adultos > qtde_jovens and qtde_adultos > qtde_idosos:
    print("O maior é a qtde. de adultos!")
elif qtde_idosos > qtde_jovens and qtde_idosos > qtde_adultos:
    print("O maior é a qtde. de idosos!")
elif qtde_jovens == qtde_adultos or qtde_adultos == qtde_idosos or qtde_jovens == qtde_idosos:
    print("Um ou mais qtdes. são iguais!")


