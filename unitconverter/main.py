import streamlit as st

def unitconverter(value, unitfrom, unitto):
    conversions = {
        "meters_kilometers": 0.001,
        "kilometers_meters": 1000,
        "gram_kilogram": 0.001,
        "kilogram_gram": 1000,
        "liters_gallons": 0.264172,
        "gallons_liters": 3.78541,
    }

    key = f"{unitfrom}_{unitto}"

    if key in conversions:
        conversion = conversions[key]
        if callable(conversion):
            return conversion(value)
        return conversion * value
    else:
        st.error("Invalid unit combination")
        return None

st.title("Unit Converter")

value = st.number_input("Enter the value")
unitfrom = st.selectbox("Convert from:", ["meters", "kilometers", "grams", "kilograms", "liters", "gallons"])
unitto = st.selectbox("Convert to:", ["meters", "kilometers", "grams", "kilograms", "liters", "gallons"])

if st.button("Convert"):
    result = unitconverter(value, unitfrom, unitto)
    if result is not None:
        st.write(f"Converted value: {result}")