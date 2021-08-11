import os
import pandas as pd
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox


def open_path():
    path = filedialog.askdirectory(title="Select directory!")
    show_path = Label(fetchfilesize, text="You chose this path: " + path, bg="#e4e5e5")
    show_path.grid(column=0, row=11, columnspan=4)
    blank = Label(fetchfilesize, text="", bg="#e4e5e5")
    blank.grid(column=0, row=10, columnspan=4)
    return path


def openfile():
    file = filedialog.askopenfile(title="Select file!")
    return file


def save_file():
    location = filedialog.askdirectory(title="Save File!")
    show_location = Label(fetchfilesize, text="Your file (output.xlsx) can be found here: " + location, bg="#e4e5e5")
    show_location.grid(column=0, row=12, columnspan=4)
    return location


def choose():
    choice = [variable.get(), variable2.get()]
    if tuple(choice) == ('','directory'):
        def start():
            column = ["filename", 'path', "filesize (MB)"]
            _list = []
            totalsize = 0
            filetypes = [var1.get(), var2.get(), var3.get(), var4.get(), var5.get(), var6.get(), var7.get(), var8.get(),
                         var9.get()]
            while "" in filetypes:
                filetypes.remove("")
            messagebox.showinfo("You chose filetype(s): ", filetypes)

            for x, y, z in os.walk(open_path()):

                for a in z:
                    if a.endswith(tuple(filetypes)):
                        b = os.path.join(x, a)
                        c = os.path.getsize(b)
                        d = round(c / (1024 * 1024), 3)
                        totalsize += d
                        e = str(a) + '%£~' + str(b) + '%£~' + str(d)
                        f = e.split('%£~')

                        _list.append(f)
            df = pd.DataFrame(_list, columns=column)
            messagebox.showinfo("Choose location", "Please choose a location to store the result")

            # Windows OS
            df.to_excel(str(save_file()) + "\output.xlsx")

            # linux - MAC OS
            df.to_excel(str(save_file()) + "/output.xlsx")

            size = Label(fetchfilesize, text="The total size is: " + str(round(totalsize / 1024, 2)) + " GB",
                         bg="#e4e5e5")
            size.grid(row=14, column=0, columnspan=4)

            if len(_list) > 0:
                averagesize = totalsize / len(_list)
                average = Label(fetchfilesize, text="The average size is: " + str(round(averagesize, 2)) + " MB",
                                bg="#e4e5e5")
                average.grid(row=15, column=0, columnspan=4)
            else:
                average = Label(fetchfilesize, text='The average size is: 0.0 MB', bg="#e4e5e5")
                average.grid(row=15, column=0, columnspan=4)

        var1 = StringVar()
        var2 = StringVar()
        var3 = StringVar()
        var4 = StringVar()
        var5 = StringVar()
        var6 = StringVar()
        var7 = StringVar()
        var8 = StringVar()
        var9 = StringVar()

        checktif = Checkbutton(fetchfilesize, text=".tif", bg="#e4e5e5", onvalue=".tif", offvalue="", variable=var1)
        checkjpg = Checkbutton(fetchfilesize, text=".jpg", bg="#e4e5e5", onvalue=".jpg", offvalue="", variable=var2)
        checkwav = Checkbutton(fetchfilesize, text=".wav", bg="#e4e5e5", onvalue=".wav", offvalue="", variable=var3)
        checkmov = Checkbutton(fetchfilesize, text=".mov", bg="#e4e5e5", onvalue=".mov", offvalue="", variable=var4)
        checkmp3 = Checkbutton(fetchfilesize, text=".mp3", bg="#e4e5e5", onvalue=".mp3", offvalue="", variable=var5)
        checkmp4 = Checkbutton(fetchfilesize, text=".mp4", bg="#e4e5e5", onvalue=".mp4", offvalue="", variable=var6)
        checktiff = Checkbutton(fetchfilesize, text=".tiff", bg="#e4e5e5", onvalue=".tiff", offvalue="", variable=var7)
        checkJPG = Checkbutton(fetchfilesize, text=".JPG", bg="#e4e5e5", onvalue=".JPG", offvalue="", variable=var8)
        checkTIF = Checkbutton(fetchfilesize, text=".TIF", bg="#e4e5e5", onvalue=".TIF", offvalue="", variable=var8)

        checktif.grid(row=5, column=0)
        checkjpg.grid(row=5, column=1)
        checkwav.grid(row=5, column=2)
        checkmov.grid(row=5, column=3)
        checkmp3.grid(row=6, column=0)
        checkmp4.grid(row=6, column=1)
        checktiff.grid(row=6, column=2)
        checkJPG.grid(row=6, column=3)
        checkTIF.grid(row=6, column=4)

        blank2 = Label(text="", bg="#e4e5e5")
        blank2.grid(row=4, column=1)
               
        blank3 = Label(text="", bg="#e4e5e5")
        blank3.grid(row=7, column=1)

        buttonstart = Button(fetchfilesize, text="Start", padx=50, pady=10, borderwidth=4, bg="#04a37b", command=start)
        buttonstart.grid(row=8, column=1, columnspan=2)

    else:
        def start():
            column = ["filename", 'path', "filesize (MB)"]
            lijst = []

            for x, y, z in os.walk(open_path()):

                for a in z:
                    b = os.path.join(x, a)
                    c = os.path.getsize(b)
                    d = round(c / (1024 * 1024), 3)
                    e = str(a) + '%£~' + str(b) + '%£~' + str(d)
                    f = e.split('%£~')
                    lijst.append(f)
            df = pd.DataFrame(lijst, columns=column)
            messagebox.showinfo("Choose file", "Please open file with filenames (one column with header 'filename')")
            filenames = pd.read_csv(open_file())
            result = pd.merge(filenames, df, left_on='filename', right_on="filename", how='left')
            messagebox.showinfo("Choose location", "Please choose a location to store the result")
            result.to_excel(save_file() + r"\result.xlsx")
            
        
        blank4 = Label(text="", bg="#e4e5e5")
        blank4.grid(row=4, column=1)
        
        _info = Label(text="Press Start", bg="#e4e5e5")
        _info.grid(row=5, column=1)
        
        blank5 = Label(text="", bg="#e4e5e5")
        blank5.grid(row=6, column=1)

        buttonstart = Button(fetchfilesize, text="Start", padx=50, pady=10, borderwidth=4, bg="#04a37b", command=start)
        buttonstart.grid(row=7, column=1, columnspan=4)


fetchfilesize = Tk()
fetchfilesize.title("fetch filesize")
fetchfilesize.configure(bg="#e4e5e5")
fetchfilesize.geometry("900x550")

Info = Label(text="Please choose filesource and press start")
Info.grid(row=0, column=1)

blank6 = Label(text="", bg="#e4e5e5")
blank6.grid(row=2, column=1)

variable = StringVar()
variable2 = StringVar()

Filesource1 = Checkbutton(fetchfilesize, text="csv", variable=variable, onvalue="csv", offvalue="", bg="#e4e5e5")
Filesource2 = Checkbutton(fetchfilesize, text="directory", variable=variable2, onvalue="directory", offvalue="", bg="#e4e5e5")


Filesource1.grid(row=1, column=1)
Filesource2.grid(row=1, column=2)

buttonchoose = Button(fetchfilesize, text="Start", padx=50, pady=10, borderwidth=4, bg="#04a37b", command=choose)
buttonchoose.grid(row=3, column=1, columnspan=2)

fetchfilesize.mainloop()
