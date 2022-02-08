from tkinter import Label, Tk, Frame, N, W, E, S

import cv2
from PIL import Image, ImageTk

root = Tk()
root.title("Goggle")
root.bind("<Escape>", lambda _ : root.quit())

mainframe = Frame(root)
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

label = Label(mainframe)
label.grid(row=0,column=0)

cap = cv2.VideoCapture(0)

def show_frame():
    _, frame = cap.read()
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    label.imgtk = imgtk
    label.configure(image=imgtk)
    label.after(100, show_frame)

show_frame()
root.mainloop()
root.destroy()
cap.release()
