from tkinter import *
from PIL import ImageTk, Image
import tkinter.messagebox as tmsg
import webbrowser

def speed():
    statusvar.set("Loading..")
    from speedtest import Speedtest
    st = Speedtest()
    sbar.update()
    import time
    time.sleep(1)
    sp_dwn = st.download() / 1000000
    sp_upl = st.upload() / 1000000
    dw= "%.2f" % sp_dwn
    up= "%.2f" % sp_upl
    pi = st.get_best_server()
    tmsg.showinfo("SpeedTest Result", f"Download Speed is: {dw} Mbps \n"
                                      f"Download Speed is: {up} Mbps \n"
                                      f"Ping is {int(pi['latency'])} \n"
                                      f"Location : {pi['name']},{pi['country']}")
    statusvar.set("Ready")

def getrate():
    with open("rate.txt",'a') as f:
        f.write(f"Rating is {myslider.get()}\n")
    tmsg.showinfo("Rating",f"Thank you for {myslider.get()} stars")

def callfacebook():
    webbrowser.open_new("https://www.facebook.com/shivam.tandon.718/")
def calltwitter():
    webbrowser.open_new("https://twitter.com/ShivamT95133118")
def callgithub():
    webbrowser.open_new("https://github.com/shivamtandon200500")
def calllinkedin():
    webbrowser.open("https://www.linkedin.com/in/shivam-t-896834b2")

root=Tk()
root.title("SpeedTester by Shivam Tandon")
root.geometry("700x505")
root.wm_iconbitmap("speed-test.ico")
root.config(bg="black")
root.resizable(0, 0)
#middle-pic
my_pic=Image.open("share-logo.png")
resize=my_pic.resize((495,100),Image.ANTIALIAS)
new=ImageTk.PhotoImage(resize)
img_labe=Label(root,image=new)
img_labe.grid(pady=20)
img_labe.place(x=110,y=17)
#download text
text_dwn=Label(root,text="Check Your\n"
                         "Download Speed",font="helvetica 14 bold",fg="white",bg="black")
text_dwn.grid(pady=20)
text_dwn.place(x=200,y=210, anchor="center")
#upload text
text_upl=Label(root,text="Check Your\n"
                         "Upload Speed",font="helvetica 14 bold",fg="white",bg="black")
text_upl.grid(pady=20)
text_upl.place(x=515,y=210, anchor="center")
#msg
msg_txt=Label(root,text="Check your speed through our Software",font="helvetica 23 bold",fg="white",bg="black")
msg_txt.grid(pady=10)
msg_txt.place(x=343,y=273,anchor="center")
#check_button
check=Button(root,text="Check",pady=8,padx=9,command=speed,font="helvetica 13 bold",bg="grey",fg="white",relief=SUNKEN)
check.grid(pady=20)
check.place(x=351,y=328,anchor="center")

#statusbar
statusvar=StringVar()
statusvar.set("Ready")
sbar=Label(root,textvariable=statusvar,relief=SUNKEN,anchor="w")
sbar.pack(fill=X,side=BOTTOM)
#credits
text_credit=Label(root,text="For any queries e-mail us at\n"
                            "tandonshivam05@gmail.com",font="helvetica 10",fg="white",bg="black")
text_credit.pack(fill=Y,side=BOTTOM,anchor="se")

#rating
Button(root,text="Rate Us",pady=3,command=getrate,font="helvetica 10 bold",bg="grey",fg="white",relief=SUNKEN).pack(fill=Y,side=BOTTOM,anchor="sw",padx=4,pady=1)
myslider=Scale(root,from_=0,to=10,orient=HORIZONTAL,bg="grey")
myslider.pack(fill=Y,side=BOTTOM,anchor="sw",padx=4,pady=1)
tx_rate=Label(root,text="Give us rating",font="helvetica 13 bold",fg="white",bg="black")
tx_rate.pack(fill=Y,side=BOTTOM,anchor="sw",padx=4,pady=1)

#fB
my_fb=Image.open("fb.png")
fb_img=my_fb.resize((38,39),Image.ANTIALIAS)
fb_new=ImageTk.PhotoImage(fb_img)
fb=Button(root,image=fb_new,command=callfacebook).pack(side=TOP,anchor="se",padx=6,pady=3)
#insta
my_insta=Image.open("twi.png")
insta_img=my_insta.resize((38,39),Image.ANTIALIAS)
insta_new=ImageTk.PhotoImage(insta_img)
insta=Button(root,image=insta_new,command=calltwitter).pack(side=TOP,anchor="se",padx=6,pady=3)
#Git
my_git=Image.open("git.png")
git_img=my_git.resize((38,39),Image.ANTIALIAS)
git_new=ImageTk.PhotoImage(git_img)
git=Button(root,image=git_new,command=callgithub).pack(side=TOP,anchor="se",padx=6,pady=3)
#Linkedin
my_lin=Image.open("lin.png")
lin_img=my_lin.resize((38,39),Image.ANTIALIAS)
lin_new=ImageTk.PhotoImage(lin_img)
lin=Button(root,image=lin_new,command=calllinkedin).pack(side=TOP,anchor="se",padx=6,pady=3)
root.mainloop()
a=input()
