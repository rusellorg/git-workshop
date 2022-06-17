import datetime
from dateutil.relativedelta import relativedelta 

def calculate_age_prompt(birth_Dates: list):
    ages = []
    age_prompt = 0
    for i in range(len(birth_Dates)):
        datetime.datetime.strptime(birth_Dates[i], "%d-%m-%Y")
        ages.append(relativedelta(datetime.datetime.now(), datetime.datetime.strptime(birth_Dates[i], "%d-%m-%Y")))

    for i in range(len(ages)):
        age_prompt += ages[i].years
    age_prompt /= len(ages)
    return age_prompt    



