import pandas as pd

# An example of how some datasets had to be merged with the Human SNP dataset to get rsID


# Read the Human SNP dataset from NCBI an keep only relevant columns
build37 = pd.read_csv('build37.vcf', sep='\t', header=55) 
build37 = build37[['#CHROM', 'POS', 'ID']]
build37 = build37.rename(columns={'#CHROM':'chr', 'POS':'pos'})

# Read sumstats that misses rsID, choose relevant columns and rename as needed
pcos = pd.read_csv('PCOS_summary_data_19092018.txt', sep='\t')
pcos['MarkerName'] = pcos['MarkerName'].str.replace(':ID', '')
pcos[['chr', 'pos']] = pcos['MarkerName'].str.split(':', n=1, expand=True)
pcos = pcos[pcos['chr'] != 'X']
pcos['chr'] = pcos['chr'].astype('int64')
pcos['pos'] = pcos['pos'].astype('int64')
pcos.drop('MarkerName', axis=1, inplace=True)

# Merge sumstats with SNP dataset
pcos_updated = pd.merge(pcos, build37, on=['chr', 'pos'], how='inner')
#pcos_updated = pcos_updated[pcos_updated['p_value'] <= 0.05]  #filter on p-value if needed before using file as input in FUMA
pcos_updated.to_csv('pcos_updated.tsv', index=False, sep='\t') 

