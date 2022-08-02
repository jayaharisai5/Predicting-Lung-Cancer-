import streamlit as st
import pandas as pd

header = st.container()
dataset = st.container()
features = st.container()
modelTrining = st.container()

with header:
    st.title("Welcome to my project... Lung cancer predict")
    st.text("This is the project i am looking for for predect whether he may get cancer or not")



with dataset:
    st.header("Lung Cancer predict dataset")
    st.text("This is the data set i am using.")

    data = pd.read_csv("survey lung cancer.csv")
    st.write(data.head())

with features:
    st.header("The features i created")
    st.text("These are some of the features i have create")

with modelTrining:
    st.header("Time tot trine the model!..")
    st.text("Let's start trining.....")