import numpy as np
import pickle
import pandas as pd

import streamlit as st

pickle_in = open("modle_pickle","rb")
classifier = pickle.load(pickle_in)

def predict_note_authentication(gender, age, smoking, yellow_fingures, anxiety, peer_pressure, chronic_disease, fatigue,
                                        allergy, wheezing, alcohol_consuming, coughing, shortness_of_breath, swalling_defficulty, chest_pain):
    
    prediction = classifier.predict([[gender, age, smoking, yellow_fingures, anxiety, peer_pressure, chronic_disease, fatigue, allergy, wheezing, alcohol_consuming, coughing, shortness_of_breath, swalling_defficulty, chest_pain]])
    print(prediction)
    return prediction



def main():
    st.title("Lung Cancer")
    gender = st.text_input("gender","TextHere")
    age = st.text_input("age","TextHere")
    smoking = st.text_input("smoking","TextHere")
    yellow_fingures = st.text_input("yellow_fingures","TextHere")
    anxiety = st.text_input("anxiety","TextHere")
    peer_pressure = st.text_input("peer_pressure","TextHere")
    chronic_disease = st.text_input("chronic_disease","TextHere")
    fatigue = st.text_input("fatigue","TextHere")
    allergy = st.text_input("allergy","TextHere")
    wheezing = st.text_input("wheezing","TextHere")
    alcohol_consuming = st.text_input("alcohol_consuming","TextHere")
    coughing = st.text_input("coughing","TextHere")
    shortness_of_breath = st.text_input("shortness_of_breath","TextHere")
    swalling_defficulty =st.text_input("swalling_defficulty","TextHere")
    chest_pain = st.text_input("chest_pain","TextHere")
    result = ""
    if st.button("Predict"):
        result = predict_note_authentication(gender, age, smoking, yellow_fingures, anxiety, peer_pressure, chronic_disease, fatigue, allergy, wheezing, alcohol_consuming, coughing, shortness_of_breath, swalling_defficulty, chest_pain)
    st.success("The output is {}" .format(result))
    if st.button("About"):
        st.text("Lets Learn")
        st.text("Build with stream")



if __name__ == "__main__":
    main()