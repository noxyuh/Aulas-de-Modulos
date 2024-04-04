import moeda

dinheiro = float(input('Digite o preço: '))
print(f'A metade de {moeda.moeda(dinheiro)} é {moeda.metade(dinheiro, True)}')
print(f'O dobro de {moeda.moeda(dinheiro)} é {moeda.dobro(dinheiro, True)}')
print(f'Aumentando 10%, temos {moeda.aumentar(dinheiro, True)}')
print(f'A diminuiçao de 10%, temos {moeda.diminuir(dinheiro, True)}')



