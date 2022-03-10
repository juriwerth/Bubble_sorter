from tkinter import *
import numpy as np

j = 0

root = Tk() 
root.title('Visual bubble sorter') 
root.geometry("500x500") 
root.config(bg='#DCDCDC')

def unsort():
    global list
    for element in root.winfo_children():
                    element.destroy()
    l = 0
    list = np.random.randint(1,35,50)
    print(list)
    for i in range(len(list)):
        Label(root, height=list[i],width=1, bg='black').place(x=l)
        l = l + 10
    Button(root, text="Start sorting",font=("Calibri",14), command=sort,height=1,width=10,).place(x=10,y=450)

def sort():
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

unsort()
root.mainloop()