from tkinter import*
root = Tk()
root.geometry("500x500")
root.title("My App")
root.config(bg="#ff0000")


def printhi(*args):
    print("Hi!")

btn = Button(root, text="Click to print hi", command=printhi)
btn.place(x=200, y=200)

root.mainloop()