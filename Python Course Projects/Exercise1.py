patient_name = 'John Smith'
patient_age = 20
patient_new = True
if patient_new == True:
    isnew = 'is'

print(f'{patient_name}, is {patient_age} years old and {isnew} a new patient')

import random

patient_new = random.choice([True, False])

if patient_new == True:
    isnew = 'is'
elif patient_new == False:
    isnew = 'is not'

print(f'{patient_name}, is {patient_age} years old and {isnew} a new patient')