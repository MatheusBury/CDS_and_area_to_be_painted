# -*- coding: utf-8 -*-
"""
Vidya.
Script to fill the inspection attributes after the inspection campaign
(area_to_be_painted, cds, ...)

@author: Matheus Bury
"""

import pandas as pd

# %%
df0 = pd.read_csv(r"F:\Vidya\MV30\query_final_mv30.csv", low_memory=False)
df = df0.copy()
df = df.drop_duplicates(subset=['id'], keep='first')

# %%
df = df.rename(columns={'Area to be Painted [m²]': 'area_to_be_painted'})
df = df.rename(columns={'CDS': 'cds'})
df = df.rename(columns={'Access Type': 'access_type'})

df['area_to_be_painted_date_time'] = '2024-04-30 00:00:00'
df['cds_date_time'] = '2024-04-30 00:00:00'

df = df[['guid', 'model_id', 'base_element_type_id', 'cds', 'cds_date_time',
         'area_to_be_painted', 'area_to_be_painted_date_time']]

# %% save attributes spreadsheet

# modec dictionary
# =============================================================================
# dictionary = {'1354': {'model_id': 2, 'base_element_type_id': 1451, 'contract': 'MV23', 'structure_type': 'piping'},
#               '1367': {'model_id': 3, 'base_element_type_id': 1453, 'contract': 'MV29', 'structure_type': 'nonpiping'},
#               '1368': {'model_id': 3, 'base_element_type_id': 1452, 'contract': 'MV29', 'structure_type': 'piping'},
#               '1369': {'model_id': 4, 'base_element_type_id': 1454, 'contract': 'MV24', 'structure_type': 'piping'},
#               '1370': {'model_id': 4, 'base_element_type_id': 1455, 'contract': 'MV24', 'structure_type': 'nonpiping'},
#               '1371': {'model_id': 5, 'base_element_type_id': 1456, 'contract': 'MV26', 'structure_type': 'nonpiping'},
#               '1372': {'model_id': 5, 'base_element_type_id': 1457, 'contract': 'MV26', 'structure_type': 'piping'},
#               '1373': {'model_id': 6, 'base_element_type_id': 1458, 'contract': 'MV27', 'structure_type': 'nonpiping'},
#               '1374': {'model_id': 6, 'base_element_type_id': 1459, 'contract': 'MV27', 'structure_type': 'piping'}}
#               '1379': {'model_id': 8, 'base_element_type_id': 1462, 'contract': 'MV30', 'structure_type': 'nonpiping'},
#               '1380': {'model_id': 8, 'base_element_type_id': 1463, 'contract': 'MV30', 'structure_type': 'piping'}}                
# =============================================================================


dictionary = {'1380': {'model_id': 8, 'base_element_type_id': 1463, 'contract': 'MV30', 'structure_type': 'piping'},
              '1379': {'model_id': 8, 'base_element_type_id': 1462, 'contract': 'MV30', 'structure_type': 'nonpiping'}}

for attribute_schema_code in dictionary:
    model_id = dictionary[attribute_schema_code]['model_id']
    base_element_type_id = dictionary[attribute_schema_code]['base_element_type_id']
    contract = dictionary[attribute_schema_code]['contract']
    structure_type = dictionary[attribute_schema_code]['structure_type']
    dfi = df.loc[(df['model_id'] == model_id) & (
        df['base_element_type_id'] == base_element_type_id)]
    dfi = dfi.drop(columns=['model_id', 'base_element_type_id'])
    
    new_path = r'G:\Drives compartilhados\Modec\MV30\CDS e Area to be painted'

    dfi.to_excel(f'{new_path}\\{contract}_{structure_type}_inspection_attributes.xlsx',
                 sheet_name=attribute_schema_code, index=False)
print("Finalizado")