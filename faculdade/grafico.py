import pandas as pd
import matplotlib.pyplot as plt

# criar dataframe com os dados
df = pd.DataFrame({
    'Intervalo': ['0-2', '2-4', '4-6', '6-8', '8-10'],
    'Frequencia': [3, 20, 15, 8, 23]
})

# converter os intervalos em valores numéricos
df['Valor'] = df['Intervalo'].apply(lambda x: (int(x.split('-')[0]) + int(x.split('-')[1])) / 2)

# definir os limites dos intervalos de classe
bins = [0, 2, 4, 6, 8, 10]

# plotar o histograma
plt.hist(df['Valor'], bins=bins, weights=df['Frequencia'], edgecolor='black')

# configurar o eixo x
plt.xticks(bins)

# adicionar rótulos e título
plt.xlabel('Valor')
plt.ylabel('Frequência')
plt.title('Histograma de Frequências')

# exibir o gráfico
plt.show()

# plotar o gráfico de dispersão
plt.scatter(df['Valor'], df['Frequencia'], marker='o')

# adicionar rótulos e título
plt.xlabel('Valor')
plt.ylabel('Frequência')
plt.title('Gráfico de Dispersão')

# exibir o gráfico
plt.show()
