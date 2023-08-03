import pandas as pd

# DataFrame

l = [1,2,3,4,5,6]
d ={"name":['sabbir','ibnul'],'roll':[1,2],'Test':["human?", "Dog?"]} # dic length must be same
var = pd.DataFrame(l)
print(var)
print(type(var))
DicV = pd.DataFrame(d)
print(DicV) # this gives the key as header col also gives the serial number

print('\n')
DicVBaseOnCol = pd.DataFrame(d, columns=['name','Test'], index=['Index-1','Index-2']) # only name column will be available
print(DicVBaseOnCol)

print('\n')
print("Accesing the value of roll column , 1 row value")
print(DicV["roll"][1])


sr = {'s':pd.Series([1,2,3,4]),'r':pd.Series([5,6,7,8])}
SerisInDataFrame = pd.DataFrame(sr)
print(SerisInDataFrame)