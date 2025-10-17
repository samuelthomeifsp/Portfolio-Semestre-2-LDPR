continuar = True
while continuar:
    percentual = 0
    saldo_medio = float(input("Saldo médio: "))

    if saldo_medio < 200:
        print("O cliente não tem direito a crédito.")
    elif saldo_medio < 400:
        percentual = 20
        print(f'O cliente tem direito a R${(saldo_medio * percentual * 0.01):.2f}')
    elif saldo_medio < 600:
        percentual = 30
        print(f'O cliente tem direito a R${(saldo_medio * percentual * 0.01):.2f}')
    else:
        percentual = 40
        print(f'O cliente tem direito a R${(saldo_medio * percentual * 0.01):.2f}')

    print(f'Saldo médio: R${saldo_medio:.2f}')
    print(f'Percentual: {percentual}%')
    print(f'Crédito: R${(saldo_medio * (1 + percentual * 0.01)):.2f}')

    continuar = bool(input("Digite True ou False: "))

