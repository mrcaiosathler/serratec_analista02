import pandas as pd
import numpy as np

# 1. Geração randômica de dados
np.random.seed(42)
alunos = [f'Aluno {i+1:02d}' for i in range(50)]
disciplinas = ['Front-end', 'Back-end', 'Cibersegurança', 'Big Data', 
               'Java', 'Python', '.NET', 'PHP', 'C#']

dados = {
    'nome_aluno': np.random.choice(alunos, size=200),  
    'disciplina': np.random.choice(disciplinas, size=200),
    'nota_prova': np.round(np.random.uniform(0, 10, size=200), 2),
    'nota_trabalho': np.round(np.random.uniform(0, 10, size=200), 2),
    'frequencia': np.random.randint(50, 100, size=200)  # Percentual de frequência
}

# 2. Criação do DataFrame
df_alunos = pd.DataFrame(dados)

# Exibição dos primeiros registros
print(df_alunos.head())