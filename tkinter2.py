from tkinter import*
def show_entry_fields():
    print('First Name: %s\nLast Name: %s' % (e1.get(), e2.get()))
window= Tk()
Label(window, text= 'First Name').grid(row=0)
Label(window, text= 'Last Name').grid(row=1)
e1=Entry(window)
e2=Entry(window)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
Button(window, text='Quit', command=window.quit).grid(row=3, column=0, sticky=W, pady=4)
Button(window, text= 'Show', command=show_entry_fields).grid(row=3, column=1,sticky=W,pady=4)


mainloop()