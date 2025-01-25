import time
import pandas as pd
names = pd.read_csv('C:/VSCodeProjects/PythonProjects/WritingEficient/Popular_Baby_Names.csv')
# print(names[names['Gender'] == 'MALE'])

# low speed
start_time = time.time()
names['Gender'].loc[names.Gender == 'MALE'] = 'BOY'
print(time.time() - start_time)
print(names[names['Gender'] == 'BOY'].head())

# high speed
start_time = time.time()
names['Gender'].replace(r'\bF\w*', 'GIRL', inplace=True, regex=True)
print(time.time() - start_time)
print(names[names['Gender'] == 'GIRL'].head())