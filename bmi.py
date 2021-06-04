# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 15:53:18 2021

@author: user
"""
import pandas as pd
import numpy as np



def bmi_processing(df):
    df['HeightM'] = df['HeightCm']/100
    df['BMI'] = round((df.WeightKg / df.HeightM),2)
    
    check = [(df['BMI']<=18.4),
         (25 <= df['BMI']) & (df['BMI'] <= 24.9),
        (25 <= df['BMI']) & (df['BMI'] <= 29.9),
        (30 <= df['BMI']) & (df['BMI'] <= 34.9),
        (35 <= df['BMI']) & (df['BMI'] <= 39.9),
        (df['BMI'] >= 40) 
        ]
    
    values = ['Underweight', 'Normal weight', 'Overweight', 'Moderately obese','Severely obese','Very severely obese']
    df['BMI Category'] = np.select(check, values)
    
    values1 = ['Malnutrition risk', 'Low risk', 'Enhanced risk', 'Medium risk','High risk','Very high risk']
    df['Health risk'] = np.select(check, values1)
    return df    


def count_Overweight(result):
    s = result['BMI Category'].value_counts()
    try:
        print("Count the total number of overweight people:" ,s['Overweight'])
    except:
        print("No entry found")
        
        
# __name__ 
if __name__=="__main__":
    df = pd.read_json (r'data.json')
    result = bmi_processing(df)
    count_Overweight(result)
    