import tkinter as tk
from PIL import ImageTk, Image


root = tk.Tk()
root.title('Matrix Calculator')

canvas = tk.Canvas(root, bg="blue", height=400, width=600)       #main window
background_win1 = ImageTk.PhotoImage(Image.open(r'../fbackground2.jpg'))

background_label = tk.Label(root, image = background_win1)
background_label.pack()
canvas.pack()

frame = tk.Frame(root, bg = 'black')        #frame inside main window
frame.place(relx = 0.15, rely = 0.15, relwidth = 0.7, relheight = 0.7)

label_win1_1 = tk.Label(frame, text = "Matrix Calculator", bg = 'black', fg = 'white', font = ("Times New Roman" ,44))
label_win1_1.pack(anchor = 'center')

label_win1_2 = tk.Label(frame, text = "Choose language:", bg = 'black', fg = 'white', font = ("Times New Roman" ,28))
label_win1_2.place(relx = 0.5, rely = 0.2, anchor = 'center')

button_EN = tk.Button(frame, text = "English", bg = '#3d3b3b', fg = 'white', width = 14)
button_EN.place(relx = 0.5, rely = 0.3, anchor = 'center')

button_PL = tk.Button(frame, text = "Polish", bg = '#3d3b3b', fg = 'white', width = 14)
button_PL.place(relx = 0.5, rely = 0.35, anchor = 'center')

root.mainloop()