# EXEMPLO 1: ENTIDADE BÁSICA
# Na modelagem de dados, uma "entidade" representa algo do mundo real que queremos guardar no sistema.
# Aqui vamos criar a entidade Cliente em Python usando uma classe.

class Cliente:
    def __init__(self, nome, cpf, email):
        # Aqui estamos armazenando os dados do cliente em atributos da classe.
        # Esses atributos correspondem às "características" da entidade Cliente.
        self.nome = nome
        self.cpf = cpf
        self.email = email

# Criamos duas ocorrências (instâncias) da entidade Cliente.
cliente1 = Cliente("Maria Silva", "12345678900", "maria@email.com")
cliente2 = Cliente("João Souza", "98765432100", "joao@email.com")

# Exibindo os dados armazenados (equivalente a visualizar os registros de uma tabela).
print(cliente1.nome, cliente1.cpf)
print(cliente2.nome, cliente2.cpf)
