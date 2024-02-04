from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("ImageViewerPy")
root.iconbitmap("icon/ImageViewerPy.ico")
root.configure(bg="#303030")
fontscript = ("helvetica",15,"bold")
fontscript2 = ("arial",12)
max_dimension = 500
imgno = 0

def forward():
    global imagedisplay, button_back,button_forward, imgno,button_forward,button_back,button_quit,status,frame,frame2,fontscript,fontscript2
        
    imagedisplay.pack_forget()
    imgno += 1
    imagedisplay = Label(frame,image=final_imgs[imgno])
    button_back = Button(frame2, text="<<",command=previous,font = fontscript,bg="#0078c2",fg="white")
    if imgno == len(final_imgs) - 1:
        button_forward = Button(frame2, text=">>",state = DISABLED,font = fontscript,bg="#0078c2",fg="white",bd=0,relief=SUNKEN)
    else:
        button_forward = Button(frame2, text=">>",command= forward,font = fontscript,bg="#0078c2",fg="white")
    status = Label(frame2, text= "Image "+str(imgno+1)+" of "+str(len(final_imgs)),font=fontscript2,bg="#303030",fg="white")
    
    imagedisplay.pack(padx=10,pady=10)
    button_back.grid(row=0,column=0)
    button_forward.grid(row=0,column=2)
    status.grid(row=1,column=1)
    

def previous():
    global imagedisplay, button_back,button_forward, imgno,button_forward,button_back,button_quit,status,frame,frame2,fontscript
    imagedisplay.pack_forget()
    imgno -= 1
    imagedisplay = Label(frame,image=final_imgs[imgno])
    button_forward = Button(frame2, text=">>",command= forward,font = fontscript,bg="#0078c2",fg="white")
    status = Label(frame2, text= "Image "+str(imgno+1)+" of "+str(len(final_imgs)),font=fontscript2,bg="#303030",fg="white")
    
    if imgno == 0:
        button_back = Button(frame2, text="<<",state=DISABLED,font = fontscript,bg="#0078c2",fg="white",bd=0,relief=SUNKEN)
    else:
        button_back = Button(frame2, text="<<",command=previous,font = fontscript,bg="#0078c2",fg="white")
    
    imagedisplay.pack(padx=10,pady=10)
    button_back.grid(row=0,column=0)
    button_forward.grid(row=0,column=2)
    status.grid(row=1,column=1)

img1 = Image.open("images/1.jpg")
img2 = Image.open("images/2.jpg")
img3 = Image.open("images/3.jpg")
img4 = Image.open("images/4.jpg")
img5 = Image.open("images/5.jpg")
imgs = [img1,img2,img3,img4,img5]
resized_imgs = list()

#image resizing
for i in imgs:
    width, height = i.size
    resized_image = i
    if width > max_dimension or height > max_dimension:
        if width > height:
            scale_factor = max_dimension / width
        elif height > width:
            scale_factor = max_dimension / height
        width = width * scale_factor
        height = height * scale_factor
        resized_image = i.resize((int(width), int(height)))
    resized_imgs.append(resized_image)

#image allocator
my_img1 = ImageTk.PhotoImage(resized_imgs[0])
my_img2 = ImageTk.PhotoImage(resized_imgs[1])
my_img3 = ImageTk.PhotoImage(resized_imgs[2])
my_img4 = ImageTk.PhotoImage(resized_imgs[3])
my_img5 = ImageTk.PhotoImage(resized_imgs[4])
final_imgs = [my_img1, my_img2, my_img3, my_img4,my_img5]

frame = Frame(root, width=1920, height=1080,bg="#303030",padx=20,pady=20)
frame.pack()

frame2 = Frame(root, width=1000, height=200,bg="#303030")
frame2.pack()
imagedisplay = Label(frame,image=final_imgs[imgno])
imagedisplay.pack()



button_back = Button(frame2, text="<<",command=previous,state=DISABLED,font = fontscript,bg="#0078c2",fg="white",bd=0)
button_quit = Button(frame2, text="Exit",command=root.quit,font = fontscript,padx = 30,bg="#0078c2",fg="white")
button_forward = Button(frame2, text=">>",command= forward,font = fontscript,bg="#0078c2",fg="white")
status = Label(frame2, text= "Image "+str(imgno+1)+" of "+str(len(final_imgs)),font=fontscript2,bg="#303030",fg="white")

button_back.grid(row=0,column=0)
button_quit.grid(row=0,column=1)
button_forward.grid(row=0,column=2)
status.grid(row=1,column=1)

root.mainloop()