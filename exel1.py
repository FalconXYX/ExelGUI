import openpyxl
alpha = ["C","D","E","F","G","H","I","J","K","L"]
years = [2009,2010,2011,2012,2013,2014,2015,2016,2017,2018]
numbers =[1,2,3,4,5,6,7,8,9,10]
countries=[]
variables = []
def countries_exel():
    wb = openpyxl.load_workbook('CableBrodband.xlsx')
    sheet = wb['1'] # Get a sheet from the workbook.
    anotherSheet = wb.active

    for x in range(7, 41):
        thing = str(x)
        a = sheet['A' + thing].value
        countries.append(a)
def year(letter,vari,number):
    vari = []
    wb = openpyxl.load_workbook('CableBrodband.xlsx')
    sheet = wb['1'] # Get a sheet from the workbook.
    anotherSheet = wb.active
    variables.append(vari)
    for x in range(7, 41):
        thing = str(x)
        a = sheet[letter + thing].value
        vari.append(a)


def country(ins, vari):
    index = countries.index(ins)
    vari = []
    for x in range(0,10):
        thing = str(x)
        temp = variables[x]
        vari.append(temp[index])
    print(vari)



countries_exel()
for x in range(0,len(countries)):
    try:
        year(alpha[x],"y"+str(years[x]),numbers[x])
    except:
        pass
input = input("enter country: ")
country(input, input)
