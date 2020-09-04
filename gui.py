from tkinter import *

def main():
    w1=Tk()
    w1.title("Price Comparison")
    # Width, height in pixels
    f1=Frame(w1, height=400, width=500)
    f1.pack()

    description = Text(f1, width=70, height=5)
    description.insert(INSERT, "Welcome to Price Comparison Program!"+"\n"+"This Program will automatically search a lowest price of an item that you want to buy."+"\n"+"This program will search at Amazon, Bestbuy, Target, etc. First, type any item that you want to get, then press it!")
    description.pack(side="top")

    entry = Entry(f1, fg="black", bg="white", width=95)
    #Need to have a safecase where if entry is empty, then don't run program
    entry.pack()

    resultStr = ""

    result = Text(f1, width=70, height=5)

    def onPress():
        result.insert(INSERT, entry.get())
        result.pack() 

    b = Button(f1, text='Search', command=onPress)
    b.pack()
    
    w1.mainloop()

main()

