"""Method"""
from datetime import date
import datetime as dates
import re
import json
import mysql.connector
import config as cfg

HOST1=cfg.information["host"]
USER1=cfg.information["user"]
PASSWD1=cfg.information["passwd"]
DB1=cfg.information["database"]

mydb=mysql.connector.connect(host= HOST1, user=USER1, passwd=PASSWD1, database=DB1)

class Validation():
    """method"""
    @classmethod
    def age_check(cls, birthdate):
        """method"""
        # string = re.sub("[,./-]", " ", dob).split(" ")
        # yeard = int(string[2])
        # monthd = int(string[1])
        # dayd = int(string[0])
        # birthDate = date(yeard, monthd, dayd)
        today = date.today()
        ageof = today.year - birthdate.year - ((today.month, today.day) <
                                               (birthdate.month, birthdate.day))
        return ageof

    @classmethod
    def func_gen_check(cls, gender_1, age_1):
        """method"""
        gender_1=gender_1.casefold()
        if gender_1=="male" and age_1>=21 or gender_1=="female" and age_1>=18:
            return "Eligible"
        if gender_1=="male" and age_1<=20 or gender_1=="female" and age_1<=18:
            return "Not Eligible. Your age is lesser!"
        return "Not Eligible"

    @classmethod
    def nation(cls, n_1):
        """method"""
        n_1=n_1.casefold()
        if "american" in n_1 or "indian" in n_1:
            return "Eligible"
        return "Not Eligible"

    @classmethod
    def func_salary(cls, sal_1):
        """method"""
        if 10000<= sal_1<=90000:
            return "Eligible"
        return "Not Eligible"

    @classmethod
    def check_state(cls, state_1):
        """mehtod"""
        states=['andhrapradhesh', 'arunachalpradesh', 'assam','bihar','chhattisgarh','karnataka',
                'madhyapradesh','odisha','tamilnadu','telangana','westbengal']
        state_1=state_1.replace(' ','')
        state_1=state_1.casefold()
        if state_1 in states:
            return "Eligible"
        return "State is not Eligible!"

    @classmethod
    def fivevalid(cls, days):
        """method"""
        if days > 5:
            return "Eligible"
        return "Last request were must be greater than 5 days"

fname=input("Enter first name:")
mname=input("Enter middle name:")
lname=input("Enter last name:")
dob=input("Enter DOB YYYY-MM-DD ")
dob=dates.datetime.strptime(dob,'%Y-%m-%d')
dob=dob.date()
gender=input("Enter gender:")
nationality=input("Enter nationality:")
city=input("Enter city:")
state=input("Enter state:")
pin=int(input("Enter pincode:"))
q=input("Enter qualification:")
sal=int(input("Enter salary:"))
pan=input("Enter PAN:")
req_date=dates.datetime.now()

mycursor=mydb.cursor()
mycursor.execute("INSERT INTO request_info (Firstname, Middlename, Lastname, Dob, "
                 "Gender, Nationality, City, State, Pincode, Qualification,"
                 " Salary, PanID, request_date)"
                 " VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                 ,(fname, mname, lname, dob, gender, nationality, city, state,
                   pin, q, sal, pan,req_date))
mydb.commit()

mycursor.execute("select request_date from request_info where Request_id ="
                 " (select max(Request_id) "
                 "from request_info group by PanID having PanID='{}')"
                 .format(pan))

value=mycursor.fetchone()
VALUE1=str(value[0].date())
REQ1=str(req_date.date())
print(VALUE1 , REQ1)
STR1=re.split('-',VALUE1)
STR2=re.split('-',REQ1)

val1=int(STR1[0])
val2=int(STR1[1])
val3=int(STR1[2])

val4=int(STR2[0])
val5=int(STR2[1])
val6=int(STR2[2])

d0=date(val1,val2,val3)
d1=date(val4,val5,val6)
days1=(d1-d0).days

print("No of days:",days1)

obj=Validation()

age=obj.age_check(dob)
TEMP=""
FLAG=1

if FLAG==1:
    NEWSTR0=obj.func_gen_check(gender, age)
    if NEWSTR0 != "Eligible":
        FLAG = 0
        TEMP=NEWSTR0
if FLAG==1:
    NEWSTR1=obj.nation(nationality)
    if NEWSTR1 != "Eligible":
        FLAG=0
        TEMP = NEWSTR1
if FLAG==1:
    NEWSTR2=obj.func_salary(sal)
    if NEWSTR2 != "Eligible":
        FLAG=0
        TEMP = NEWSTR2
if FLAG==1:
    STR3=obj.check_state(state)
    if STR3 != "Eligible":
        FLAG=0
        TEMP = STR3
if FLAG==1:
    STR4=obj.fivevalid(days1)
    if STR4 != "Eligible":
        FLAG=0
        TEMP = STR4

mycursor.execute("select max(Request_id) from request_info")
rid=mycursor.fetchone()
request_id=int(rid[0])

if FLAG==1:
    RESPONSE="Success"
    diction={"Request_id":request_id,"Response":RESPONSE}
    dictation=json.dumps(diction)
    print(dictation)
    mycursor.execute("INSERT INTO response_info(Request_id,response) "
                     "VALUES ('{}','{}')".format(request_id,dictation))
    mydb.commit()
else:
    RESPONSE="Failure"
    diction = {"Request_id": request_id, "Response": RESPONSE,"Reason":TEMP}
    dictation = json.dumps(diction)
    print(dictation)
    mycursor.execute("INSERT INTO response_info(Request_id,response) "
                     "VALUES ('{}','{}')".format(request_id, dictation))
    mydb.commit()
# Delete records
# mycursor=mydb.cursor()
# sqlform="Delete from request_info where FirstName='rakul'"
# mycursor.execute(sqlform)
# mydb.commit()
mycursor.execute("select * from request_info")
for db in mycursor:
    print(db)
