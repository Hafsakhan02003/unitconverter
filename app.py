import streamlit as st

# Title of the app
st.title("Simple Unit Converter")

# Select unit category
category = st.selectbox("Select Conversion Category:", ["Length", "Weight", "Temperature"])

# Define conversion functions
def convert_length(value, from_unit, to_unit):
    conversions = {
        "Meters": 1,
        "Kilometers": 0.001,
        "Centimeters": 100,
        "Millimeters": 1000,
        "Miles": 0.000621371,
        "Yards": 1.09361,
        "Feet": 3.28084,
        "Inches": 39.3701
    }
    return value * conversions[to_unit] / conversions[from_unit]

def convert_weight(value, from_unit, to_unit):
    conversions = {
        "Kilograms": 1,
        "Grams": 1000,
        "Pounds": 2.20462,
        "Ounces": 35.274
    }
    return value * conversions[to_unit] / conversions[from_unit]

def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    if from_unit == "Celsius":
        return (value * 9/5) + 32 if to_unit == "Fahrenheit" else value + 273.15
    if from_unit == "Fahrenheit":
        return (value - 32) * 5/9 if to_unit == "Celsius" else ((value - 32) * 5/9) + 273.15
    if from_unit == "Kelvin":
        return value - 273.15 if to_unit == "Celsius" else ((value - 273.15) * 9/5) + 32

# Select units and input value
if category == "Length":
    units = ["Meters", "Kilometers", "Centimeters", "Millimeters", "Miles", "Yards", "Feet", "Inches"]
    from_unit = st.selectbox("From:", units)
    to_unit = st.selectbox("To:", units)
    value = st.number_input("Enter value:", min_value=0.0, format="%.4f")
    if st.button("Convert"):
        st.success(f"{value} {from_unit} = {convert_length(value, from_unit, to_unit)} {to_unit}")

elif category == "Weight":
    units = ["Kilograms", "Grams", "Pounds", "Ounces"]
    from_unit = st.selectbox("From:", units)
    to_unit = st.selectbox("To:", units)
    value = st.number_input("Enter value:", min_value=0.0, format="%.4f")
    if st.button("Convert"):
        st.success(f"{value} {from_unit} = {convert_weight(value, from_unit, to_unit)} {to_unit}")

elif category == "Temperature":
    units = ["Celsius", "Fahrenheit", "Kelvin"]
    from_unit = st.selectbox("From:", units)
    to_unit = st.selectbox("To:", units)
    value = st.number_input("Enter value:", format="%.2f")
    if st.button("Convert"):
        st.success(f"{value} {from_unit} = {convert_temperature(value, from_unit, to_unit):.2f} {to_unit}")
