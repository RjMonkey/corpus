import os

list = os.listdir("./annotation/")
for item in list:
    name = item.split('_')[1]
    print(name)
pass

