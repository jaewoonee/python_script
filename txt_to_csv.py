import re
import csv
import pandas as pd

#csv.register_dialect('skip_space', skipinitialspace=True)
f = open('input.txt', 'r', encoding='utf16')
#txt_file = pd.read_csv('input.txt', delim_whitespace=True, encoding='utf-16')
#reader = csv.reader(f, delimiter=' ', dialect='skip_space')
reader = csv.reader(f)
csv_list=[]
for l in reader:
    csv_list.append(l)
f.close()

df = pd.DataFrame(csv_list)

#df.to_csv('output.csv', index=False, header=False)