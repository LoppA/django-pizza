pedidos = []

#   ''     ''      ''     ''     observacao='sem observacoes'
def criar_pedido(nome, sabor, observacao=None):
    pedido = {}
    pedido['nome'] = nome
    pedido['sabor'] = sabor
    pedido['observacao'] = observacao

    return pedido

print(pedidos)
pedidos.append(criar_pedido('mario', 'pepperoni'))
pedidos.append(criar_pedido('marco', 'presunto'))
print(pedidos)
