# TODO hacer un programa con ventana
# donde el usuario pueda insertar un enlace de youtube
# y pueda elegir dos opciones: Peek y Download.
# Si se elige Peek se mostrará el título del video,
# el canal, y la miniatura.
# Si se elige Download se descargará el video.

from pytube import YouTube
import tkinter as ttk
import ttkbootstrap as ttk
from PIL import Image, ImageTk
from fontTools.ttLib import TTFont
import requests
from io import BytesIO

def select_font(type):
    font_path = f"assets/fonts/Poppins-{type}.ttf"
    my_font = TTFont(font_path) 
    return my_font

def peek_video():
    url = link_input.get()
    video = YouTube(url)

    title_label.config(text=video.title)
    autor_label.config(text=video.author)

    img = requests.get(video.thumbnail_url)
    thumbnail_image = ImageTk.PhotoImage(Image.open(BytesIO(img.content)).resize((320, 180)))
    image_panel.config(image=thumbnail_image)
    image_panel.image = thumbnail_image

    return video

def download_video():
    video = peek_video().streams.get_highest_resolution()
    video.download()
    print(f"{video.title}.mp4 has been downloaded")

root = ttk.Window(themename="vapor")
root.title("YT.py")
root.geometry("700x500")

frm = ttk.Frame(root)
frm.pack(padx=30, pady=20)

link_input = ttk.Entry(frm, font=(select_font("Regular"), 12))
link_input.pack()
link_input.insert(0, "https://youtu.be/dQw4w9WgXcQ")

title_label = ttk.Label(frm, text="Enter a YT link", font=(select_font("SemiBold"), 20), wraplength=650)
title_label.pack()

autor_label = ttk.Label(frm, text="and select an option", font=(select_font("Medium"), 16))
autor_label.pack(pady=10)

thumbnail_image = ImageTk.PhotoImage(Image.open("assets/images/cat.png").resize((180, 180)))
image_panel = ttk.Label(frm, image=thumbnail_image)
image_panel.pack()

ttk.Button(frm, text="Peek video", command=peek_video).pack(pady=20)
ttk.Button(frm, text="Download video", command=download_video).pack(pady=20)

root.mainloop()
