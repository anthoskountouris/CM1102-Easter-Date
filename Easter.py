#!/usr/bin/python3
import cgi, cgitb
form = cgi.FieldStorage()

def Easter(y): 
    a = y % 19
    b = y // 100 
    c = y%100 
    d = b // 4 
    e=b%4
    g = (8 * b + 13) // 25
    h = (19 * a + b - d - g + 15) % 30
    j = c // 4
    k=c%4
    m = (a + 11 * h) // 319
    r=(2*e+2*j-k-h+m+32)%7 
    n = (h-m + r + 90) // 25
    p = (h-m + r + n + 19) % 32
    return (str(p) + '/' + str(n) + '/' + str(y))


year = int(form.getvalue("Year"))
easterdate = Easter(year)
formatt = form.getvalue("howformat")

splitted=easterdate.split('/')
months=[" ","January","Febuary","March","April","May","June","July","August","September","October","November","December"]
day=splitted[0]
month=months[int(splitted[1])]
years=splitted[2]

if len(day)==1:
    day1="0"+day
else:
    day1=splitted[0]

if len(splitted[1])==1:
    month1="0"+splitted[1]
else:
    month1=splitted[1]

if len(splitted[0])==2:
    if splitted[0]=="11":
        sup="th"
    elif splitted[0]=="12":
        sup="th"
    elif splitted[0]=="13":
        sup="th"
    elif splitted[0][1]=="1":
        sup="st"
    elif splitted[0][1] == "2":
        sup="nd"
    elif splitted[0][1] == "3":
        sup="rd"
    else:
        sup="th"
elif len(splitted[0])==1:
    if splitted[0][0] == "1":
        sup="st"
    elif splitted[0][0] == "2":
        sup="nd"
    elif splitted[0][0] == "3":
        sup="rd"
    else:
        sup="th"

print("Content-Type: text/html; charset=utf-8")
print("")
print("<!DOCTYPE html>")
print("<head>") 
print("<title> Python script for Easter date </title>")
print('<link rel="stylesheet" type="text/css" href="../easter.css">')
print("</head>")
print("<body>")

if formatt == "numerically":
    print("<p class='easter1'>")
    print(f"The Easter date of year {year} is at <span class='east'>{day1}/{month1}/{year}</span>")
    print("</p>")
elif formatt == "verbosely":
    print("<p class='easter2'>")
    print(f"The Easter date of year {year} is at <br/> <span class='east'>{day}<sup>{sup}</sup> of {month} {years}</span>")
    print("</p>")
elif formatt == "both":
    print("<p class='easter3'>")
    print(f"The Easter date of year {year} is at <br/> <span class='east'>{day1}/{month1}/{year}</span>, <span class='east'> {day}<sup>{sup}</sup> of {month} {years}</span>")
    print("</p>")

print("</body>")
print("</html>")

