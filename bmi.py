import pandas as pd

patients = pd.DataFrame({ 
    "patientid": ["P01", "P02", "P03", "P04", "P05"], 
    "heightcm": [172, 165, 181, 158, 175], 
    "weight_kg": [68, 72, 85, 54, 91], 
    "heartrate": [72, 88, 105, 64, 112] 
})

patients["bmi"] = patients["weight_kg"] / (patients["heightcm"] / 100) **2
high_hr = patients[patients["heartrate"] > 100]

print(patients)

print(high_hr)

