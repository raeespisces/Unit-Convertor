import streamlit as st
st.markdown(
    """ 
    <style>
    body {
        background-color: #1e1e2f;
        color: white;
    }
    .stApp { 
        background: linear-gradient(135deg, #bcbcbc, #cfe2f3); 
        padding:30px;
        border-radius: 15px;
        box-shadow: 0px 10px 30px rgba(0, 0, 0, 0.3);
    }
    h1 {
        color: #2b2b3d;
        text-align: center;
        font-size: 36px;
        font-weight: bold;
        text-transform: uppercase;
        letter-spacing: 2px;
        margin-bottom: 30px;
    }
    .stButton {
        background-color: #2b2b3d;
        color: black;
        border: none;
        border-radius: 5px;
        padding: 10px 20px;
        font-size: 18px;
        font-weight: extrabold;
        text-transform: uppercase;
        letter-spacing: 1px;
        cursor: pointer;
    }
    .stButton:hover {
        transform: scale(1.05);
        transition: all 0.3s ease;
        background-color: #4b4b61;
        color: black;
    }
    .resultbox {
        background-color: #2b2b3d;
        font-size: 24px;
        font-weight: bold;
        text-align: center;
        color: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0px 10px 30px rgba(0, 0, 0, 0.3);
    }
    .footer {
        text-align: center;
        color: #2b2b3d;
        font-size: 14px;
        margin-top: 30px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

#title and description
st.markdown("<h1 style='text-align: center ; color: purple;'>Unit  Convertor using Python and Streamlit</h1>", unsafe_allow_html=True)
st.write("<h2 style='text-align: center ; color:rgb(54, 54, 231);'>YOU CAN CONVERT HERE I.E. UNITS OF LENGTH, WEIGHT, AND TEMPERATURE</h2>", unsafe_allow_html=True)

#sidebar menu
conversion_type = st.sidebar.selectbox("SELECT THE CONVERSION TYPE", ["Length", "Weight", "Temperature"])

#input
value = st.number_input("Enter the value", value=0.0, min_value=0.0, step=0.1)
col1, col2 = st.columns(2)

if conversion_type == "Length":
    with col1:
        from_unit = st.selectbox("Form", ["Meters", "Kilometers", "Centimeters", "Milimeters","Miles", "Yards","Inches","Feet"])
    with col2:
        to_unit = st.selectbox("To", ["Meters", "Kilometers", "Centimeters", "Milimeters","Miles", "Yards","Inches","Feet"])

elif conversion_type == "Weight":
    with col1:
        from_unit = st.selectbox("Form", ["Kilograms", "Grams", "Pounds", "Ounces"])
    with col2:
        to_unit = st.selectbox("To", ["Kilograms", "Grams", "Pounds", "Ounces"])

elif conversion_type == "Temperature":
    with col1:
        from_unit = st.selectbox("Form", ["Celsius", "Fahrenheit", "Kelvin"])
    with col2:
        to_unit = st.selectbox("To", ["Celsius", "Fahrenheit", "Kelvin"])

#conversion
def length_conversion(value, from_unit, to_unit):
    length_units = {
        "Meters": 1.0,
        "Kilometers": 1000.0,
        "Centimeters": 100.0,
        "Milimeters": 1000.0,
        "Miles": 1609.34,
        "Yards": 0.9144,
        "Inches": 0.0254,
        "Feet": 0.3048
    }
    return value * length_units[from_unit] / length_units[to_unit]

def weight_conversion(value, from_unit, to_unit):
    weight_units = {
        "Kilograms": 1.0,
        "Grams": 0.001,
        "Pounds": 0.453592,
        "Ounces": 0.0283495,
        "Tonnes": 1000.0,
        "Quintals": 100.0,
        "Stones": 6.35029,
        "Carats": 0.0002,
        "Milligrams": 0.001,
    }
    return value * weight_units[from_unit] / weight_units[to_unit]

#conversion
def temperature_conversion(value, from_unit, to_unit):
    if from_unit == "Celsius" and to_unit == "Fahrenheit":
        return (value * 9/5) + 32
    elif from_unit == "Fahrenheit" and to_unit == "Celsius":
        return (value - 32) * 5/9
    elif from_unit == "Celsius" and to_unit == "Kelvin":
        return value + 273.15
    elif from_unit == "Kelvin" and to_unit == "Celsius":
        return value - 273.15
    elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
        return (value + 459.67) * 5/9
    elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
        return value * 9/5 - 459.67
    else:
        return value

#result
if st.button("Convert"):
    if conversion_type == "Length":
        result = length_conversion(value, from_unit, to_unit)
    elif conversion_type == "Weight":
        result = weight_conversion(value, from_unit, to_unit)
    elif conversion_type == "Temperature":
        result = temperature_conversion(value, from_unit, to_unit)
    st.markdown(f"<div class='resultbox'>Result: {result}</div>", unsafe_allow_html=True)

#footer
st.markdown("<p class='footer'>Made with ❤️ by <a href='https://github.com/raeespisces'>Muhammad Raees Alam</a></p>", unsafe_allow_html=True)






















