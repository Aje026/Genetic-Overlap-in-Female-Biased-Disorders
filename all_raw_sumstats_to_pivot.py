import pandas as pd

psych_dfs = []
other_dfs = []

adhd_df = pd.read_csv('ADHD_meta_Jan2022_iPSYCH1_iPSYCH2_deCODE_PGC.meta', sep=' ')
adhd_df = adhd_df[['SNP', 'P']]
adhd_df = adhd_df.rename(columns={'SNP': 'rs_id', 'P': 'p_value'})
psych_dfs.append(adhd_df)

anxiety_df = pd.read_table('anxiety.meta.full.cc.tbl')
anxiety_df = anxiety_df[['SNPID', 'P.value']]
anxiety_df = anxiety_df.rename(columns={'SNPID': 'rs_id', 'P.value': 'p_value'})
psych_dfs.append(anxiety_df)

aud_df = pd.read_csv('AUDIT_UKB_2018_AJP.txt', sep=' ')
aud_df = aud_df[['rsid', 'p_T']]
aud_df = aud_df.rename(columns={'rsid': 'rs_id', 'p_T': 'p_value'})
psych_dfs.append(aud_df)

anorexia_df = pd.read_csv('pgcAN2.2019-07.vcf.tsv', sep='\t', comment='#')
anorexia_df = anorexia_df[['ID', 'PVAL']]
anorexia_df = anorexia_df.rename(columns={'ID': 'rs_id', 'PVAL': 'p_value'})
psych_dfs.append(anorexia_df)

asd_df = pd.read_csv('iPSYCH-PGC_ASD_Nov2017', sep='\t')
asd_df = asd_df[['SNP', 'P']]
asd_df = asd_df.rename(columns={'SNP': 'rs_id', 'P': 'p_value'})
psych_dfs.append(asd_df)

bpd_df = pd.read_csv('daner_bip_pgc3_nm_noukbiobank', sep='\t')
bpd_df = bpd_df[['SNP', 'P']]
bpd_df = bpd_df.rename(columns={'SNP': 'rs_id', 'P': 'p_value'})
psych_dfs.append(bpd_df)

cud_df = pd.read_csv('CUD_EUR_full_public_11.14.2020', sep=' ')
cud_df = cud_df[['SNP', 'P']]
cud_df = cud_df.rename(columns={'SNP': 'rs_id', 'P': 'p_value'})
psych_dfs.append(cud_df)

hoarding_df = pd.read_csv('hoarding2022.vcf.tsv', sep='\t', comment='#')
hoarding_df = hoarding_df[['ID', 'PVAL']]
hoarding_df = hoarding_df.rename(columns={'ID': 'rs_id', 'PVAL': 'p_value'})
psych_dfs.append(hoarding_df)

mdd_df = pd.read_csv('PGC_UKB_depression_genome-wide.txt', sep=' ')
mdd_df = mdd_df[['MarkerName', 'P']]
mdd_df = mdd_df.rename(columns={'MarkerName': 'rs_id', 'P': 'p_value'})
psych_dfs.append(mdd_df)

ocd_df = pd.read_csv('ocd_aug2017', sep='\t')
ocd_df = ocd_df[['SNP', 'P']]
ocd_df = ocd_df.rename(columns={'SNP': 'rs_id', 'P': 'p_value'})
psych_dfs.append(ocd_df)

# od_1 = pd.read_table('opi.DEPvEXP_EUR.noAF.tbl')
# od_2 = pd.read_table('opi.DEPvUNX_EUR.noAF.tbl')
# od_3 = pd.read_table('opi.EXPvUNX_EUR.noAF.tbl')
# od_1 = od_1[['rsID', 'P-value']]
# od_2 = od_2[['rsID', 'P-value']]
# od_3 = od_3[['rsID', 'P-value']]
#
# od_list = [od_1, od_2, od_3]

od_df = pd.read_table('od')
od_df = od_df[['rsID', 'P-value']]
od_df = od_df.rename(columns={'rsID': 'rs_id', 'P-value': 'p_value'})
psych_dfs.append(od_df)

ptsd_df = pd.read_csv('pts_eur_freeze2_overall.results', sep='\t')
ptsd_df = ptsd_df[['SNP', 'P']]
ptsd_df = ptsd_df.rename(columns={'SNP': 'rs_id', 'P': 'p_value'})
psych_dfs.append(ptsd_df)

scz_df = pd.read_csv('PGC3_SCZ_wave3.european.autosome.public.v3.vcf.tsv', sep='\t', comment='#')
scz_df = scz_df[['ID', 'PVAL']]
scz_df = scz_df.rename(columns={'ID': 'rs_id', 'PVAL': 'p_value'})
psych_dfs.append(scz_df)

tourette_df = pd.read_csv('TS_Oct2018', sep=' ')
tourette_df = tourette_df[['SNP', 'P']]
tourette_df = tourette_df.rename(columns={'SNP': 'rs_id', 'P': 'p_value'})
psych_dfs.append(tourette_df)

panic_df = pd.read_csv('pgc-panic2019.vcf.tsv', sep='\t', header=72)
panic_df = panic_df[['ID', 'PVAL']]
panic_df = panic_df.rename(columns={'ID': 'rs_id', 'PVAL': 'p_value'})
psych_dfs.append(panic_df)

