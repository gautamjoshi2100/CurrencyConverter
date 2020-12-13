#reqired libraries 
from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
import requests

#main window and it's config
root = Tk()
root.geometry("550x600")
root.title("Currency Converter")

#canvas and background image
canvas = Canvas(root,width=800,height=600)
img = ImageTk.PhotoImage(Image.open('assets\\bgpic.jpg'))
canvas.create_image(0,0,anchor=NW, image=img)
canvas.pack(side='top', fill='both', expand='yes')

#main heading
main_heading = Label(canvas,text="Currency Converter",bg="#A5BD35",fg="black",font="Arial 24 italic")
main_heading.grid(row=0,column=0,padx=100,pady=50,columnspan=2)

# API_KEY!!
API_KEY = '0dda6bc98dbc5313e31487283f21a12e'

# method to request data from server and do the calulations 
def do_calcualations():
    currency_from = currency_selecter1.get()
    currency_to = currency_selecter2.get()
    url = "https://data.fixer.io/api/latest?access_key="+API_KEY+'&base='+currency_from+'&symbols='+currency_to

    # get data and convert to json format
    exchange_data=requests.get(url)
    recived_data = exchange_data.json()
    money1 = Input1.get("1.0",END)
    money1 = float(money1)

    money2 = float(recived_data['rates'][currency_to])

    output = Label(canvas,text=money1*money2,width=20,font=('Verdana',20)).grid(row=2,column=1)


# input box and other UI related stuff
Input1 = Text(canvas,height=1,width=20,font=('Verdana',20))
Input1.grid(row=1,column=1, padx=20)
url = "https://data.fixer.io/api/symbols?access_key="+API_KEY
exchange_data=requests.get(url)
recived_data = exchange_data.json()
myOptList = list()
for opt in recived_data['symbols']:
    myOptList.append(opt)


currency_selecter1 = ttk.Combobox(canvas,values= myOptList,font ="Verdana 14" ,width=12)
currency_selecter1.set("USD")
currency_selecter1.grid(row=1,column=0, padx=5, pady=5)


currency_selecter2 = ttk.Combobox(canvas,values= myOptList,font ="Verdana 14" ,width=12)
currency_selecter2.set("EUR")
currency_selecter2.grid(row=2,column=0, padx=5, pady=35)


calculate = Button(canvas,text="Convert!",width = 15,font="Arial 15 bold",fg= "black",bg="#61E713",command=do_calcualations)
calculate.grid(row=3,column=1,rowspan=1)

root.mainloop()
