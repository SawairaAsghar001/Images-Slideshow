from itertools import cycle
from PIL import Image, ImageTk
import time
import tkinter as tk 


root = tk.Tk()
root.title("Image Slideshow Viewer")

#List of Image Path
image_paths = [
    r"E:\Projects\6.Image Slideshow\Images\AHHO9094.JPG",
    r"E:\Projects\6.Image Slideshow\Images\BSQN8941.JPG",
    r"E:\Projects\6.Image Slideshow\Images\CZWN3728.JPG",
    r"E:\Projects\6.Image Slideshow\Images\IMG_4664.JPG",
    r"E:\Projects\6.Image Slideshow\Images\IMG_5531.PNG",
    r"E:\Projects\6.Image Slideshow\Images\IMG_5532.PNG",
    r"E:\Projects\6.Image Slideshow\Images\IMG_5535.PNG",
    r"E:\Projects\6.Image Slideshow\Images\IMG_5983.JPG",
]
#Resize the images to 180x1080
image_size= (1080,1080)
images = [Image.open(path).resize(image_size) for path in image_paths]
photo_images =[ImageTk.PhotoImage(image)for image in images]


label = tk.Label(root)
label.pack()

def update_image():
    for photo_image in photo_images:
        label.config(image=photo_image)
        label.update()
        time.sleep(3)

Slideshow= cycle(photo_images)

def start_slideshow():
    for _ in range(len(image_paths)):
        update_image()

play_button = tk.Button(root, text= 'Play', command=start_slideshow)
play_button.pack()

root.mainloop()