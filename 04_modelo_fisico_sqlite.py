# EXEMPLO 4: MODELO FÍSICO COM BANCO DE DADOS
# Aqui vamos usar SQLite (banco de dados leve que já vem no Python).
# Ele serve para mostrar como um DER (conceitual) se transforma em tabelas e relacionamentos reais.

import sqlite3

# ---------------------------
# Escolha o modo de conexão:
# ---------------------------
USAR_MEMORIA = False  # Mude para True se quiser rodar só em memória (dados somem ao fechar)

if USAR_MEMORIA:
    # Banco de dados em memória (não gera arquivo físico, ideal para testes rápidos)
    con = sqlite3.connect(":memory:")
else:
    # Banco de dados salvo em arquivo (persiste em "meu_banco.db")
    con = sqlite3.connect("meu_banco.db")

cur = con.cursor()

# Criando a tabela Cliente (entidade)
cur.execute("""
CREATE TABLE IF NOT EXISTS cliente (
    cpf TEXT PRIMARY KEY,   -- CPF é chave primária (identifica unicamente o cliente).
    nome TEXT,
    email TEXT
)
""")

# Criando a tabela Pedido (entidade) com chave estrangeira para Cliente (relacionamento 1:N)
cur.execute("""
CREATE TABLE IF NOT EXISTS pedido (
    numero INTEGER PRIMARY KEY,
    cliente_cpf TEXT,
    FOREIGN KEY (cliente_cpf) REFERENCES cliente(cpf)
)
""")

# Inserindo dados de exemplo (ocorrências das entidades)
cur.execute("INSERT OR IGNORE INTO cliente VALUES ('12345678900', 'Maria Silva', 'maria@email.com')")
cur.execute("INSERT OR IGNORE INTO pedido VALUES (101, '12345678900')")
cur.execute("INSERT OR IGNORE INTO pedido VALUES (102, '12345678900')")

# Consultando os dados relacionados (JOIN = junção entre tabelas)
cur.execute("""
SELECT cliente.nome, pedido.numero
FROM cliente
JOIN pedido ON cliente.cpf = pedido.cliente_cpf
""")

# Exibindo o resultado da consulta
print("Resultados da consulta (JOIN entre Cliente e Pedido):")
for row in cur.fetchall():
    print(row)

# Salvando as alterações (necessário apenas se for arquivo físico)
con.commit()
con.close()
