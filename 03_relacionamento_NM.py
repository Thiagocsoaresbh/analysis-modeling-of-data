# EXEMPLO 3: RELACIONAMENTO N:M
# Em um relacionamento muitos-para-muitos, uma entidade pode estar ligada a várias outras e vice-versa.
# Exemplo clássico: Alunos ↔ Disciplinas

class Aluno:
    def __init__(self, nome):
        self.nome = nome
        self.disciplinas = []  # Lista que guardará em quais disciplinas o aluno está matriculado.

    def matricular(self, disciplina):
        # Quando um aluno se matricula em uma disciplina, precisamos registrar dos dois lados.
        self.disciplinas.append(disciplina)
        disciplina.alunos.append(self)

class Disciplina:
    def __init__(self, nome):
        self.nome = nome
        self.alunos = []  # Lista de alunos matriculados.

# Criamos alunos e disciplinas
aluno1 = Aluno("Ana")
aluno2 = Aluno("Carlos")
disciplina1 = Disciplina("Banco de Dados")
disciplina2 = Disciplina("Algoritmos")

# Relacionamos (matriculamos) os alunos nas disciplinas.
aluno1.matricular(disciplina1)
aluno1.matricular(disciplina2)
aluno2.matricular(disciplina1)

# Mostrando resultados
print(f"{aluno1.nome} está em {[d.nome for d in aluno1.disciplinas]}")
print(f"A disciplina {disciplina1.nome} tem {[a.nome for a in disciplina1.alunos]} como alunos")
