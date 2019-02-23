#!/usr/bin/python3
import cgi, cgitb, csv

from datetime import date

form = cgi.FieldStorage()


cgitb.enable() # displays any errors; useful for debugging
form = cgi.FieldStorage()


name = form.getvalue('user_name_input')
email = form.getvalue('user_email_input')
phone_number = int(form.getvalue('user_phone_input'))
message = form.getvalue('user_message_year')


fileObject = open("contact_file.csv","a")
#This code writes the values of each piece in a seperate column
writeFileObject = csv.writer(fileObject)
writeFileObject.writerow([name , email , phone_number , message])
#This closes the file
fileObject.close()

print('Content-Type: text/html; charset=utf-8')
print('')
print('<!DOCTYPE html>')
print('<html>')

print('<head>')
print('<link rel="stylesheet" type="text/css" href="..\stylesheet.css">')
print('<link rel="icon" type="image/png" href="images/Icon.png">')
print('<title> Message Sent! </title>')
print('</head>')

print('<body>')
print('<p>')
print('<center><a href="index.html" class="title">Message Sent</a></center>')
print('<br>')
print('</p>')

print('<footer>')
print('<p>')
print('Ieuan Morris')
print('</p>')
print('<p>')
print('Copyright | 2018')
print('</p>')
print('<br>')
print('</footer>')

print('</body>')

print('</html>')
