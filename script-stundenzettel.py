import calendar 
from fillpdf import fillpdfs

from datetime import date
 
 
def numOfDays(date1, date2):
  #check which date is greater to avoid days output in -ve number
    if date2 > date1:   
        return (date2-date1).days
    else:
        return (date1-date2).days
 
 
# Driver program
date1 = date(2015, 2, 14)
date2 = date(2015, 2, 25)
print(numOfDays(date1, date2), "days")

form_fields=list(fillpdfs.get_form_fields('stundenzettel_mindestlohngesetz.pdf').keys())

print(len(form_fields))

print('type in the month you want to fill out (mm)')
Monat= input()

print('type in the year (yyyy)')
Jahr=input()

Monat_Jahr=Monat+'/'+Jahr

#if Monat_Jahr == '04/'
#data_dict={
#    form_fields[4]: Monat_Jahr
#}

fillpdfs.write_fillable_pdf('stundenzettel_mindestlohngesetz.pdf', 'filled_out.pdf', data_dict)

print(form_fields)