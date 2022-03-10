import numpy as np

list = np.random.randint(1,100,np.random.randint(10,30))
print('List: '+str(list))
steps = len(list)-1

for i in range(len(list)):
    for j in range(steps):
        if list[j] > list[j+1]:
            temp = list[j]
            list[j] = list[j+1]
            list[j+1] = temp
    for l in range(steps-1,len(list)-steps,-1):
        if list[l] < list[l-1]:
            temp = list[l]
            list[l] = list[l-1]
            list[l-1] = temp

    print(str(i+1)+': ',list)