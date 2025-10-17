num_criancas = 0
adultos_pesam_mais_100 = 0
media_criancas = 0
maior_peso_adultos = 0

for i in range(8):
    print(f'Pessoa n°{i + 1}:')
    idade = int(input("Idade: "))

    if idade < 0 or idade > 60:
        print("Faixa etária inválida!")
        continue
    
    peso = float(input("Peso (Kg): "))

    if idade < 13:
        num_criancas += 1
        media_criancas += peso
    else:
        if peso > 100:
            adultos_pesam_mais_100 += 1
        if peso > maior_peso_adultos:
            maior_peso_adultos = peso
    

media_criancas /= 8

print(f'Quantas crianças foram cadastradas: {num_criancas} crianças.')
print(f'Quantos adultos pesam mais que 100Kg: {adultos_pesam_mais_100} adultos.')
print(f'A média de peso entre as crianças: {media_criancas:.2f}Kg.')
print(f'O maior peso entre os adultos: {maior_peso_adultos}Kg.')
