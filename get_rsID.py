import pandas as pd


#build37 = pd.read_csv('build37.vcf', sep='\t', header=55)

build38 = pd.read_csv('build38.vcf',sep='\t', header=55)


#build37 = build37[['#CHROM', 'POS', 'ID']]
build38 = build38[['#CHROM', 'POS', 'ID']] 

#build37 = build37.rename(columns={'#CHROM':'chr', 'POS':'pos'})
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



""" pb = pd.read_csv('preterm_birth_lifted.bed', sep='\t', header=None)
pb = pb.rename(columns={0:'chr',1:'pos'})
pb = pb[['chr','pos']]
pb['pos'] = pb['pos'].astype(int)
pb['chr'] = pb['chr'].str.replace('chr','')
pb_updated = pd.merge(pb, build38,on=['chr', 'pos'], how='inner')
pb_updated.to_csv('pb_updated.tsv', index=False, sep='\t')


mg = pd.read_csv('myasthenia_lifted.bed', sep='\t', header=None)
mg = mg.rename(columns={0:'chr',1:'pos'})
mg = mg[['chr','pos']]
mg['pos'] = mg['pos'].astype(int)
mg['chr'] = mg['chr'].str.replace('chr','')
mg_updated = pd.merge(mg, build38,on=['chr', 'pos'], how='inner')
mg_updated.to_csv('mg_updated.tsv', index=False, sep='\t')


gdm = pd.read_csv('gdm_lifted.bed', sep='\t', header=None)
gdm = gdm.rename(columns={0:'chr',1:'pos'})
gdm = gdm[['chr','pos']]
gdm['pos'] = gdm['pos'].astype(int)
gdm['chr'] = gdm['chr'].str.replace('chr','')
gdm_updated = pd.merge(gdm, build38,on=['chr', 'pos'], how='inner')
gdm_updated.to_csv('gdm_updated.tsv', index=False, sep='\t') """


""" fibromyalgia=pd.read_csv('fibromyalgia_buildGRCh37.tsv',sep='\t')
fibromyalgia=fibromyalgia.rename(columns={'chromosome':'chr','base_pair_location':'pos'})
fibromyalgia_updated = pd.merge(fibromyalgia, build37, on=['chr', 'pos'], how='inner')
fibromyalgia_updated.to_csv('fibromyalgia_updated3.tsv', sep='\t', index=False) """



""" endometriosis = pd.read_csv('endometriosis_buildgrch37.txt', sep='\t')
endometriosis=endometriosis.rename(columns={'chromosome':'chr','base_pair_location':'pos'})
endometriosis_updated = pd.merge(endometriosis, build37, on=['chr', 'pos'], how='inner')
endometriosis_updated.to_csv('endometriosis_updated3.tsv', index=False, sep='\t')"""






""" preeclampsia = pd.read_csv('preeclampsia.tsv', sep='\t')
preeclampsia=preeclampsia.rename(columns={'chromosome':'chr','base_pair_location':'pos'})
preeclampsia_updated = pd.merge(preeclampsia, build37, on=['chr', 'pos'], how='inner')
preeclampsia_updated.to_csv('preeclampsia_updated3.tsv',index=False, sep='\t') """


""" preterm_birth = pd.read_csv('GCST90271753_pretermbirth.tsv', sep='\t')
preterm_birth=preterm_birth.rename(columns={'chromosome':'chr','base_pair_location':'pos'})
preterm_birth_updated = pd.merge(preterm_birth, build38, on=['chr', 'pos'], how='inner')
preterm_birth_updated.to_csv('preterm_birth_updated4.tsv', index=False, sep='\t') """



pcos = pd.read_csv('PCOS_summary_data_19092018.txt', sep='\t')
pcos['MarkerName'] = pcos['MarkerName'].str.replace(':ID', '')
pcos[['chr', 'pos']] = pcos['MarkerName'].str.split(':', n=1, expand=True)
pcos = pcos[pcos['chr'] != 'X']
pcos['chr'] = pcos['chr'].astype('int64')
pcos['pos'] = pcos['pos'].astype('int64')
pcos.drop('MarkerName', axis=1, inplace=True)
pcos_updated = pd.merge(pcos, build37, on=['chr', 'pos'], how='inner')
pcos_updated.to_csv('pcos_updated3.tsv', index=False, sep='\t') 