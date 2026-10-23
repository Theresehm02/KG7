import pandas as pd

patients = pd.DataFrame({ 
    "patientid": ["P01", "P02", "P03", "P04", "P05"], 
    "heightcm": [172, 165, 181, 158, 175], 
    "weight_kg": [68, 72, 85, 54, 91] 
    "patientid": ["P01", "P02", "P03", "P04", "P05", "P06"], 
    "heartrate": [72, 88, 105, 64, 112, 79] 
})

bmi = (patients[patients["weight_kg"]]/patients[patients["height(m)"]]^2)
high_hr = patients[patients["heartrate] > 100"]]

print(bmi)

print(high_hr)

