import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd. read_csv('all_pivoted.csv', index_col='rs_id')
df = df.fillna(0)
df = df.drop(columns='Unnamed: 0')

correlation_matrix = df.corr(method='spearman')

plt.figure(figsize=(15, 15))


sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")


plt.title('Correlation Heatmap')


plt.savefig('correlation_heatmap_4.jpg')
#%%
