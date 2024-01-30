import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('genetic_correlation_psyck.csv', sep=';', index_col=0)



plt.figure(figsize=(15, 15))


sns.heatmap(df, annot=True, cmap='coolwarm', fmt=".2f")


plt.title('Correlation Heatmap')

#plt.show()
plt.savefig('correlation_heatmap_psych.jpg')
#%%
