import pandas as pd

# Insert

var = pd.DataFrame({"A":[1,2,3,4,5], "B":[9,8,7,6,5]})
print(var)

var.insert(2,"New Col",var["A"]) # index number , position and name of column, actual data to import

print(var)
print('\n')
var.insert(1,"Extra Col",[11,12,13,14,15]) # data should be same size

print(var)

var['Short'] = var['A'][:3]
print(var)

# Delete

var.pop("B")
print(var)

del var['A']
print(var)