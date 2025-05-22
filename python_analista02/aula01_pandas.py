import pandas as pd

#Criando a partir de um dicionário
data ={
    'Nome': ['Andre', 'Julia', 'Paula'],
    'Idade': [35,29,50],
    'Cidade': ['Rio de Janeiro', 'Petrópolis', 'Areal']
}

df = pd.DataFrame(data)
#Exibir o DataFrame
print(df)