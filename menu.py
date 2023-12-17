
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import mysql.connector as db


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\micha\OneDrive\Desktop\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)
def editBarang():
    import edit

mydb = db.connect(
  host="localhost",
  user="root",
  password=""
)

window = Tk()

window.geometry("734x464")
window.configure(bg = "#628469")


canvas = Canvas(
    window,
    bg = "#628469",
    height = 464,
    width = 734,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    370.0,
    236.0,
    image=image_image_1
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=41.0,
    y=199.0,
    width=130.0,
    height=141.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: [print("button_2 clicked"), editBarang()],
    relief="flat"
)
button_2.place(
    x=389.0,
    y=199.0,
    width=126.0,
    height=141.0
)

canvas.create_text(
    229.29989624023438,
    18.69293212890625,
    anchor="nw",
    text="Hello, User!",
    fill="#FFFFFF",
    font=("Sansation Regular", 53 * -1)
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=554.0,
    y=199.0,
    width=125.0,
    height=145.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat"
)
button_4.place(
    x=210.0,
    y=199.0,
    width=131.0,
    height=141.0
)

window.title("Menu Utama")
window.resizable(False, False)
window.mainloop()
