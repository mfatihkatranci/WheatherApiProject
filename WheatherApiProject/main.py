from tkinter import *
from tkinter import ttk
import requests

window = Tk()
window.title("Wheater App")
window.minsize(400,400)

def get_weather(event):
    city= event.widget.get()
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    if response.status_code == 200:

        weather_desc = data["weather"][0]["description"]

        temperature = data["main"]["temp"]

        result_label.config(text=f"Weather: {weather_desc}\nTemperature: {temperature}°C")
    else:
        result_label.config(text="City not found.")



choose_label = Label(text="Lütfen Hava durumunu Görmek İstediğiniz Şehri Seçiniz")
choose_label.grid(row=0,column=0)

selected_city = StringVar()
city_box = ttk.Combobox(window,width = 27,  textvariable = selected_city,state = "readonly")

city_box["values"] = ("Adana", "Adıyaman", "Afyon", "Ağrı", "Amasya", "Ankara", "Antalya", "Artvin", "Aydın", "Balıkesir",
          "Bilecik", "Bingöl", "Bitlis", "Bolu", "Burdur", "Bursa", "Çanakkale", "Çankırı", "Çorum", "Denizli",
          "Diyarbakır", "Edirne", "Elazığ", "Erzincan", "Erzurum", "Eskişehir", "Gaziantep", "Giresun", "Gümüşhane",
          "Hakkari", "Hatay", "Isparta", "İçel (Mersin)", "İstanbul", "İzmir", "Kars", "Kastamonu", "Kayseri",
          "Kırklareli", "Kırşehir", "Kocaeli", "Konya", "Kütahya", "Malatya", "Manisa", "Kahramanmaraş", "Mardin",
          "Muğla", "Muş", "Nevşehir", "Niğde", "Ordu", "Rize", "Sakarya", "Samsun", "Siirt", "Sinop", "Sivas",
          "Tekirdağ", "Tokat", "Trabzon", "Tunceli", "Şanlıurfa", "Uşak", "Van", "Yozgat", "Zonguldak", "Aksaray",
          "Bayburt", "Karaman", "Kırıkkale", "Batman", "Şırnak", "Bartın", "Ardahan", "Iğdır", "Yalova", "Karabük",
          "Kilis", "Osmaniye", "Düzce")
city_box.grid(row=1,column=0)
city_box.bind("<<ComboboxSelected>>", get_weather)

result_label = Label(text="")
result_label.grid(row=2,column=0)

city = city_box.get()
api_key = "key"

#get_weather()
window.mainloop()