import json
from os import name
from urllib import request

def createUser(request):
    neuerUser = request.GET
    dateiNameUser =  "./main/user/" + neuerUser["name"] + ".txt"

    with open (dateiNameUser, "w") as datei:
        datei.write(json.dumps(neuerUser))

'''def createBeitrag(request):
    neuerBeitrag = request.GET
    dateiNameBeitrag = "../post/" + neuerBeitrag[name] + neuerBeitrag[artikel] + ".txt"

    with open (dateiNameBeitrag, "w")as datei:
        datei.write(json.dumps(neuerBeitrag))


def loginUser(file, request):
    loginDaten = request.GET
    file = "./user/"
    for element in file:
        elementliste = element.split()
        vorhandenerUser = elementliste[0] #wie bekomm ich beim splitten nur den ersten Teil?
        if vorhandenerUser == loginDaten["name"]:
            for item in element:
                if item == "Passwort":
                    if Passwort ==         


def addKommentar(request):
    Kommentar = request.GET
    file = "./post/"
    
'''