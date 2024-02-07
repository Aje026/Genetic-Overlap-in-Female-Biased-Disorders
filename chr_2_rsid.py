from easy_entrez import EntrezAPI
import pandas as pd
entrez_api = EntrezAPI('your-tool-name','your.email@gmail.com')

df = pd.read_csv('fibromyalgia_buildGRCh37.tsv', sep='\t')

df = df[['chromosome', 'base_pair_location']]

rsID = []
for i in range(len(df)):
    results = entrez_api.search(
        dict(chromosome=df['chromosome'][i], organism='human', position_grch37=df['base_pair_location'][i]),
        database='snp',
        max_results=10
    )
    # rsID.append('rs'+results.data['esearchresult']['idlist'][-1])
    # Check if any results were found
    idlist = results.data['esearchresult']['idlist']
    if idlist:
        rsID.append('rs' + idlist[-1])
    else:
        rsID.append(None)


df['rs_id'] = rsID

df.to_csv('fibromyalgia_rsid.txt', sep='\t', index=False)