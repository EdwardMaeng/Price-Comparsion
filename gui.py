from tkinter import *
from PIL import Image, ImageTk

def main():
    w1=Tk()
    w1.geometry("600x200")
    w1.title("Price Comparison")
    # Width, height in pixels
    f1=Frame(w1, height=400, width=500)
    f1.pack()

    description = Text(f1, width=70, height=5)
    description.insert(INSERT, "Welcome to Price Comparison Program!"+"\n"+"This Program will automatically search a lowest price of an item that you want to buy."+"\n"+"This program will search at Amazon, Bestbuy, Target, etc. First, type any item that you want to get, then press it!")
    description.pack(side="top")

    entry = Entry(f1, bg="white", width=95)
    #Need to have a safecase where if entry is empty, then don't run program
    entry.pack()

    resultStr = ""

    result = Text(f1, width=70, height=5)

    def onPress():
        # Toplevel object which will  
        # be treated as a new window 
        newWindow = Toplevel(w1) 
        # sets the title of the 
        # Toplevel widget 
        newWindow.title("Result") 
        # sets the geometry of toplevel 
        newWindow.geometry("700x500") 
        # A Label widget to show in toplevel 
        listObject = Frame(newWindow, width=150, height=100)
        listObject.pack()
        # Company Image
        companyImage = PhotoImage(file="amazon.png")
        ImageLabel = Label(listObject, image=companyImage)
        ImageLabel.photo = companyImage
        ImageLabel.pack()
        # Price
        lowestPrice = Text(listObject, width=35, height=5)
        lowestPrice.config(pady=10)
        lowestPrice.insert(INSERT, "PRICE: ")
        lowestPrice.place(relx=0.5, rely=0.5, anchor=CENTER)

    b = Button(f1, text='Search', command=onPress)
    b.pack()
    
    w1.mainloop()

main()

