#Version 2
#Simple script to overlay Liz Ladder Size Standards over Geneious for Fragment Analysis
#If Liz Ladder does not fit, stretch borders or adjust image file in Paint to fit your monitor
#Can be used to overlay other image files over desktop applications 
#Just replace file and adjust root.geometry for initial window size (right click image properties for dimensions)



from Tkinter import *
from PIL import Image, ImageTk

class App(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.columnconfigure(0,weight=1)
        self.rowconfigure(0,weight=1)
        self.original = Image.open('LizLadderStandardPurple.png')
        self.image = ImageTk.PhotoImage(self.original)
        self.display = Canvas(self, bd=0, highlightthickness=1)
        self.display.create_image(0, 0, image=self.image, anchor=NW, tags="IMG")
        self.display.grid(row=0, sticky=W+E+N+S)
        self.lift()
        self.pack(fill=BOTH, expand=1)
        self.bind("<Configure>", self.resize)

    def resize(self, event):
        size = (event.width, event.height)
        resized = self.original.resize(size,Image.ANTIALIAS)
        self.image = ImageTk.PhotoImage(resized)
        self.display.delete("IMG")
        self.display.create_image(0, 0, image=self.image, anchor=NW, tags="IMG")

root = Tk()
root.wm_attributes("-topmost", True)                #Always on top
root.wm_attributes("-transparentcolor", "white")	#Make white transparent
root.update()
root.geometry('1122x212')							#Initial window size

app = App(root)
app.mainloop()
#root.destroy()