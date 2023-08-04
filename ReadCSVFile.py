import pandas as pd

csv_1 = pd.read_csv("username-password-recovery-code.csv")
print(csv_1)
print('\n')
csv_2 = pd.read_csv("username-password-recovery-code.csv", nrows=1)
print(csv_2)
print(type(csv_2))

# csv_3 = pd.read_csv("username-password-recovery-code.csv", usecols=[0, 3]) # column is not finding
# print(csv_3)

csv_3 = pd.read_csv("username-password-recovery-code.csv", skiprows=[0]) # header or 0 number row skip kore jay
print(csv_3)

print('\n')
csv_4 = pd.read_csv("username-password-recovery-code.csv", header= 2)
print(csv_4)

print('\n')
csv_5 = pd.read_csv("username-password-recovery-code.csv", header=None) # call assign wrong
print(csv_5)