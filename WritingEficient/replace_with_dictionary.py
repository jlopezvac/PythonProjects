import time
import pandas as pd
names = pd.read_csv('C:/VSCodeProjects/PythonProjects/WritingEficient/Popular_Baby_Names.csv')
print(names.head())

# high speed
start_time = time.time()
names['Gender'].replace({'MALE' : 'BOY', 'FEMALE' : 'GIRL'}, inplace=True)
print(names.head(25))