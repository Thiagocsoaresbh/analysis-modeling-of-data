# EXEMPLO 5: REGRAS DE NEGÓCIO E VALIDAÇÕES
# Na modelagem de dados, regras de negócio são restrições que definem como os dados devem se comportar.
# Aqui vamos simular algumas regras clássicas usando Python.

class Cliente:
    clientes_registrados = {}  # dicionário para garantir unicidade de CPF
    
    def __init__(self, nome, cpf, email):
        # Regra 1: CPF deve ser único
        if cpf in Cliente.clientes_registrados:
            raise ValueError("Erro: CPF já cadastrado!")
        
        # Regra 2: Validação simples de email
        if "@" not in email:
            raise ValueError("Erro: E-mail inválido!")
        
        self.nome = nome
        self.cpf = cpf
        self.email = email
        
        # Adiciona o cliente ao "banco" (simulado em memória)
        Cliente.clientes_registrados[cpf] = self

class Pedido:
    def __init__(self, numero, cliente):
        self.numero = numero
        self.cliente = cliente
        self.itens = []
    
    def adicionar_item(self, item):
        # Adiciona um item ao pedido
        self.itens.append(item)
    
    def fechar_pedido(self):
        # Regra 3: Pedido só pode ser fechado se tiver ao menos 1 item
        if len(self.itens) == 0:
            raise ValueError("Erro: Pedido não pode ser fechado sem itens!")
        print(f"Pedido {self.numero} do cliente {self.cliente.nome} foi fechado com {len(self.itens)} item(s).")

# ---------- TESTES PRÁTICOS ----------

# Criando clientes válidos
cliente1 = Cliente("Maria Silva", "12345678900", "maria@email.com")

# Tentando cadastrar cliente com CPF repetido
try:
    cliente2 = Cliente("João Souza", "12345678900", "joao@email.com")
except ValueError as e:
    print(e)

# Tentando cadastrar cliente com email inválido
try:
    cliente3 = Cliente("Carlos Pereira", "98765432100", "carlospereira.com")
except ValueError as e:
    print(e)

# Criando um pedido
pedido1 = Pedido(101, cliente1)

# Tentando fechar sem itens (não pode)
try:
    pedido1.fechar_pedido()
except ValueError as e:
    print(e)

# Adicionando item e fechando corretamente
pedido1.adicionar_item("Notebook")
pedido1.fechar_pedido()
