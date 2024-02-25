import pickle
import streamlit as st
import numpy as np

#filename = "heart_disease_prediction.sav"

saved_model = pickle.load(open("C:\\Users\\hp\\Desktop\\Heart disease Prediction\\heart_disease_prediction.sav","rb"))

input_values = (1, 39,  4.0,  0,  0.0,  0.0,  0,  0,  0,  195.0,  106.0,  70.0, 26.97, 80.0, 77.0)
input_values = np.array(input_values).reshape(1,-1)
prediction = saved_model.predict(input_values)

if prediction==0:
    print("Has no heart disease")
else:
    print("Has heart disease")