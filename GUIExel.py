import openpyxl
import subprocess
import sys
import random
import tkinter as tk
import time
from tkinter import *
import matplotlib.pyplot as plt
from datetime import date
from tkcalendar import Calendar, DateEntry
import varname
import re
alpha = ["C","D","E","F","G","H","I","J","K","L"]
years = [2009,2010,2011,2012,2013,2014,2015,2016,2017,2018]
countries=[]
variables_list = []
variables_list2 = []
checkboxlist = []
varlist = []
va = []

xpos = [50,50,50,50,50,50,50,50,50,50,50,50,50,175,175,175,175,175,175,175,175,175,175,175,175,175,300,300,300,300,300,300,300,300,300,300,300,300,300,425,425,425,425,425,425,425,425,425
,425,425,425,425,550,550,550,550,550,550,550,550,550,550,550,550,550,550,550,550]
ypos = [225,250,275,300,325,350,375,400,425,450,475,500,525,225,250,275,300,325,350,375,400,425,450,475,500,525,225,250,275,300,325,350,375,400,425,450,475,500,525,
225,250,275,300,325,350,375,400,425,450,475,500,525,225,250,275,300,325,350,375,400,425,450,475,500,525,550,575,600]
global vari2
def countries_exel():
    wb = openpyxl.load_workbook('CableBrodband.xlsx')
    sheet = wb['1'] # Get a sheet from the workbook.
    anotherSheet = wb.active
    for x in range(7, 41):
        thing = str(x)
        a = sheet['A' + thing].value
        countries.append(a)


countries_exel()

for y in range(1, len(countries)):
    checkboxlist.append("check"+str(y))




class App(tk.Tk):

    def __init__(self):
        def makecheck(vari, num, vari2,xnum,ynum):
            vari2 = IntVar()
            vari = Checkbutton(self,text=countries[num], variable=vari2)
            checkboxlist.append(vari)
            vari.place(x=xnum,y=ynum)
            varlist.append(vari2)

        def runmakecheck():
            for y in range(0, len(countries)-1):
                vary = "var"+str(y-1)
                # varlist.append(vary)
                makecheck( checkboxlist[y], y,vary,xpos[y],ypos[y])
            l.place_forget()
            submit.place(x=400, y=400)

        def go(vari,num):

            if((vari.get()) == 1):
                va.append(countries[num])


        def rungo():
            for a in range(0, len(countries)-1):
                go(varlist[a], a)
            rungetarray()
        def rungetarray():
            for country in va:
                b= []
                l = countries.index(country)
                wb = openpyxl.load_workbook('CableBrodband.xlsx')
                sheet = wb['1'] # Get a sheet from the workbook.
                anotherSheet = wb.active
                for x in (alpha):
                    thing = str(x)
                    a = sheet[x + str(l+7)].value
                    b.append(a)
                plt.plot(years,b)
            graph()
        def graph():
            plt.xlabel("Years")
            plt.ylabel("Broadband Cable suscriptions")
            plt.title("Broadband Cable suscriptions by year(2009-2018)")
            plt.legend(va)
            scale_factor = 1
            xmin, xmax = plt.xlim()
            plt.xlim((xmin * scale_factor)+1, xmax * scale_factor)
            plt.show()

        selfdow_x = 780
        selfdow_y = 720
        tk.Tk.__init__(self)
        self.title("Broard Band Cable Subcriptions per Country")
        self.geometry("1080x620") #Width x Height of selfdow
        title = tk.Label(self, text="Broard Band Cable Su   bcriptions per Country", fg="Black",font=("Courier", 24))
        title2 = tk.Label(self, text="Pick countries to Graph", fg="Black",font=("Courier", 18))
        for y in range(1, len(countries)):
         default = StringVar()
        t = tk.Entry(self)
        l = tk.Button(self, text="Start", command=runmakecheck)
        submit = tk.Button(self, text="Submit", command=rungo)
        l.place(x=400, y=400)
        title.place(x=200, y=25)
        title2.place(x=200, y=125)





walls = App()
walls.mainloop()
