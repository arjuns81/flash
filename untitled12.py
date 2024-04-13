from tkinter import*
root=Tk()

root.title("multidimensional arrays.")
root.geometry("500x500")
label=Label(root)

array_1d=["John","Nate","Troy"]
print(array_1d[0])

array_2d=[["John","A+"],["Nate","B-"],["Troy","D-"]]
print(array_2d[0][1])

array_3d=[[["John","A+","excellent"],["Nate","B-","good"],["Troy","D-","bad"]]]
print(array_3d[0][0][2])

def report():
    label["text"]=array_3d[0][1][0]+"got grade"+array_3d[0][1][0]+"and he is doing"+array_3d[0][1][2]
   
    btn=Button(root,text="show report",command=report)
    btn.place(relx=0.5,rely=0.5,anchor=center)
    
    label.place(relx=0.5,rely=0.6,anchor=center)
    
    root.mainloop()
