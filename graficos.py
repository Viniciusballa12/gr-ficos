import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv('ecommerce_preparados.csv')
print(df.head().to_string())

#Histograma
plt.hist(df['Nota'])
plt.show()

#Gráfico de Dispersão

sns.jointplot(x='Qtd_Vendidos', y='Preço', data=df,kind='scatter')
plt.show()

#Gráfico de Calor
#Mapa de calor
corr = df[['Marca_Cod', 'Qtd_Vendidos_Cod', 'Material_Cod', 'Temporada_Cod', 'N_Avaliações_MinMax','Nota_MinMax', 'Preço']].corr()
plt.figure(figsize=(10, 8))
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Correlação Vendidos e Preço')

plt.tight_layout()
plt.show()

#Gráficos de Barras
plt.figure(figsize=(10, 6))
df['Qtd_Vendidos'].value_counts().plot(kind='bar', color='#90ee70')
plt.title('Divisão de vendas - 1')
plt.xlabel('Nível de vendas')
plt.ylabel('Quantidade')
plt.xticks(rotation=0)
plt.show()

x = df['Qtd_Vendidos'].value_counts().index
y = df['Qtd_Vendidos'].value_counts().values

plt.figure(figsize=(10, 6))
plt.bar(x, y, color='#60aa65')
plt.title('Divisão de vendas - 1')
plt.xlabel('Nível de vendas')
plt.ylabel('Quantidade')

#Gráfico de Pizza
plt.figure(figsize=(10, 6))
plt.pie(y, labels=x, autopct='%.2f%%', startangle=180)
plt.title('Distribuição de Nível de Educação')
plt.show()

#Gráfico de Densidade
plt.figure(figsize=(10, 6))
sns.kdeplot(df['Nota'], fill=True, color='#863e9c')
plt.title('Densidade de Notas')
plt.xlabel('Notas')
plt.show()

#Gráfico de Regressão
sns.regplot(x='Preço', y='Desconto', data=df, color='#278f65', scatter_kws={'alpha': 0.5, 'color': '#34c289'})
plt.title('Regressão de Preço e Desconto')
plt.xlabel('Preço')
plt.ylabel('Desconto')
plt.show()

