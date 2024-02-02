from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("ImageViewerPy")
root.iconbitmap("icon/ImageViewerPy.ico")

def buttonnext():
    return

def buttonprevious():
    return

my_img1 = ImageTk.PhotoImage(Image.open("images/1.png"))
my_img2 = ImageTk.PhotoImage(Image.open("images/2.png"))
my_img3 = ImageTk.PhotoImage(Image.open("images/3.png"))
my_img4 = ImageTk.PhotoImage(Image.open("images/4.png"))

all_imgs = [my_img1,my_img2,my_img3,my_img4]
imagedisplay = Label(image=my_img1)
imagedisplay.grid(row=0,column=0,columnspan=3)

button_back = Button(root, text="<<",command=buttonprevious)
button_quit = Button(root, text="Exit",command=root.quit)
button_forward = Button(root, text=">>",command=buttonnext)

button_back.grid(row=1,column=0)
button_quit.grid(row=1,column=1)
button_forward.grid(row=1,column=2)

root.mainloop()