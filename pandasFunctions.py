import pandas as pd
import numpy as np

csv_1 = pd.read_csv("username-password-recovery-code.csv")
print(csv_1.index)
print('\n')
print(csv_1.columns)
print('\n')
print(csv_1.describe())
print('\n')
print(csv_1.head(2))
print('\n')
print(csv_1.tail(2))
print('\n')
print(csv_1[2:4])
print('\n')
print(csv_1.index.array)
print('\n')
print(csv_1.to_numpy())
v = np.asarray(csv_1)
print('\n')
print(v)

print(csv_1.sort_index(axis=0 ,ascending=False)) # axis=0 means row 1 means column

csv_1["Username"]