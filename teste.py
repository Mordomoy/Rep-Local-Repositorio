estoque = [20, 15, 10, 30, 3]

def atualizar(elemento, quantidade):
    posicao = elemento -1
    if 0 <= posicao < len(estoque):
        estoque [posicao] -= quantidade
    else: 
        print("elemento invalido!")


