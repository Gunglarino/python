import requests
import xmltodict
from tkinter import *
from tkinter import ttk
def getTrains():
    inp = str.lower(b.get())
    auth_details = ('thomas.vandenberg@student.hu.nl', '15WrX1DxLAGDQFUcqzdqppBt2f48VaFj0z8EwYDRd0paR88-dN7pDw')
    api_url = 'http://webservices.ns.nl/ns-api-avt?station='+inp
    response = requests.get(api_url, auth=auth_details)

    vertrekXML = xmltodict.parse(response.text)
    for vertrek in vertrekXML['ActueleVertrekTijden']['VertrekkendeTrein']:
        eindbestemming = vertrek['EindBestemming']
        treinSoort = vertrek["TreinSoort"]
        spoor = vertrek["VertrekSpoor"]
        vertrekSpoor = spoor['#text']

        vertrektijd = vertrek['VertrekTijd']  # 2016-09-27T18:36:00+0200
        vertrektijd = vertrektijd[11:16]  # 18:36
        Label(root,
              text='Om ' + vertrektijd + " vertrekt een " + treinSoort + " naar " + eindbestemming + " vanaf spoor " + vertrekSpoor).grid()

root = Tk()
ttk.Button(root, text="Krijg de treinen", command=getTrains).grid(column=1)
b = StringVar()
inputBox = Entry(root, textvariable=b).grid()



root.mainloop()