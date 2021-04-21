import tkinter
from PIL import ImageTk, Image
import os

root = tkinter.Tk()  

img = ImageTk.PhotoImage(Image.open("pup.jpg"))
  

panel = tkinter.Label(root, image = img)
  

panel.pack(side = "bottom", fill = "both",
           expand = "yes")
  
root.mainloop()