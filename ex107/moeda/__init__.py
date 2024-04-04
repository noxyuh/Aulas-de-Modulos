def aumentar(preco=0, formato=False):
    valor_aumento = (preco * 10) / 100
    novo_salario = preco + valor_aumento
    return novo_salario if formato == False else moeda(preco)
    
    
def diminuir(preco=0, formato=False):
    valor_diminuir = (preco * 10) / 100
    salario_desconto = preco - valor_diminuir
    return salario_desconto if formato == False else moeda(salario_desconto)
    

def dobro(preco=0, formato=False):
    dob = preco * 2
    return dob if formato == False else moeda(dob)
    

def metade(preco=0, formato=False):
    meta = preco / 2
    return meta if formato == False else moeda(meta)

def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.',',')