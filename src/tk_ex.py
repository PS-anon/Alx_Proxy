from tkinter import *
from alx_tk import * 

window = Tk()

window.title("Welcome to LikeGeeks app")

window.geometry('1920x1080')

txt = Entry(window,width=10)

txt.grid(column=0, row=0)

lbl = Label(window, text="Response")

lbl.grid(column=0, row=1)



hd = Label(window, text="Headers")

hd.grid(column=0, row=2)

bngg = Label(window, text="Body")
bngg.grid(column=0, row =4)

header_ = Text(window)
header_.grid(column=0, row=3, columnspan=3)

banner =Text(window)
banner.grid(column=0, row= 5, columnspan=4)
def clicked():

   # res = "Welcome to " + txt.get()
    resp = get_req(txt.get())
    lbl.configure(text= resp)
   # lbl.configure(text= res)
def header():
    headers = headerss(txt.get())
    rss = "\n".join(headers)
    header_.delete("1.0", "end")
    header_.insert("end", rss)
def banner_grb():
	bgr = gb(txt.get())
	#rs = "\n".join(bgr)
	banner.insert("end", bgr)
btn = Button(window, text="Start", command=clicked)

btn.grid(column=2, row=1)
hdbutton = Button(window, text="Start", command= header)
hdbutton.grid(column=2, row=2)
bbutton = Button(window, text="Start", command=banner_grb)
bbutton.grid(column=2, row=4)
window.mainloop()