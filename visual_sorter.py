from tkinter import *
import numpy as np

j = 0

root = Tk() 
root.title('Visual bubble sorter') 
root.geometry("500x500") 
root.config(bg='#DCDCDC')

def unsort():
    global list
    global steps
    for element in root.winfo_children():
                    element.destroy()
    l = 0
    list = np.random.randint(1,35,50)
    steps = len(list)-1
    print(list)
    for i in range(len(list)):
        Label(root, height=list[i],width=1, bg='black').place(x=l)
        l = l + 10
    Button(root, text="Bubble sort",font=("Calibri",14), command=Bubble,height=1,width=10,).place(x=10,y=450)
    Button(root, text="Shaker sort",font=("Calibri",14), command=Shaker,height=1,width=10,).place(x=125,y=450)

def Bubble():
    for i in range(len(list)):
        for j in range(len(list)-1):
            if list[j] > list[j+1]:
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp
                for element in root.winfo_children():
                    element.destroy()
                j = 0
                for i in range(len(list)):
                    Label(root, height=list[i],width=1, bg='black').place(x=j)
                    j = j + 10
                root.update()
    Button(root, text="Unsort",font=("Calibri",14), command=unsort,height=1,width=10,).place(x=10,y=450)

def Shaker():
    for i in range(len(list)):
        for j in range(steps):
            if list[j] > list[j+1]:
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp
                for element in root.winfo_children():
                    element.destroy()
                j = 0
                for i in range(len(list)):
                    Label(root, height=list[i],width=1, bg='black').place(x=j)
                    j = j + 10
                root.update()
        for l in range(steps-1,len(list)-steps,-1):
            if list[l] < list[l-1]:
                temp = list[l]
                list[l] = list[l-1]
                list[l-1] = temp
                for element in root.winfo_children():
                    element.destroy()
                j = 0
                for i in range(len(list)):
                    Label(root, height=list[i],width=1, bg='black').place(x=j)
                    j = j + 10
                root.update()
    Button(root, text="Unsort",font=("Calibri",14), command=unsort,height=1,width=10,).place(x=10,y=450)

unsort()
root.mainloop()