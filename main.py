import os
import pandas as pd
from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
from tkinter import messagebox

doggofiles = Tk()
doggofiles.title("doggofiles")
doggofiles.iconbitmap(r"C:\Users\Verkesfl\Documents\Documenten\ICON\icon.ico")
doggofiles.configure(bg="#fed2ed")
doggofiles.geometry("900x550")

doggo = ImageTk.PhotoImage(Image.open(r"C:\Users\Verkesfl\Documents\Documenten\PERSONAL\doggos.jpg"))
doggo2 = ImageTk.PhotoImage(Image.open(r"C:\Users\Verkesfl\Documents\Documenten\PERSONAL\doggofroggo.jpg"))
doggo_pic = Label(image=doggo)
doggo_pic2 = Label(image=doggo2)
doggo_pic.grid(column=0, row=0, columnspan=4)
doggo_pic2.grid(column=0, row=9, columnspan=4)


def openpad():
    pad = filedialog.askdirectory(title="get dem files doggo!")
    toon_padnaam = Label(doggofiles, text="You chose this path: " + pad, bg="#fed2ed")
    toon_padnaam.grid(column=0, row=2, columnspan=4)
    return pad


path = Button(doggofiles, text="Choose a Directory!", padx=100, pady=10, bg="#fe37af", borderwidth=10, command=openpad)
path.grid(column=0, row=1, columnspan=4)

padnaam = openpad()


var1 = StringVar()
var2 = StringVar()
var3 = StringVar()
var4 = StringVar()
var5 = StringVar()
var6 = StringVar()
var7 = StringVar()

checktif = Checkbutton(doggofiles, text=".tif", bg="#fed2ed", onvalue=".tif", offvalue="", variable=var1)
checkjpg = Checkbutton(doggofiles, text=".jpg", bg="#fed2ed", onvalue=".jpg", offvalue="", variable=var2)
checkwav = Checkbutton(doggofiles, text=".wav", bg="#fed2ed", onvalue=".wav", offvalue="", variable=var3)
checkmov = Checkbutton(doggofiles, text=".mov", bg="#fed2ed", onvalue=".mov", offvalue="", variable=var4)
checkmp3 = Checkbutton(doggofiles, text=".mp3", bg="#fed2ed", onvalue=".mp3", offvalue="", variable=var5)
checkmp4 = Checkbutton(doggofiles, text=".mp4", bg="#fed2ed", onvalue=".mp4", offvalue="", variable=var6)
checktiff = Checkbutton(doggofiles, text=".tiff", bg="#fed2ed", onvalue=".tiff", offvalue="", variable=var7)

checktif.grid(row=3, column=0)
checkjpg.grid(row=3, column=1)
checkwav.grid(row=3, column=2)
checkmov.grid(row=3, column=3)
checkmp3.grid(row=4, column=0)
checkmp4.grid(row=4, column=1)
checktiff.grid(row=4, column=2)


def start():
    column = ["filename", 'path', "filesize"]
    lijst = []
    totalsize = 0

    filetypes = [var1.get(), var2.get(), var3.get(), var4.get(), var5.get(), var6.get(), var7.get()]
    while "" in filetypes:
        filetypes.remove("")
    messagebox.showinfo("You chose filetype(s): ", filetypes)

    for x, y, z in os.walk(padnaam):
        for a in z:
            if a.endswith(tuple(filetypes)):
                b = os.path.join(x, a)
                c = os.path.getsize(b)
                d = round(c / (1024 * 1024), 3)
                totalsize += d
                e = str(a) + '%£~' + str(b) + '%£~' + str(d)
                f = e.split('%£~')
                lijst.append(f)
    df = pd.DataFrame(lijst, columns=column)
    df.to_excel("output.xlsx")
    size = Label(doggofiles, text="The total size is: " + str(round(totalsize/1024, 2)) + " GB", bg="#fed2ed")
    size.grid(row=7, column=0, columnspan=4)

    if len(lijst) > 0:
        averagesize = totalsize/len(lijst)
        average = Label(doggofiles, text="The average size is: " + str(round(averagesize, 2)) + " MB", bg="#fed2ed")
        average.grid(row=8, column=0, columnspan=4)
    else:
        average = Label(doggofiles, text='The average size is: 0.0 MB', bg="#fed2ed")
        average.grid(row=8, column=0, columnspan=4)


buttonstart = Button(doggofiles, text="Start!", padx=50, pady=10, borderwidth=10, bg="#fe37af", command=start)
buttonstart.grid(row=6, column=0, columnspan=4)

doggofiles.mainloop()
