import pandas as pd

#pcos = pd.read_csv('pcos.txt', sep='\t')
build37 = pd.read_csv('build37.vcf', sep='\t', header=55)
fibromyalgia=pd.read_csv('fibromyalgia_buildGRCh37.tsv', sep='\t' )
#build38 = pd.read_csv('build')


build37 = build37[['#CHROM', 'POS', 'ID']]
#build38 = build38[['#CHROM', 'POS', 'ID']] 

build37 = build37.rename(columns={'#CHROM':'chr', 'POS':'pos'})
#build38 = build38.rename(columns={'#CHROM':'chr', 'POS':'pos'})

fibromyalgia=fibromyalgia.rename(columns={'chromosome':'chr','base_pair_location':'pos'})
fibromyalgia_updated = pd.merge(fibromyalgia, build37, on=['chr', 'pos'], how='inner')
fibromyalgia_updated.to_csv('fibromyalgia_updated2.tsv', sep='\t', index=False)

#build37.to_csv('build37_clean.txt', sep='\t', index=False)
#build38.to_csv('build38_clean.txt', sep='\t', index =False)

""" pcos_updated = pd.merge(pcos, build37, on=['chr', 'pos'], how='inner')
pcos_updated.to_csv('pcos_updated.txt', sep='\t') """