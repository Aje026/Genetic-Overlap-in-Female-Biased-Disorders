import pandas as pd


build37 = pd.read_csv('build37.vcf', sep='\t', header=55)
build38 = pd.read_csv('build38.vcf',sep='\t', header=55)


build37 = build37[['#CHROM', 'POS', 'ID']]
build38 = build38[['#CHROM', 'POS', 'ID']] 

build37 = build37.rename(columns={'#CHROM':'chr', 'POS':'pos'})
build38 = build38.rename(columns={'#CHROM':'chr', 'POS':'pos'})


gh = pd.read_csv('metal_geshtn_European_allBiobanks_omitNone_1.txt', sep='\t')
gh = gh.drop(columns=['MarkerName'])
gh = gh.rename(columns={'Chromosome': 'chr', 'Position': 'pos'})
gh_updated = pd.merge(gh,build38,on=['chr', 'pos'], how='inner')
gh_updated.to_csv('gh_updated.tsv', index=False, sep='\t')


preec = pd.read_csv('metal_preec_European_allBiobanks_omitNone_1.txt', sep='\t')
preec = preec.drop(columns=['MarkerName'])
preec = preec.rename(columns={'Chromosome': 'chr', 'Position': 'pos'})
preec_updated = pd.merge(preec,build38,on=['chr', 'pos'], how='inner')
preec_updated.to_csv('preec_updated.tsv', index=False, sep='\t')


pcos = pd.read_csv('PCOS_summary_data_19092018.txt', sep='\t')
pcos['MarkerName'] = pcos['MarkerName'].str.replace(':ID', '')
pcos[['chr', 'pos']] = pcos['MarkerName'].str.split(':', n=1, expand=True)
pcos = pcos[pcos['chr'] != 'X']
pcos['chr'] = pcos['chr'].astype('int64')
pcos['pos'] = pcos['pos'].astype('int64')
pcos.drop('MarkerName', axis=1, inplace=True)
pcos_updated = pd.merge(pcos, build37, on=['chr', 'pos'], how='inner')
pcos_updated.to_csv('pcos_updated3.tsv', index=False, sep='\t') 