# %%
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("C:/Users/jlope/Downloads/temperatures.csv")
df.info()
# df.loc[df['avg_temp_c'].isnull(), 'avg_temp_c'] = 99.99
# print(df['avg_temp_c'].max())
#df = df[df['avg_temp_c'].isnull() == False]

# df = df.dropna()
print(df.isna().sum())

print(df[df['city'] == 'Berlin'])
plt.scatter(x = 'date', y = 'avg_temp_c', data=df[df['city'] == 'Berlin'])
plt.show()

print(df[['city','country']])


# %%
print(df[df.duplicated()])


# %%
import pandas as pd
the_data = pd.read_csv("C:/Users/jlope/Downloads/temperatures.csv")
countries = set(the_data['country'])
iberia = {'Spain','Portugal'}
print(iberia)
print(countries)
not_in_iberia = set(the_data['country']).difference(iberia)
print(not_in_iberia)
print(the_data.info())



# %%
import pandas as pd
import numpy as np
the_data = pd.read_csv("C:/Users/jlope/Downloads/temperatures.csv")
print(the_data['avg_temp_c'].describe())
the_data['new_data'] = pd.qcut(the_data['avg_temp_c'], q = 3, labels=['cat1','cat2','cat3'])
print(the_data.head(500))
print(the_data.groupby('new_data').describe())

# %%
import time
import pandas as pd
names = pd.read_csv('C:/VSCodeProjects/PythonProjects/WritingEficient/Popular_Baby_Names.csv')
# print(names[names['Gender'] == 'MALE'])

# low speed
start_time = time.time()
names['Gender'].loc[names['Gender'] == 'MALE'] = 'BOY'
print(time.time() - start_time)
print(names[names['Gender'] == 'BOY'].head())

# high speed
start_time = time.time()
names['Gender'].replace(r'\bF\w*', 'GIRL', inplace=True, regex=True)
print(time.time() - start_time)
print(names[names['Gender'] == 'GIRL'].head())


