import tkinter
import os
import tkinter.filedialog
from tkinter import PhotoImage
from PIL import Image, ImageTk, ImageFont, ImageDraw

screen = tkinter.Tk()
screen.geometry("600x400")
screen.title("ImageWaterMarking")

file = tkinter.filedialog.askopenfilename(title="Choose the image", filetypes=(("png files", "*.png"), ("all files", ".*")))
label = tkinter.Label(text="This image will be watermarked")
label.pack()
myimage = ImageTk.PhotoImage(Image.open(file))
myimageLabel = tkinter.Label(image=myimage)
myimageLabel.pack()


labeltext = tkinter.Label(text="Enter the text you want to put as a watermark.")
labeltext.pack()
text=tkinter.Text(height=2, width=50)
text.pack()

button = tkinter.Button(text="Add Watermark")
button.pack()

screen.mainloop()