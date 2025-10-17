resposta = "S"

while resposta == "S" or resposta == "SIM":
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))
    operacao = input("Digite a operação (+, -, * ou /): ")
    if operacao == "+":
        print(f'Resultado de {numero1} + {numero2} = {numero1 + numero2}')
    elif operacao == "-":
        print(f'Resultado de {numero1} - {numero2} = {numero1 - numero2}')
    elif operacao == "*":
        print(f'Resultado de {numero1} * {numero2} = {numero1 * numero2}')
    elif operacao == "/":
        print(f'Resultado de {numero1} / {numero2} = {numero1 / numero2}')
    else:
        print("Operação inválida!")
    resposta = input("Digite se quer um novo resultado (S/N): ").upper()
