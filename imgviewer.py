from tkinter import *
import os
from PIL import ImageTk, Image

root = Tk()
root.title("ImageViewerPy")
root.iconbitmap("icon/ImageViewerPy.ico")
root.configure(bg="#303030")
fontscript = ("helvetica",15,"bold")
fontscript2 = ("arial",12)
max_dimension = 500
imgno = 0
directory = "images"

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
    
    imagedisplay.pack(expand=True,padx=10,pady=10)
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
    
    imagedisplay.pack(expand=True,padx=10,pady=10)
    button_back.grid(row=0,column=0)
    button_forward.grid(row=0,column=2)
    status.grid(row=1,column=1)

#reading all images
imgs = []
for filename in os.listdir(directory):
    if filename.endswith(".jpg") or filename.endswith(".png"): # Adjust extensions as needed
        image_path = os.path.join(directory, filename)
        image = Image.open(image_path)
        imgs.append(image)
        
#image resizing
resized_imgs = list()
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
final_imgs = []
for i in resized_imgs:
    my_img = ImageTk.PhotoImage(i)
    final_imgs.append(my_img)

#Frame 1 Holding Image
frame = Frame(root, width=700, height=500,bg="#303030",padx=20,pady=20)
frame.pack(expand=True)
frame.pack_propagate(False)

imagedisplay = Label(frame,image=final_imgs[imgno],justify="center")
imagedisplay.pack(expand=True,padx=10,pady=10)

#Frame 2 Consisting of Buttons
frame2 = Frame(root, width=700, height=200,bg="#303030")
frame2.pack()

button_back = Button(frame2, text="<<",command=previous,state=DISABLED,font = fontscript,bg="#0078c2",fg="white",bd=0)
button_quit = Button(frame2, text="Exit",command=root.quit,font = fontscript,padx = 30,bg="#0078c2",fg="white")
button_forward = Button(frame2, text=">>",command= forward,font = fontscript,bg="#0078c2",fg="white")
status = Label(frame2, text= "Image "+str(imgno+1)+" of "+str(len(final_imgs)),font=fontscript2,bg="#303030",fg="white")

button_back.grid(row=0,column=0)
button_quit.grid(row=0,column=1)
button_forward.grid(row=0,column=2)
status.grid(row=1,column=1)

root.mainloop()