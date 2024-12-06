import streamlit as st
# giving title
st.title("BMI Calculator")

# bmi defination and credits
if(st.button("About")):
    st.text("Body Mass Index (BMI) is used as an indicator of body fat content")
    st.text("Made by Yuvraj Gurjar")

# taking weight in kilogram
Weight = st.number_input("Enter weight in kg")

# giving error that weight is non-positive
if(Weight<=0):
    st.info("Enter valid Weight")

# taking height in meters
Height = st.number_input("Enter your height in meters")

# giving error that height is non-positive
if(Height<=0):
    st.info("Enter valid Height")


# calculating BMI using BMI = weight/height^2
try:
    BMI = Weight/(Height**2)
# giving error when height is entered zero
except:
    st.text("Enter valid height")


# check if the Calculate BMI button is pressed
if(st.button("Calculate BMI")):
    # printing BMI value
    st.text("Your BMI is {}.".format(BMI))

    # display the bmi category
    if(BMI<16):
        st.error("Extremely Underweight")
    elif(BMI>=16 and BMI<18.5):
        st.warning("Underweight")
    elif(BMI>=18.5 and BMI<25):
        st.success("Healthy")
    elif(BMI>=25 and BMI<30):
        st.warning("Overweight")
    else:
        st.error("Extremely Overweight")



