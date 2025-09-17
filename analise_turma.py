alunos = [{"matricula": "2025A01", "nome": "Ana Silva", "nota_final": 8.5, "frequencia": 80.0, "status_matricula": "ativo"},{"matricula": "2025A02", "nome": "Bruno Costa", "nota_final": 6.8, "frequencia": 95.0, "status_matricula": "ativo"},{"matricula": "2025A03", "nome": "Carla Dias", "nota_final": 4.5, "frequencia": 70.0, "status_matricula": "ativo"},{"matricula": "2025A04", "nome": "Daniel Farias", "nota_final": 9.5, "frequencia": 90.0, "status_matricula": "ativo"},{"matricula": "2025A05", "nome": "Elisa Mendes", "nota_final": 7.5, "frequencia": 65.0, "status_matricula": "desligado"},{"matricula": "2025A06", "nome": "Fábio Souza", "nota_final": 9.2, "frequencia": 75.0, "status_matricula": "ativo"},{"matricula": "2025A07", "nome": "Giovana Lima", "nota_final": 6.0, "frequencia": 100.0, "status_matricula": "ativo"},{"matricula": "2025A08", "nome": "Hugo Rocha", "nota_final": 7.0, "frequencia": 74.9, "status_matricula": "ativo"}]

# 1. Filtrar alunos elegíveis: frequência >= 75.0 e status_matricula == "ativo"
alunos_elegiveis = filter(lambda aluno: aluno["frequencia"] >= 75.0 and aluno["status_matricula"] == "ativo", alunos)

# 2. Aplicar bônus de 10% na nota, com limite de 10.0
alunos_com_bonus = map(lambda aluno: {**aluno, "nota_final": min(aluno["nota_final"] * 1.1, 10.0)}, alunos_elegiveis)

# 3. Identificar destaques: nota_final >= 9.0 após o bônus
alunos_destaques = filter(lambda aluno: aluno["nota_final"] >= 9.0, alunos_com_bonus)

# Imprimir o nome e a nota final (com bônus) dos alunos destaque
print("Alunos Destaque:")
for aluno in alunos_destaques:
    print(f'Nome: {aluno["nome"]}, Nota Final: {aluno["nota_final"]:.2f}')