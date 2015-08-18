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

#printa na ordem q ta
for pedido in pedidos:
    print('Nome: {}\nSabor: {}' .format(pedido['nome'],pedido['sabor']))

for pedido in pedidos:
    s = 'Nome: {}\nSabor: {}'
    print(s.format(pedido['nome'],pedido['sabor']))
