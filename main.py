import os
import pandas as pd
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox


def open_path():
    path = filedialog.askdirectory(title="Select directory!")
    show_path = Label(fetchfilesize, text="You chose this path: " + path, bg="#fed2ed")
    show_path.grid(column=0, row=8, columnspan=4)
    return path


def openfile():
    file = filedialog.askopenfile(title="Select file!")
    return file


def save_file():
    location = filedialog.askdirectory(title="Save File!")
    show_location = Label(fetchfilesize, text="Your file can be found here: " + location, bg="#fed2ed")
    show_location.grid(column=0, row=9, columnspan=4)
    return location


def choose():
    choice = [variable.get(), variable2.get()]
    if choice == "directory":
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
                         bg="#fed2ed")
            size.grid(row=10, column=0, columnspan=4)


            if len(_list) > 0:
                averagesize = totalsize / len(_list)

                average = Label(fetchfilesize, text="The average size is: " + str(round(averagesize, 2)) + " MB",
                                bg="#fed2ed")
                average.grid(row=11, column=0, columnspan=4)
            else:
                average = Label(fetchfilesize, text='The average size is: 0.0 MB', bg="#fed2ed")
                average.grid(row=11, column=0, columnspan=4)

        var1 = StringVar()
        var2 = StringVar()
        var3 = StringVar()
        var4 = StringVar()
        var5 = StringVar()
        var6 = StringVar()
        var7 = StringVar()
        var8 = StringVar()
        var9 = StringVar()

        checktif = Checkbutton(fetchfilesize, text=".tif", bg="#fed2ed", onvalue=".tif", offvalue="", variable=var1)
        checkjpg = Checkbutton(fetchfilesize, text=".jpg", bg="#fed2ed", onvalue=".jpg", offvalue="", variable=var2)
        checkwav = Checkbutton(fetchfilesize, text=".wav", bg="#fed2ed", onvalue=".wav", offvalue="", variable=var3)
        checkmov = Checkbutton(fetchfilesize, text=".mov", bg="#fed2ed", onvalue=".mov", offvalue="", variable=var4)
        checkmp3 = Checkbutton(fetchfilesize, text=".mp3", bg="#fed2ed", onvalue=".mp3", offvalue="", variable=var5)
        checkmp4 = Checkbutton(fetchfilesize, text=".mp4", bg="#fed2ed", onvalue=".mp4", offvalue="", variable=var6)
        checktiff = Checkbutton(fetchfilesize, text=".tiff", bg="#fed2ed", onvalue=".tiff", offvalue="", variable=var7)
        checkJPG = Checkbutton(fetchfilesize, text=".JPG", bg="#fed2ed", onvalue=".JPG", offvalue="", variable=var8)
        checkTIF = Checkbutton(fetchfilesize, text=".TIF", bg="#fed2ed", onvalue=".TIF", offvalue="", variable=var8)

        checktif.grid(row=4, column=0)
        checkjpg.grid(row=4, column=1)
        checkwav.grid(row=4, column=2)
        checkmov.grid(row=4, column=3)
        checkmp3.grid(row=5, column=0)
        checkmp4.grid(row=5, column=1)
        checktiff.grid(row=5, column=2)
        checkJPG.grid(row=5, column=3)
        checkTIF.grid(row=5, column=4)

        Info = Label(text="This tool ...")
        Info.grid(row=0, column=0)

        buttonstart = Button(fetchfilesize, text="Start", padx=50, pady=10, borderwidth=10, bg="#fe37af", command=start)
        buttonstart.grid(row=7, column=0, columnspan=4)

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


        buttonstart = Button(fetchfilesize, text="Start!", padx=50, pady=10, borderwidth=10, bg="#fe37af",
                             command=start)
        buttonstart.grid(row=7, column=0, columnspan=4)


fetchfilesize = Tk()
fetchfilesize.title("fetch filesize")
fetchfilesize.configure(bg="#fed2ed")
fetchfilesize.geometry("900x550")

Info = Label(text="Please choose filesource and press start")
Info.grid(row=0, column=0)

variable = StringVar()
variable2 = StringVar()

Filesource1 = Checkbutton(fetchfilesize, text="csv", variable=variable, onvalue="csv", offvalue="")
Filesource2 = Checkbutton(fetchfilesize, text="directory", variable=variable2, onvalue="directory", offvalue="")


Filesource1.grid(row=1, column=0)
Filesource2.grid(row=1, column=1)

buttonchoose = Button(fetchfilesize, text="Start", padx=50, pady=10, borderwidth=10, bg="#fe37af", command=choose)
buttonchoose.grid(row=7, column=0, columnspan=4)

fetchfilesize.mainloop()