import pandas as pd

build37 = pd.read_csv('build37.vcf',comment='#', sep='t')
build38 = pd.read_csv('build38.vcf', comment='#', sep='\t')

endometriosis = pd.read_csv('endometriosis.txt', sep='\t')
diabetes1 = pd.read_csv('diabetes1.txt', sep='\t')
fibromyalgia = pd.read_csv('fibromyalgia.txt', sep='\t')
gdm = pd.read_csv('gdm.txt', sep='\t')
pcos = pd.read_csv('pcos.txt', sep='\t')
preeclampsia = pd.read_csv('preeclampsia.txt', sep='\t')
preterm_birth = pd.read_csv('preterm_birth.txt', sep='\t')
fatigue = pd.read_csv('fatigue.txt', sep='\t')

#endometriosis=endometriosis.rename(columns={'chromosome':'chr','base_pair_location':'pos'})
endometriosis_updated = pd.merge(endometriosis, build38, on=['chr', 'pos'], how='inner')
endometriosis_updated.to_csv('endometriosis_updates.txt', sep='\t')

#diabetes1=diabetes1.rename(columns={'chromosome':'chr','base_pair_location':'pos'})
diabetes1_updated = pd.merge(diabetes1, build38, on=['chr', 'pos'], how='inner')
diabetes1_updated.to_csv('diabetes_updated.txt', sep='\t')

#fibromyalgia=fibromyalgia.rename(columns={'chromosome':'chr','base_pair_location':'pos'})
fibromyalgia_updated = pd.merge(fibromyalgia, build38, on=['chr', 'pos'], how='inner')
fibromyalgia_updated.to_csv('fibromyalgia_updated.txt', sep='\t')

#gdm=gdm.rename(columns={'chromosome':'chr','base_pair_location':'pos'})
gdm_updated = pd.merge(gdm, build38, on=['chr', 'pos'], how='inner')
gdm_updated.to_csv('gdm_updated.txt', sep='\t')

pcos_updated = pd.merge(pcos, build37, on=['chr', 'pos'], how='inner')
pcos_updated.to_csv('pcos_updated.txt', sep='\t')

#preeclampsia=preeclampsia.rename(columns={'chromosome':'chr','base_pair_location':'pos'})
preeclampsia_updated = pd.merge(preeclampsia, build38, on=['chr', 'pos'], how='inner')
preeclampsia_updated.to_csv('preeclampsia_updated.txt', sep='\t')

#preterm_birth=preterm_birth.rename(columns={'chromosome':'chr','base_pair_location':'pos'})
preterm_birth_updated = pd.merge(preterm_birth, build38, on=['chr', 'pos'], how='inner')
preterm_birth_updated.to_csv('preterm_birth_updated.txt', sep='\t')

#fatigue=preterm_birth.rename(columns={'chromosome':'chr','base_pair_location':'pos'})
fatigue_updated = pd.merge(fatigue, build38, on=['chr', 'pos'], how='inner')
fatigue_updated.to_csv('fatigue_updated.txt', sep='\t')

