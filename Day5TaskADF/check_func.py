from sql_app import *
from datetime import date
import re

#validate functions
def f_l_name(fname, lname):
    if len(fname)>0 and len(lname)>0:
        return 1
    else:
        return 0

def age_check(dob):
    string=re.sub("[,./-]"," ",dob).split(" ")
    yeard=int(string[2])
    monthd=int(string[1])
    dayd=int(string[0])
    returnthis = date(yeard, monthd, dayd)
    return returnthis
splitres = age_check(dob)

def agecalc(birthDate):
	today = date.today()
	age = today.year - birthDate.year -((today.month, today.day) < (birthDate.month, birthDate.day))
	return age
age=agecalc(splitres)

def func_gender(gender):
    if gender=="male" or gender=="female":
        return 1
    else:
        return 0

def nation(nationality):
    nationality=nationality.casefold()
    if nationality=="american" or nationality=="indian":
        return 1
    else:
        return 0




