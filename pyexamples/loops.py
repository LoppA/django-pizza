a, b = 1, 2

pedidos = [
    {
        'nome': 'Mario',
        'sabor': 'portuguesa'        
    },
    {
        'nome': 'Marco',
        'sabor': 'presunto'
    }
]

for pedido in pedidos:
    print('Nome: {0}\nSabor: {1}' .format(pedido['nome'],pedido['sabor']))
