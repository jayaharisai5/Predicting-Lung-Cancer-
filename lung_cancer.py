import streamlit as st
import pickle

import pandas as pd

data = pd.read_csv("survey lung cancer.csv")

pickle_in = open("pickle.pkl", "rb")
classifier = pickle.load(pickle_in)

header = st.container()
header_two = st.container()

def prediction(gender, age, smoking, yellow_fingers, anxiety, peer_pressure, chronic_disease, fatigue, allergy, wheezing, alcohol, coughing, shortness_of_breath, swallowing_difficulty, chest_pain):
    predict = classifier.predict([[gender, age, smoking, yellow_fingers, anxiety, peer_pressure, chronic_disease, fatigue, allergy, wheezing, alcohol, coughing, shortness_of_breath, swallowing_difficulty, chest_pain]])
    return predict

with header:
    st.title("LUNG CANCER PREDICTIONS")
    st.text("The effictuveness of cancer prediction system helps the people to ")
    st.text("know their cancer risk with low cost and it also helps the people to take  ")
    st.text("and it also helps the people to take the appropriate decision based on their ")
    st.text("cancer risk status.")

with header_two:
    st.header("Predict your risk from Lung cancer")
    gender = st.text_input("Gender (Female = 0, Male = 1)")
    age = st.text_input("Age (Enter your age)")
    smoking = st.text_input("Smoking (Yes = 2, No = 1)")
    yellow_fingers = st.text_input("Yellow Fingers (Yes = 2, No = 1)")
    anxiety = st.text_input("Anxiety (Yes = 2, No = 1)")
    peer_pressure = st.text_input("Peer Pressure (Yes = 2, No = 1)")
    chronic_disease = st.text_input("Chronic Disease  (Yes = 2, No = 1)")
    fatigue = st.text_input("Fatigue (Yes = 2, No = 1)")
    allergy = st.text_input("Allergy (Yes = 2, No = 1)")
    wheezing = st.text_input("Wheezing (Yes = 2, No = 1)")
    alcohol = st.text_input("Alcohol (Yes = 2, No = 1)")
    coughing = st.text_input("Coughing (Yes = 2, No = 1)")
    shortness_of_breath = st.text_input("Shortness of Breath (Yes = 2, No = 1)")
    swallowing_difficulty = st.text_input("Swallowing Difficulty (Yes = 2, No = 1)")
    chest_pain = st.text_input("Chest Pain (Yes = 2, No = 1)")
    result = ''
    if st.button("Predict"):
        result = prediction(gender, age, smoking, yellow_fingers, anxiety, peer_pressure, chronic_disease, fatigue, allergy, wheezing, alcohol, coughing, shortness_of_breath, swallowing_difficulty, chest_pain)
        if result == 1:
            st.text("there is a chance to get CANCER" + str(result))
        else:
            st.text("No CANCER"+ str(result))
    #st.success("The Output is {} ".format(result))