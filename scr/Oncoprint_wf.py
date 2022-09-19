import pandas as pd
import sys

Input = sys.argv[1]
Output = sys.argv[2]

df = pd.read_csv(Input)
df = df.drop(['End',  'Cyt_Met', 'Cyt_NoMet'], axis=1)

count = df['Sample'].value_counts()

Onco = df.pivot(index=['Chr', 'Start'], columns = ['Sample', 'Status'])

count.to_csv(Output+'/Count.csv')
Onco.to_csv(Output+'/Oncoprint_wf.csv')
