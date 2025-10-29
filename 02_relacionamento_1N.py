# EXEMPLO 2: RELACIONAMENTO 1:N
# Em modelagem de dados, um relacionamento 1:N significa "um para muitos".
# Exemplo: Um cliente pode ter muitos pedidos.

class Pedido:
    def __init__(self, numero, cliente):
        # Cada pedido tem um número e está ligado a um cliente.
        self.numero = numero
        self.cliente = cliente

# Criamos dois pedidos associados ao mesmo cliente.
pedido1 = Pedido(101, cliente1)
pedido2 = Pedido(102, cliente1)

# Aqui mostramos como os pedidos estão relacionados ao cliente.
print(f"Pedido {pedido1.numero} feito por {pedido1.cliente.nome}")
print(f"Pedido {pedido2.numero} feito por {pedido2.cliente.nome}")
