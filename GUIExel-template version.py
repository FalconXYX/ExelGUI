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
,425,425,425,425,550,550,550,550,550,550,550,550,550,550,550,550,550,550,550,550]#These will have to be changed/removed
ypos = [225,250,275,300,325,350,375,400,425,450,475,500,525,225,250,275,300,325,350,375,400,425,450,475,500,525,225,250,275,300,325,350,375,400,425,450,475,500,525,
225,250,275,300,325,350,375,400,425,450,475,500,525,225,250,275,300,325,350,375,400,425,450,475,500,525,550,575,600]#These will have to be changed/removed
global vari2
def countries_exel(): #this function gets the name of all the countries in the first columb
    wb = openpyxl.load_workbook('CableBrodband.xlsx')#Put the name of your spread sheet here
    sheet = wb['1'] # Get the sheet from the workbook.
    anotherSheet = wb.active
    for x in range(7, 41):#the 7 and 41 will have to changed to fit your spreadsheet
        thing = str(x)# x to convert to string
        a = sheet['A' + thing].value #gets the name of the countrie in the first columb and "thing" is the row number, change A to the letter of the first row
        countries.append(a)#put that data in a array


countries_exel()

for y in range(1, len(countries)):
    checkboxlist.append("check"+str(y))
    #makes the names of all the checkboxes and puts them in a list



class App(tk.Tk):

    def __init__(self):
        def makecheck(vari, num, vari2,xnum,ynum):#make the checkboxes
            vari2 = IntVar() #makes a varible that changes if the check box is hit
            vari = Checkbutton(self,text=countries[num], variable=vari2)#makes the checkboxes
            vari.place(x=xnum,y=ynum)#place the box
            varlist.append(vari2)

        def runmakecheck():
            for y in range(0, len(countries)-1):#for every county run the function
                vary = "var"+str(y-1)
                makecheck( checkboxlist[y], y,vary,xpos[y],ypos[y])
            l.place_forget()
            submit.place(x=400, y=400)

        def go(vari,num):

            if((vari.get()) == 1):#if the check box is clicked
                va.append(countries[num])#add the country the checkbox is assoaited to to a list


        def rungo():
            for a in range(0, len(countries)-1):
                go(varlist[a], a)#for every countr run go()
            getarray()#then run getarray
        def getarray():

            wb = openpyxl.load_workbook('CableBrodband.xlsx')
            sheet = wb['1'] # Get a sheet from the workbook.
            anotherSheet = wb.active#find and activate the sheet
            for country in va: #for each country in va- the array that contains all the clicked countries and country is the current country we are fetching data for
                l = countries.index(country)# gets the position of the country in the array of all countries
                b= []
                for x in (alpha):# for every year which is repersented by an alphabet
                    thing = str(x)
                    a = sheet[x + str(l+7)].value# get the value of the cell that is the given year and the correct country we add 7 because there are 7 lines of ussless info above everything
                    b.append(a)#add it to an array of the same country
                plt.plot(years,b)#plot the country
            graph()#when all data is colected run graph
        def graph():
            plt.xlabel("Years")
            plt.ylabel("Broadband Cable suscriptions")
            plt.title("Broadband Cable suscriptions by year(2009-2018)")
            plt.legend(va)#add labels and the legend
            scale_factor = 1
            xmin, xmax = plt.xlim()
            plt.xlim((xmin * scale_factor)+1, xmax * scale_factor)#scale the x-axis to look better
            plt.show()

        selfdow_x = 780
        selfdow_y = 720
        tk.Tk.__init__(self)
        self.title("Broard Band Cable Subcriptions per Country")#title of window
        self.geometry("1080x620") #Width x Height of selfdow
        title = tk.Label(self, text="Broard Band Cable Su   bcriptions per Country", fg="Black",font=("Courier", 24))#title in window
        title2 = tk.Label(self, text="Pick countries to Graph", fg="Black",font=("Courier", 18))#subheading
        for y in range(1, len(countries)):
         default = StringVar()

        l = tk.Button(self, text="Start", command=runmakecheck)
        submit = tk.Button(self, text="Submit", command=rungo)
        l.place(x=400, y=400)
        title.place(x=200, y=25)
        title2.place(x=200, y=125)





walls = App()
walls.mainloop()
