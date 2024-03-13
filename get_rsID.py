import pandas as pd


build37 = pd.read_csv('build37.vcf', sep='\t', header=55)

build38 = pd.read_csv('build38.vcf',sep='\t', header=55)


build37 = build37[['#CHROM', 'POS', 'ID']]
build38 = build38[['#CHROM', 'POS', 'ID']] 

build37 = build37.rename(columns={'#CHROM':'chr', 'POS':'pos'})
build38 = build38.rename(columns={'#CHROM':'chr', 'POS':'pos'})

""" fibromyalgia=pd.read_csv('fibromyalgia_buildGRCh37.tsv',sep='\t')
fibromyalgia=fibromyalgia.rename(columns={'chromosome':'chr','base_pair_location':'pos'})
fibromyalgia_updated = pd.merge(fibromyalgia, build37, on=['chr', 'pos'], how='inner')
fibromyalgia_updated.to_csv('fibromyalgia_updated3.tsv', sep='\t', index=False) """



endometriosis = pd.read_csv('endometriosis_buildgrch37.txt', sep='\t')
endometriosis=endometriosis.rename(columns={'chromosome':'chr','base_pair_location':'pos'})
endometriosis_updated = pd.merge(endometriosis, build37, on=['chr', 'pos'], how='inner')
endometriosis_updated.to_csv('endometriosis_updated3.tsv', index=False, sep='\t')






preeclampsia = pd.read_csv('preeclampsia.tsv', sep='\t')
preeclampsia=preeclampsia.rename(columns={'chromosome':'chr','base_pair_location':'pos'})
preeclampsia_updated = pd.merge(preeclampsia, build38, on=['chr', 'pos'], how='inner')
preeclampsia_updated.to_csv('preeclampsia_updated3.tsv',index=False, sep='\t')


preterm_birth = pd.read_csv('spontanious_preterm_birth.tsv', sep='\t')
preterm_birth=preterm_birth.rename(columns={'chromosome':'chr','base_pair_location':'pos'})
preterm_birth_updated = pd.merge(preterm_birth, build38, on=['chr', 'pos'], how='inner')
preterm_birth_updated.to_csv('preterm_birth_updated3.tsv', index=False, sep='\t')



pcos = pd.read_csv('pcos.txt', sep='\t')
pcos_updated = pd.merge(pcos, build37, on=['chr', 'pos'], how='inner')
pcos_updated.to_csv('pcos_updated3.tsv', index=False, sep='\t') 