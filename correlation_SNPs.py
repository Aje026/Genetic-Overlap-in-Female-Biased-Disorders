import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('ldsc_corr_all.csv', sep=';', index_col=0)



plt.figure(figsize=(20, 15))


sns.heatmap(df, annot=True, cmap='coolwarm', fmt=".2f")


plt.title('Correlation Heatmap')

#plt.show()
plt.savefig('correlation_heatmap_psych.jpg')
#%%
