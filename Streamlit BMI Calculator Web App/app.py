import streamlit as st

st.title("BMI Calculator")

height = st.slider("Enter Your Height (in cm):", 100, 300, 200)
weight = st.slider("Enter Your Weight (in kg):", 20, 150, 85)
bmi = weight / ((height/100) ** 2)

st.write(f"Your BMI is {bmi:.2f}")
st.write("### BMI Categories ###")
st.write("- Underweight: BMI Less than 18.5")
st.write("- Normal weight: BMI between 18.5 and 24.9")
st.write("- Overweight: BMI between 25 and 29.9")
st.write("- Obesity: BMI 30 or Greater")