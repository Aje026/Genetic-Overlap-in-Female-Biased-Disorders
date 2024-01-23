import numpy as np
import pandas as pd

# Read dataframes
df_genes = pd.read_csv('genes.txt', sep='\t')
df_eqtl = pd.read_csv('eqtl.txt', sep='\t')
df_snps = pd.read_csv('snps.txt', sep='\t')
df_ci = pd.read_csv('ci.txt', sep='\t')

# Filter relevant SNPs
relevant_snps = df_snps[df_snps['uniqID'].isin(df_eqtl['uniqID'].unique())]
dict1 = dict(zip(relevant_snps['uniqID'], relevant_snps['rsID']))

# Add rsID column to df_eqtl
df_eqtl['rsID'] = df_eqtl['uniqID'].map(dict1)

# Filter columns in df_eqtl
df_final = df_eqtl[['rsID', 'symbol', 'db', 'tissue', 'p']].sort_values(by=['rsID', 'symbol', 'p'], ascending=False)

# Check if SNPs have CI
ci_values = df_snps[df_snps['uniqID'].isin(df_eqtl['uniqID'].unique())]['rsID']
ci = ['Yes' if df_ci['SNPs'].str.contains(i).any() else 'No' for i in ci_values]
dict2 = dict(zip(ci_values, ci))

# Add CI column to df_final
df_final['CI'] = df_final['rsID'].map(dict2)

# Save the final dataframe to a file
df_final.to_csv('ADHD_eqtl_ci.txt', sep="\t", header=True, index=False)