import numpy as np

list = np.random.randint(1,100,np.random.randint(10,30))

for i in range(len(list)):
    for j in range(len(list)-1):
        if list[j] > list[j+1]:
            temp = list[j]
            list[j] = list[j+1]
            list[j+1] = temp
    print(str(i+1)+': ',list)