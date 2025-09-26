import streamlit as st

import pickle



st.set_page_config(page_title="Health Insurance Premium Prediction", page_icon=":guardsman:", layout="centered")
st.title("HEALTH INSURANCE PREMIUM PREDICTION")
st.caption("This is a simple web app to predict health insurance premium based on user inputs.")
st.divider()
st.header("Enter the following details:")

col1, col2 = st.columns(2)
with col1:
    age = st.number_input('Age:')
    bmi = st.number_input('BMI:')
    children = st.number_input('Number of Children:')
with col2:
    

    gender = st.selectbox("Select gender:", ('NA','male','female'))
    smoker = st.radio('Smoker (Yes/No):', ('yes','no'))


model = pickle.load(open('model.pkl','rb'))

if st.button('Predict'):
    gender = 0 if gender.upper() == 'MALE' else 1
    smoker = 0 if smoker.upper() == 'NO' else 1
    coustmers = [[age,gender,bmi,children,smoker]]
    yp=str(round(model.predict(coustmers)[0],2))
    st.write("Predicted Premium is: "+yp)

st.divider()
