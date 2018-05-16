import pandas as pd
from collections import OrderedDict
from datetime import date

students = pd.read_csv('train.csv')        
df = pd.DataFrame(students, columns=['NU_INSCRICAO', 'NU_NOTA_CN', 'NU_NOTA_CH', 'NU_NOTA_LC', 'NU_NOTA_MT', 'NU_NOTA_REDACAO'])
df.to_csv('only_notes.csv')

#only_notes = pd.read_csv('only_notes.csv')        

#print(df)

# NU_INSCRICAO NU_NOTA_CN	NU_NOTA_CH	NU_NOTA_LC	NU_NOTA_MT NU_NOTA_REDACAO NOTA_FINAL 