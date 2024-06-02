import pandas as pd

#get rsID for datasets where these are missing

#read reference file
build37 = pd.read_csv('build37.vcf', sep='\t', header=55)
build37 = build37[['#CHROM', 'POS', 'ID']]
build37 = build37.rename(columns={'#CHROM':'chr', 'POS':'pos'})

#read files and merge with reference file
fibromyalgia=pd.read_csv('fibromyalgia_buildGRCh37.tsv',sep='\t')
fibromyalgia=fibromyalgia.rename(columns={'chromosome':'chr','base_pair_location':'pos'})
fibromyalgia_updated = pd.merge(fibromyalgia, build37, on=['chr', 'pos'], how='inner')
fibromyalgia_updated.to_csv('fibromyalgia_updated3.tsv', sep='\t', index=False) 



endometriosis = pd.read_csv('endometriosis_buildgrch37.txt', sep='\t')
endometriosis=endometriosis.rename(columns={'chromosome':'chr','base_pair_location':'pos'})
endometriosis_updated = pd.merge(endometriosis, build37, on=['chr', 'pos'], how='inner')
endometriosis_updated.to_csv('endometriosis_updated3.tsv', index=False, sep='\t')


preeclampsia = pd.read_csv('preeclampsia.tsv', sep='\t')
preeclampsia=preeclampsia.rename(columns={'chromosome':'chr','base_pair_location':'pos'})
preeclampsia_updated = pd.merge(preeclampsia, build37, on=['chr', 'pos'], how='inner')
preeclampsia_updated.to_csv('preeclampsia_updated3.tsv',index=False, sep='\t') 

pcos = pd.read_csv('PCOS_summary_data_19092018.txt', sep='\t')
pcos['MarkerName'] = pcos['MarkerName'].str.replace(':ID', '')
pcos[['chr', 'pos']] = pcos['MarkerName'].str.split(':', n=1, expand=True)
pcos = pcos[pcos['chr'] != 'X']
pcos['chr'] = pcos['chr'].astype('int64')
pcos['pos'] = pcos['pos'].astype('int64')
pcos.drop('MarkerName', axis=1, inplace=True)
pcos_updated = pd.merge(pcos, build37, on=['chr', 'pos'], how='inner')
pcos_updated.to_csv('pcos_updated3.tsv', index=False, sep='\t') 
