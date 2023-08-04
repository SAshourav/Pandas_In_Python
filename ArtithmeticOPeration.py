import pandas as pd

var = pd.DataFrame({'A': [1, 2, 3, 4], "B": [5, 6, 7, 8]})
print(var)

var["Addition"] = var["A"]+var["B"]

var["Subtraction"] = var["A"]-var["B"]

var["Division"] = var["A"]/var["B"]
var["Multiplication"] = var["A"]*var["B"]
print(var)
print('\n')

var2 = pd.DataFrame({'A': [10, 20, 30, 40], "B": [50, 60, 70, 80]})
var2["Check_A"] = var2['A'] >= 20
var2["Check_B"] = var2['B'] >= 70
print(var2)