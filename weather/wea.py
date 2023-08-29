from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import requests

def data_get():
    city = city_name.get()
    response = requests.get("https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=18f483d60d0bd05e8d45173be9206b0a")
    
    data = response.json()
    w_label1.config(text=data["weather"][0]["main"])
    wb_label1.config(text=data["weather"][0]["description"])
    temp_label1.config(text=str(int(data["main"]["temp"] - 273.15)))
    per_label1.config(text=data["main"]["pressure"])

win = Tk()
win.title("Weather App")
win.config(bg="#7fa9bc")
win.geometry("570x570")

name_label = Label(win, text="WEATHER FORECAST", font=("Times New Roman", 25, "bold"), fg="#0D26F3")
name_label.place(x=25, y=50, height=50, width=450)

city_name = StringVar()
list_name = ["Mumbai", "Delhi", "Bangalore", "Hyderabad", "Chennai", "Kolkata", "Pune", "Ahmedabad", "Jaipur", "Surat", "Lucknow", "Kanpur", "Nagpur", "Indore", "Thane", "Bhopal", "Visakhapatnam", "Pimpri-Chinchwad", "Patna", "Vadodara"]
com = ttk.Combobox(win, values=list_name, font=("Times New Roman", 20, "bold"), textvariable=city_name)
com.place(x=25, y=120, height=50, width=250)

w_label = Label(win, text=" Climate", font=("Times New Roman", 15, "bold"), fg="#3C4EDD", bg="#Cfd3f0")
w_label.place(x=25, y=260, height=50, width=210)
w_label1 = Label(win, text=" ", font=("Times New Roman", 15, "bold"), fg="black", bg="#Cfd3f0")
w_label1.place(x=250, y=260, height=50, width=210)

wb_label = Label(win, text=" Description", font=("Times New Roman", 15, "bold"), fg="#3C4EDD", bg="#Cfd3f0")
wb_label.place(x=25, y=330, height=50, width=210)
wb_label1 = Label(win, text=" " , font=("Times New Roman", 15, "bold"), fg="black", bg="#Cfd3f0")
wb_label1.place(x=250, y=330, height=50, width=210)

temp_label = Label(win, text="Temperature", font=("Times New Roman", 15, "bold"), fg="#3C4EDD", bg="#Cfd3f0")
temp_label.place(x=25, y=400, height=50, width=210)
temp_label1 = Label(win, text="", font=("Times New Roman", 15, "bold"), fg="black", bg="#Cfd3f0")
temp_label1.place(x=250, y=400, height=50, width=210)

per_label = Label(win, text="Pressure", font=("Times New Roman", 15, "bold"), fg="#3C4EDD", bg="#Cfd3f0")
per_label.place(x=25, y=470, height=50, width=210)
per_label1 = Label(win, text="", font=("Times New Roman", 15, "bold"), fg="black", bg="#Cfd3f0")
per_label1.place(x=250, y=470, height=50, width=210)

done_button = Button(win, text="Done", font=("Times New Roman", 20, "bold"), bg="#2f98bb", command=data_get)
done_button.place(y=190, height=50, width=80, x=200)


icon = Image.open("g.png")

icon = icon.resize((152, 130))

icon_image = ImageTk.PhotoImage(icon)

icon_label = Label(win, image=icon_image)
icon_label.place(x=300, y=120)

win.mainloop()
