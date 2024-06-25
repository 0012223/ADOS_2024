from ultralytics import YOLO
from tkinter import *
from PIL import ImageTk, Image
import glob


model = YOLO("../runs/detect/train/weights/best.pt")

imgs = glob.glob('dataset/test/images/*.jpg')


def forward(img_no):
    global label
    global button_forward
    global button_back
    global button_exit
    label.grid_forget()

    label = Label(image=List_images[img_no-1])
    label.grid(row=1, column=0, columnspan=3)
    button_forward = Button(root, text="forward",
                        command=lambda: forward(img_no+1))

    if img_no == len(List_images):
        button_forward = Button(root, text="Forward",
                                state=DISABLED)

    button_back = Button(root, text="Back",
                         command=lambda: back(img_no-1))

    button_back.grid(row=5, column=0)
    button_exit.grid(row=5, column=1)
    button_forward.grid(row=5, column=2)

def back(img_no):
    global label
    global button_forward
    global button_back
    global button_exit
    label.grid_forget()

    label = Label(image=List_images[img_no - 1])
    label.grid(row=1, column=0, columnspan=3)
    button_forward = Button(root, text="forward",
                            command=lambda: forward(img_no + 1))
    button_back = Button(root, text="Back",
                         command=lambda: back(img_no - 1))

    if img_no == 1:
        button_back = Button(root, text="Back", state=DISABLED)

    label.grid(row=1, column=0, columnspan=3)
    button_back.grid(row=5, column=0)
    button_exit.grid(row=5, column=1)
    button_forward.grid(row=5, column=2)

root = Tk()
root.title("Image Viewer")
root.geometry("700x700")

List_images = []

for img in imgs:
    
    List_images.append(ImageTk.PhotoImage(Image.open(
        model(img)[0].save(filename = "tmp.jpg")
    )))

label = Label(image=None)
label.grid(row=1, column=0, columnspan=3)

button_back = Button(root, text="Back", command=back,
                     state=DISABLED)

button_exit = Button(root, text="Exit",
                     command=root.quit)

button_forward = Button(root, text="Forward",
                        command=lambda: forward(1))

button_back.grid(row=5, column=0)
button_exit.grid(row=5, column=1)
button_forward.grid(row=5, column=2)

root.mainloop()