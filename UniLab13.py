from tkinter import *
from tkinter import ttk
import requests
import json

# root = Tk() # Создаем главный объект (окно приложения)
#
# def get_weather():
#     city = cityField.get()  # Получаем данные от пользователя
#     key = 'd50a0e25446332b729f305864f7327fb'
#     # ссылка, с которой мы получим все данные в формате JSON
#     url = 'http://api.openweathermap.org/data/2.5/weather'
#     # Доп. параметры (ключ, город и единицы измерения - metric означает Цельсий)
#     params = {'APPID': key, 'q': city, 'units': 'metric'}
#     # Отправляем запрос по URL
#     result = requests.get(url, params=params)
#     weather = result.json()  # Получаем JSON ответ по этому URL
#     print(weather)
#     info['text'] = f'{str(weather["name"])}: {weather["main"]["temp"]}'
#
# root['bg'] = '#fafafa' # фоновый цвет
# root.title('Погодное приложение') # название окна
# root.geometry('300x250') # размеры окна
# root.resizable(width=False, height=False)
# # Создаем фрейм (область для размещения других объектов)
# frame_top = Frame(root, bg='#ffb700')
# frame_top.place(relx=0.15, rely=0.15, relwidth=0.7, relheight=0.25)
# # Все то-же самое, но для второго фрейма
# frame_bottom = Frame(root, bg='#ffb700', bd=5)
# frame_bottom.place(relx=0.15, rely=0.55, relwidth=0.7, relheight=0.1)
# # Создаем текстовое поле для получения данных от пользователя
# cityField = Entry(frame_top, bg='white', font=30)
# cityField.pack() # Размещение текстового поля
# # Создаем кнопку и при нажатии будет срабатывать метод "get_weather"
# btn = Button(frame_top, text='Посмотреть погоду', command=get_weather)
# btn.pack()
# # Создаем текстовую надпись, в кот. выведем информацию о погоде
# info = Label(frame_bottom, text='Погода в городе', bg='#ffb700', font=("Arial", 10))
# info.pack()
# # Запускаем постоянный цикл, чтобы программа работала
# root.mainloop()


def get_event():
    clientID = "NDE0NzQwNjZ8MTcxNTM3NzI0OS44MTkwMTg2"
    place = listInFrame.get()
    response = requests.get(f"https://api.seatgeek.com/2/venues?city={place}&client_id={clientID}")
    response = json.loads(response.content)["venues"]
    where = ""
    slug = ""
    whereStart = "WHERE EVENT:"
    slugStart = "SLUG OF EVENT:"
    for i in range(len(response)):
         wherenew= response[i]["address"]
         slugnew= response[i]["slug"]
         if i % 2 == 0:
             where = where + "\n"
             slug = slug + "\n"
         i = str(i + 1)
         where = where+", "+ i + ") " + wherenew
         slug = slug+", " + i + ") " + slugnew
    where = where[2:]
    slug = slug[2:]
    where = whereStart + where
    slug = slugStart + slug
    eventsSlug["text"] = slug
    whereEvents["text"] = where
    print(where, slug)

mainWindow = Tk()
mainWindow.geometry("800x800")
mainWindow.title("EVENTS IN THE US:((")
mainWindow.resizable(width=False, height=False)
topFrameInMain = Frame(mainWindow, bg="blue")
topFrameInMain.place(relx=0.1, rely=0.1, relwidth=0.75, relheight=0.1)
info = Label(topFrameInMain, text= "Choose city of USA :(", bg='blue', font=("Arial", 10))
info.pack()
CitiesOfEvil = ["LA", "NY", "SF", "Chicago"]
listInFrame = ttk.Combobox(topFrameInMain, values=CitiesOfEvil )
listInFrame.pack()
btnn = Button(topFrameInMain, text='GET SAD BUTTON',command=get_event)
btnn.pack()
lowerFrame = Frame(mainWindow, bg="blue")
lowerFrame.place(relx=0.1, rely=0.4, relwidth=0.75, relheight=0.5)
whereEvents = Label(lowerFrame, text="WHERE EVENTS", bg="blue" , font=("Arial", 10))
whereEvents.pack()
eventsSlug = Label(lowerFrame, text="EVENTS SLUG", bg="blue" , font=("Arial", 10))
eventsSlug.pack()
mainWindow.mainloop()