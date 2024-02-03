from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("ImageViewerPy")
root.iconbitmap("icon/ImageViewerPy.ico")
max_dimension = 500

imgno = 0

def forward():
    global imagedisplay, button_back,button_forward, imgno,button_forward,button_back,button_quit,status
        
    imagedisplay.grid_forget()
    imgno += 1
    imagedisplay = Label(image=final_imgs[imgno],padx=10,pady=10)
    button_back = Button(root, text="<<",command=previous,font="helvetica")
    button_forward = Button(root, text=">>",command=forward,font="helvetica")
    status = Label(root, text= "Image "+str(imgno+1)+" of "+str(len(final_imgs)))
    
    if imgno == len(final_imgs) - 1:
        button_forward = Button(root, text=">>",state = DISABLED)
    
    imagedisplay.grid(row=0,column=0,columnspan=3)
    status.grid(row=2,column=1)
    button_back.grid(row=1,column=0)
    button_forward.grid(row=1,column=2)
    

def previous():
    global imagedisplay, button_back,button_forward, imgno,button_forward,button_back,button_quit,status
    imagedisplay.grid_forget()
    imgno -= 1
    imagedisplay = Label(image=final_imgs[imgno],padx=10,pady=10)
    button_back = Button(root, text="<<",command=previous,font="helvetica")
    button_forward = Button(root, text=">>",command=forward,font="helvetica")
    status = Label(root, text= "Image "+str(imgno+1)+" of "+str(len(final_imgs)))
    
    if imgno == 0:
        button_back = Button(root, text="<<",state = DISABLED)
    
    imagedisplay.grid(row=0,column=0,columnspan=3)
    status.grid(row=2,column=1)
    button_back.grid(row=1,column=0)
    button_forward.grid(row=1,column=2)

img1 = Image.open("images/1.png")
img2 = Image.open("images/2.png")
img3 = Image.open("images/3.png")
img4 = Image.open("images/4.png")
imgs = [img1,img2,img3,img4]
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
final_imgs = [my_img1, my_img2, my_img3, my_img4]

status = Label(root, text= "Image "+str(imgno+1)+" of "+str(len(final_imgs)))
imagedisplay = Label(image=final_imgs[imgno])
imagedisplay.grid(row=0,column=0,columnspan=3,padx=10,pady=10)

button_back = Button(root, text="<<",command=previous,state=DISABLED,font="helvetica")
button_quit = Button(root, text="Exit",command=root.quit,font="helvetica")
button_forward = Button(root, text=">>",command= forward,font="helvetica")

button_back.grid(row=1,column=0)
button_quit.grid(row=1,column=1)
button_forward.grid(row=1,column=2)
status.grid(row=2,column=1)

root.mainloop()