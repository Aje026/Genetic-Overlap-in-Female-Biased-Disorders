import pandas as pd

other_dfs = []

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

other_names = ['sjogrens', 'epilepsy', 'lupus', 'biliary_chorrhosis', 'thyroid_disease', 'scleroderma', 'myasthenia',
               'rh_arthritis', 'ms', 'parkinsons',
               'migraine', 'fatigue', 'ibs', 'gout']  # 'fibromyalgia',

# Add a column with the name of the disorder in each dataframe
for df, name in zip(other_dfs, other_names):
    df['disorder'] = name


# make new dataframe combining all SNPs and disorders

concat_df = pd.concat(other_dfs, ignore_index=True)

pivot = pd.pivot_table(concat_df, values='p_value', index='rs_id', columns='disorder')
# pivot_psych = pivot_psych.fillna(0) #can the p-value be set to 0?
pivot_psych = pivot.reset_index()

pivot_psych.to_csv('other_pivoted.csv')