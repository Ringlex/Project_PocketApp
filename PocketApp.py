from tkinter import *
from tkinter import messagebox

def GetData(getAmount, getStuff):
    AmountData = getAmount
    StuffData = getStuff
    print('Data: ', AmountData,StuffData)

def main():
    root = Tk()

    root.title("PocketApp")
    root.attributes('-alpha',0.8)
    Title = Label(root, text="Your pocket")
    Title.grid(row=0,columnspan = 2 )
    Amount = Label(root, text="Please add amount: ").grid(row=1)
    Stuff = Label(root, text="What did You buy: ").grid(row=2)


    AmountEntry = Entry(root)
    AmountEntry.grid(row=1, column=1)

    StuffEntry = Entry(root)
    StuffEntry.grid(row=2, column=1)

    ButtonData = Button(root, text="Save", command=lambda: GetData(AmountEntry.get(),StuffEntry.get()))
    ButtonData.grid(row=3, column=1)


    root.mainloop()


if __name__ == '__main__':
    main()