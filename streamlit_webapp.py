
import pickle
import streamlit as st
import numpy as np

saved_model = pickle.load(open("C:\\Users\\hp\\Desktop\\Heart disease Prediction\\heart_disease_prediction.sav","rb"))

def heart_disease_prediction(input_values):
    input_values = np.array(input_values).reshape(1,-1)
    prediction = saved_model.predict(input_values)

    if prediction == 0:
       return "Has no heart disease"
    else:
       return "Has heart disease"

def main():
    st.title("Heart Disease Prediction")

    gender = st.selectbox("Choose your Gender",["Male","Female"])
    if gender == "Male":
        male = 1
    else:
        male = 0

    age = st.number_input("Enter your age")
    education_level = st.selectbox("Education Level",["Secondary","Diploma","Degree","Masters"])

    if education_level == "Secondary":
        education = 1
    elif education_level == "Diploma":
        education = 2
    elif education_level == "Degree":
        education = 3
    elif education_level == "Masters":
        education = 4

    smoking = st.selectbox("Smoking",["Yes","No"])
    if smoking == "Yes":
        currentSmoker = 1
    else:
        currentSmoker = 0

    cigsPerDay = st.number_input("Number of Cigarettes per day")
    BPMeds = st.number_input("BPMeds")
    has_prevalentStroke = st.selectbox("Has prevalentstroke",["Yes","No"])
    if has_prevalentStroke == "Yes":
        prevalentStroke = 1
    else:
        prevalentStroke = 0

    has_prevalentHyp = st.selectbox("Has prevalentHyp",["Yes","No"])
    if has_prevalentHyp == "Yes":
        prevalentHyp = 1
    else:
        prevalentHyp = 0

    has_diabetes = st.selectbox("Has Diabetes",["Yes","No"])
    if has_diabetes == "Yes":
        diabetes = 1
    else:
        diabetes = 0

    totChol = st.number_input("Enter totChol")
    sysBP = st.number_input("Enter sysBP")
    diaBP = st.number_input("Enter diaBP")
    BMI = st.number_input("Enter BMI")
    heartRate = st.number_input("Enter heartRate")
    glucose = st.number_input("Enter Glucose level")
   
    output = ""

    if st.button("Click to predict"):
       input_values = [male, age, education, currentSmoker, cigsPerDay, BPMeds, prevalentStroke, prevalentHyp, diabetes, totChol, sysBP, diaBP, BMI, heartRate, glucose]
       output = heart_disease_prediction(input_values)

    st.write(output)

if __name__ == "__main__":
   main()
   

