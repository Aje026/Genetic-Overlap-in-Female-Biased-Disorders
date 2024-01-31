import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import glob

#getting a list of files to be read
ex_table_files = glob.glob('*_extracted_table.txt')

df_list = []

for file in ex_table_files:
    df = pd.read_csv(file, sep='\t', header=0) 
    
    df_list.append(df)
print(df_list[0])  

# df = pd.read_csv('ldsc_corr_all.csv', sep=';', index_col=0)



# plt.figure(figsize=(20, 15))


# sns.heatmap(df, annot=True, cmap='coolwarm', fmt=".2f")


# plt.title('Correlation Heatmap')

# #plt.show()
# plt.savefig('correlation_heatmap_all.jpg')
# #%%
    
