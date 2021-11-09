import pandas as pd

mydataset = {
    'sites': ["Google", "Runoob", "Wiki"],
    'number': [1, 2, 3]
}

myvar = pd.DataFrame(mydataset)
print(type(myvar))
print(myvar, '\n\n')

a = [1, 2, 3]

myvar = pd.Series(a)

print(type(myvar))
