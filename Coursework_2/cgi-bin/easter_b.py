#!/usr/bin/python3
import cgi, cgitb

from datetime import date

form = cgi.FieldStorage()

#year = form.getvalue('user_input_year')

import cgi, cgitb
cgitb.enable() # displays any errors; useful for debugging
form = cgi.FieldStorage()
year_input = int(form.getvalue('user_input_year'))
year = int(year_input)
date_selected = form.getvalue('date_selection')

print_select = str(date_selected)

#Calculates the date for easter based on year input
def calc (year):
    global day, month, numeric_date
    a = year % 19
    b = year // 100
    c = year % 100
    d = (19 * a + b - b // 4 - ((b - (b + 8) // 25 + 1) // 3) + 15) % 30
    e = (32 + 2 * (b % 4) + 2 * (c // 4) - d - (c % 4)) % 7
    f = d + e - 7 * ((a + 11 * d + 22 * e) // 451) + 114
    month = f // 31
    day = f % 31 + 1
    numeric_date = ("The date of easter this year is: " + str(day) + "/" + str(month) + "/" + str(year_input))

#Creates the word date
def word_date(day, month):
    global verbose_date
    if 4 <= day <= 20 or 24 <= day <= 30:
        word_day = str(day)+"th of "
    elif day == 1 or  day == 21  or day == 31:
        word_day = str(day)+"st of "
    elif day == 2  or  day == 22:
        word_day = str(day)+"nd of "
    elif day == 3 or day == 23:
        word_day = str(day)+"rd of "
    else:
        return

    if month == 4:
        word_month = "April "
    elif month == 3:
        word_month = "March "
    else:
        word_month == "May "

    verbose_date = ("The date of easter this year is: " + word_day + word_month + str(year_input))

def print_numeric():
    print('Content-Type: text/html; charset=utf-8')
    print('')
    print('<!DOCTYPE html>')
    print('<html>')
    print('<link rel="stylesheet" type="text/css" href="..\stylesheet.css">')
    print('<head> <title> Easter Date! </title>  </head>')
    print('<body>')
    print('<p>')
    print('<center><a href="https://submission.cs.cf.ac.uk/MorrisIT/exercise2/Easter_Date.html" class="title">Finding Easter</a></center>')
    print('<br>')
    print('<center><p>' + numeric_date + '</p></center>')
    print('</p>')
    print('</body>')

    print('<footer>')
    print('<p>')
    print('Ieuan Morris')
    print('</p>')
    print('<p>')
    print('Copyright | 2018')
    print('</p>')
    print('<br>')
    print('</footer>')

    print('</html>')

def print_verbose():
    print('Content-Type: text/html; charset=utf-8')
    print('')
    print('<!DOCTYPE html>')
    print('<html>')
    print('<link rel="stylesheet" type="text/css" href="..\stylesheet.css">')
    print('<head> <title> Easter Date! </title>  </head>')
    print('<body>')
    print('<p>')
    print('<center><a href="https://submission.cs.cf.ac.uk/MorrisIT/exercise2/Easter_Date.html" class="title">Finding Easter</a></center>')
    print('<br>')
    #print("<p>The date of easter this year is: + str(word_day) + str(word_month) + str(year_input) </p>")
    print('<center><p>' + verbose_date + '</p></center>')
    print('</p>')
    print('</body>')

    print('<footer>')
    print('<p>')
    print('Ieuan Morris')
    print('</p>')
    print('<p>')
    print('Copyright | 2018')
    print('</p>')
    print('<br>')
    print('</footer>')

    print('</html>')

def print_both():
    print('Content-Type: text/html; charset=utf-8')
    print('')
    print('<!DOCTYPE html>')
    print('<html>')
    print('<link rel="stylesheet" type="text/css" href="..\stylesheet.css">')
    print('<head> <title> Easter Date! </title>  </head>')
    print('<body>')
    print('<p>')
    print('<center><a href="https://submission.cs.cf.ac.uk/MorrisIT/exercise2/Easter_Date.html" class="title">Finding Easter</a></center>')
    print('<br>')
    #print("<p>The date of easter this year is: + str(word_day) + str(word_month) + str(year_input) </p>")
    print('<center><p>' + numeric_date + '</p></center>')
    print('<center><p>' + verbose_date + '</p></center>')
    print('</p>')
    print('</body>')

    print('<footer>')
    print('<p>')
    print('Ieuan Morris')
    print('</p>')
    print('<p>')
    print('Copyright | 2018')
    print('</p>')
    print('<br>')
    print('</footer>')

    print('</html>')



calc(year)
word_date(day, month)


if print_select == "numeric_d":
    print_numeric()
elif print_select == "verbose_d":
    print_verbose()
else:
    print_both()
