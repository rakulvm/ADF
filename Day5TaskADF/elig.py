from sql_app import *
from check_func import *

#check eligibilities
def func_age_check(gender):
    if gender=="male" and age==21 or gender=="female" and age==18:
        return 1
    else:
        return 0

def nation(nationality):
    nationality=nationality.casefold()
    if nationality=="american" or nationality=="indian":
        return 1
    else:
        return 0

def func_salary(sal):
    if sal>10000 and sal<90000:
        return 1
    else:
        return 0
#Andhra Pradesh, Arunachal Pradesh, Assam, Bihar,  Chhattisgarh,  Karnataka,  Madhya Pradesh,  Odisha,  Tamil Nadu,  Telangana, West Bengal.
def check_state(state):
    states=['andhrapradhesh', 'arunachalpradesh', 'assam','bihar','chhattisgarh','karnataka','madhyapradesh','odisha','tamilnadu','telangana','westbengal']
    state=state.replace(" ","")
    state=state.casefold
    if states.contains(state)
        return 1
    else
        return 0
