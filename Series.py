import pandas as pd

x = [3,5,7,9,2]

var = pd.Series(x)
print(var)
print(type(var))

var = pd.Series(x, index=['a','s','d','e','r'],name="Test") # changing the index
print(var)
print(type(var))
print(var[2])

dic = {'name':['python','c','c++','java'],'por':['12,13,14,15'],'rank':[1,4,3,2]} # mix data type thakar karoner mix asbe
convSeris = pd.Series(dic)
print(convSeris)

s = pd.Series(12,index=[1,2,3,4,5,6,7]) # auto value added into index
print(s)

s1 = pd.Series(12,index=[1,2,3,4,5,6,7])
s2 = pd.Series(12,index=[1,2,3,4])

print(s1+s2) # s2 te je index gula nai sekhane NaN dekhacche , kintu jodi eta numpy te erokom korle error dito