def formatar_qtde(qtde):
    qtde_len = len(str(qtde))
    return str(qtde) + (" " * (8 - qtde_len))

def formatar_preco(preco_pao, qtde):
    preco_str = f'{(preco_pao * qtde):.2f}'
    preco_len = len(preco_str)
    return preco_str + (" " * (12 - preco_len))

preco_pao = float(input("Preço do pão: R$"))

print("┌──────────────┬─────────────────────┐")
print("│ Qtde de pães │ Preço dos pães (R$) │")
print("├──────────────┼─────────────────────┤")
print(f'│      1       │       R${formatar_preco(preco_pao, 1)}│')
for qtde in range(2, 51):
    print("├──────────────┼─────────────────────┤")
    print(f'│      {formatar_qtde(qtde)}│       R${formatar_preco(preco_pao, qtde)}│')
print("└──────────────┴─────────────────────┘")