sjogrens_df = pd.read_csv('sjogrens_buildGRCh37.tsv', sep='\t')
sjogrens_df = sjogrens_df[['variant_id', 'p_value']]
sjogrens_df = sjogrens_df.rename(columns={'variant_id': 'rs_id'})
other_dfs.append(sjogrens_df)

epilepsy_df = pd.read_csv('epilepsy.tsv', sep='\t')
epilepsy_df = epilepsy_df[['rs_id', 'p_value']]
other_dfs.append(epilepsy_df)

lupus_df = pd.read_csv('systemic_lupus.txt', sep='\t')
lupus_df = lupus_df[['SNP', 'P-value']]
lupus_df = lupus_df.rename(columns={'SNP': 'rs_id', 'P-value': 'p_value'})
other_dfs.append(lupus_df)

prim_bil_df = pd.read_csv('biliary_chirrosis.tsv', sep='\t', comment='#')
prim_bil_df = prim_bil_df[['variant_id', 'p_value']]
prim_bil_df = prim_bil_df.rename(columns={'variant_id': 'rs_id'})
other_dfs.append(prim_bil_df)

thyroid_df = pd.read_csv('thyroid_buildGRCh37.tsv', sep='\t', comment='#')
thyroid_df = thyroid_df[['variant_id', 'p_value']]
thyroid_df = thyroid_df.rename(columns={'variant_id': 'rs_id'})
other_dfs.append(thyroid_df)

scleroderma_df = pd.read_csv('systemic_scleroderma.txt', header=0, delim_whitespace=True)
scleroderma_df = scleroderma_df[['SNP', 'P']]
scleroderma_df = scleroderma_df.rename(columns={'SNP': 'rs_id', 'P': 'p_value'})
other_dfs.append(scleroderma_df)

myasthenia_df = pd.read_csv('myastheria_gravis.tsv', sep='\t', comment='#')
myasthenia_df = myasthenia_df[['variant_id', 'p_value']]
myasthenia_df = myasthenia_df.rename(columns={'variant_id': 'rs_id'})
other_dfs.append(myasthenia_df)

rh_arthritis_df = pd.read_csv('rheumatoid_arthritis.tsv', sep='\t', comment='#')
rh_arthritis_df = rh_arthritis_df[['variant_id', 'p_value']]
rh_arthritis_df.rename(columns={'variant_id': 'rs_id'})
other_dfs.append(rh_arthritis_df)

ms_df = pd.read_csv('ms.tsv', sep='\t', comment='#')
ms_df = ms_df[['variant_id', 'p_value']]
ms_df = ms_df.rename(columns={'variant_id': 'rs_id'})
other_dfs.append(ms_df)

parkinsons_df = pd.read_csv('parkinson.tsv', sep='\t', comment='#')
parkinsons_df = parkinsons_df[['variant_id', 'p_value']]
parkinsons_df.rename(columns={'variant_id': 'rs_id'})
other_dfs.append(parkinsons_df)

migraine_df = pd.read_csv('migraine.tsv', sep='\t', comment='#')
migraine_df = migraine_df[['variant_id', 'p_value']]
migraine_df.rename(columns={'variant_id': 'rs_id'})
other_dfs.append(migraine_df)


# fibromyalgia.head()

fatigue_df = pd.read_csv('fatigue_buildGRCh37.tsv', sep='\t')
fatigue_df = fatigue_df[['variant_id', 'p_value']]
fatigue_df = fatigue_df.rename(columns={'variant_id':'rs_id'})
other_dfs.append(fatigue_df)

ibs_df = pd.read_csv('IBS.tsv', sep='\t', comment='#')
ibs_df = ibs_df[['variant_id', 'p_value']]
ibs_df = ibs_df.rename(columns={'variant_id': 'rs_id'})
other_dfs.append(ibs_df)

gout_df = pd.read_csv('gout_buildGRCh37.tsv', sep='\t')
gout_df = gout_df[['variant_id', 'p_value']]
gout_df = gout_df.rename(columns={'variant_id':'rs_id'})
other_dfs.append(gout_df)

# lists of disorder names
psych_names = ['adhd', 'asd', 'anorexia', 'anxiety', 'aud', 'bpd', 'cud', 'hoarding', 'mdd', 'ocd', 'od', 'ptsd', 'scz',
               'tourette', 'panic']

other_names = ['sjogrens', 'epilepsy', 'lupus', 'biliary_chorrhosis', 'thyroid_disease', 'scleroderma', 'myasthenia',
               'rh_arthritis', 'ms', 'parkinsons',
               'migraine',  'fatigue', 'ibs', 'gout']  # 'fibromyalgia',


# Add a column with the name of the disorder in each dataframe
for df, name in zip(other_dfs, other_names):
    df['disorder'] = name

# Add a column with the name of the disorder in each dataframe
for df, name in zip(psych_dfs, psych_names):
    df['disorder'] = name

all_dfs = psych_dfs + other_dfs

# make new dataframe combining all SNPs and disorders

concat_df = pd.concat(all_dfs, ignore_index=True)

pivot_all = pd.pivot_table(concat_df, values='p_value', index='rs_id', columns='disorder')
pivot_all = pivot_all.fillna(0) #can the p-value be set to 0?
pivot_all = pivot_all.reset_index()

pivot_all.to_csv('all_pivoted.csv')