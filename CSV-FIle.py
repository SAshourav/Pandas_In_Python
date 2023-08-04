import pandas as pd

dis = {"A":[1,2,3,4,5], "B":[6,7,8,9,0]}
d = pd.DataFrame(dis)
print(d)
# Write in CSV file

d.to_csv("Test_New_Header_Change.csv",index=False,header=["First","Second"])

