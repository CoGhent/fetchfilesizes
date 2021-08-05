import os
import pandas as pd
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox


def open_directory():
    file_path = filedialog.askdirectory(title="Select directory!")
    show_pathname = Label(fetchfilesize, text="You chose this path: " + file_path, bg="#fed2ed")
    show_pathname.grid(column=0, row=8, columnspan=4)
    return file_path


def open_file():
    file = filedialog.askopenfile(title="Select file!")
    return file


def save_file():
    file_location = filedialog.askdirectory(title="Save File!")
    show_location = Label(fetchfilesize, text="Your file can be found here: " + file_location, bg="#fed2ed")
    show_location.grid(column=0, row=9, columnspan=4)
    return file_location


def start():
    column = ["filename", 'path', "filesize (MB)"]
    list = []
    totalsize = 0
    filetypes = [var1.get(), var2.get(), var3.get(), var4.get(), var5.get(), var6.get(), var7.get(), var8.get()]
    while "" in filetypes:
        filetypes.remove("")
    messagebox.showinfo("You chose filetype(s): ", filetypes)

    for x, y, z in os.walk(open_directory()):
        for a in z:
            if a.endswith(tuple(filetypes)):
                b = os.path.join(x, a)
                c = os.path.getsize(b)
                d = round(c / (1024 * 1024), 3)
                totalsize += d
                e = str(a) + '%£~' + str(b) + '%£~' + str(d)
                f = e.split('%£~')
                list.append(f)
    df = pd.DataFrame(list, columns=column)
    messagebox.showinfo("Choose location", "Please choose a location to store the result")
    df.to_excel(save_file() + "\output.xlsx")
    size = Label(fetchfilesize, text="The total size is: " + str(round(totalsize / 1024, 2)) + " GB", bg="#fed2ed")
    size.grid(row=10, column=0, columnspan=4)

    if len(list) > 0:
        averagesize = totalsize / len(list)
        average = Label(fetchfilesize, text="The average size is: " + str(round(averagesize, 2)) + " MB", bg="#fed2ed")
        average.grid(row=11, column=0, columnspan=4)
    else:
        average = Label(fetchfilesize, text='The average size is: 0.0 MB', bg="#fed2ed")
        average.grid(row=11, column=0, columnspan=4)


fetchfilesize = Tk()
fetchfilesize.title("fetch filesize")
fetchfilesize.configure(bg="#fed2ed")
fetchfilesize.geometry("900x550")

info = Label(fetchfilesize, text="Choose filetypes: ", bg="#ffffff")
info.grid(column=0, row=1, columnspan=4)

var1 = StringVar()
var2 = StringVar()
var3 = StringVar()
var4 = StringVar()
var5 = StringVar()
var6 = StringVar()
var7 = StringVar()
var8 = StringVar()

checktif = Checkbutton(fetchfilesize, text=".tif", bg="#fed2ed", onvalue=".tif", offvalue="", variable=var1)
checkjpg = Checkbutton(fetchfilesize, text=".jpg", bg="#fed2ed", onvalue=".jpg", offvalue="", variable=var2)
checkwav = Checkbutton(fetchfilesize, text=".wav", bg="#fed2ed", onvalue=".wav", offvalue="", variable=var3)
checkmov = Checkbutton(fetchfilesize, text=".mov", bg="#fed2ed", onvalue=".mov", offvalue="", variable=var4)
checkmp3 = Checkbutton(fetchfilesize, text=".mp3", bg="#fed2ed", onvalue=".mp3", offvalue="", variable=var5)
checkmp4 = Checkbutton(fetchfilesize, text=".mp4", bg="#fed2ed", onvalue=".mp4", offvalue="", variable=var6)
checktiff = Checkbutton(fetchfilesize, text=".tiff", bg="#fed2ed", onvalue=".tiff", offvalue="", variable=var7)
checkJPG = Checkbutton(fetchfilesize, text=".JPG", bg="#fed2ed", onvalue=".JPG", offvalue="", variable=var8)

checktif.grid(row=4, column=0)
checkjpg.grid(row=4, column=1)
checkwav.grid(row=4, column=2)
checkmov.grid(row=4, column=3)
checkmp3.grid(row=5, column=0)
checkmp4.grid(row=5, column=1)
checktiff.grid(row=5, column=2)
checkJPG.grid(row=5, column=3)

buttonstart = Button(fetchfilesize, text="Choose a Directory!", padx=50, pady=10, borderwidth=10, bg="#ffffff",
                     command=start)
buttonstart.grid(row=7, column=0, columnspan=4)


fetchfilesize.mainloop()
