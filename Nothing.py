from datetime import datetime
import time
import tkinter as tk
from PIL import Image, ImageTk


def Time_Left():
    target_date = datetime(2025, 5, 3, 12)
    current_time = datetime.now()
    time_difference = target_date - current_time
    seconds_left = time_difference.total_seconds()
    days = seconds_left / 86400
    hours = (seconds_left - (int(days) * 86400)) / 3600
    minutes = (seconds_left - int(days) * 86400 - int(hours) * 3600) / 60
    seconds = (seconds_left - int(days) * 86400 - int(hours) * 3600 - int(minutes) * 60)
    return int(days), int(hours), int(minutes), int(seconds)

def update():
    days, hours, minutes, seconds = Time_Left()
    time_left_text.set(f"{days} days, {hours} hours, {minutes} minutes, {seconds} seconds")
    window.after(1000, update)

window = tk.Tk()
window.title("Time Until")

image = Image.open("racoon.jpg")
photo = ImageTk.PhotoImage(image)
image2 = Image.open("nachos.jpg")
photo2 = ImageTk.PhotoImage(image2)
image3 = Image.open("spider.jpg")
resized_image = image3.resize((210,182))
photo3 = ImageTk.PhotoImage(resized_image)
image4 = Image.open("Rk.jpg")
resize = image4.resize((300,215))
photo4 = ImageTk.PhotoImage(resize)
image5 = Image.open("flower.jpg")
photo5 = ImageTk.PhotoImage(image5)

window.geometry("800x400")
time_left_text = tk.StringVar()
window.configure(bg="white")
word_label = tk.Label(window, text = "Time until Kiersten", font=("Arial", 24), bg="white", fg = 'blue')
word_label.place(x=275, y=25)
time_label = tk.Label(window, textvariable=time_left_text, font=("Arial", 14, "bold"), bg="white", fg = 'pink')
image_label = tk.Label(window, image=photo)
image_label.place(x=-10, y=185)
image_label2 = tk.Label(window, image=photo2)
image_label2.place(x=530, y=220)
image_label3 = tk.Label(window, image=photo3)
image_label3.place(x=-10, y=0)
image_label4 = tk.Label(window, image=photo4)
image_label4.place(x=228, y=185)
image_label5 = tk.Label(window, image=photo5)
image_label5.place(x=600, y=-8)
time_label.pack(pady=75)
update()

window.mainloop()