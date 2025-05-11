import streamlit as st
from pint import UnitRegistry

# Initialize Pint
ureg = UnitRegistry()
Q_ = ureg.Quantity

st.set_page_config(page_title="Unit Converter", layout="centered")
st.title("🔄Unit Converter")

# Step 1: Define categories and units
unit_categories = {
    "Length": ["meter", "kilometer", "centimeter", "millimeter", "mile", "yard", "foot", "inch"],
    "Mass": ["kilogram", "gram", "milligram", "pound", "ounce", "ton"],
    "Time": ["second", "minute", "hour", "day"],
    "Temperature": ["celsius", "fahrenheit", "kelvin"],
    "Speed": ["meter/second", "kilometer/hour", "mile/hour", "foot/second"]
}

# Step 2: User selects category
category = st.selectbox("**Select category**", list(unit_categories.keys()))

# Step 3: Get units for selected category
units = unit_categories[category]

# Step 4: Input layout
input_value = st.number_input("**Enter value**", value=1.0, format="%.4f")

col1, col2, col3 = st.columns([4, 1, 4])
with col1:
    from_unit = st.selectbox("**From**", units, key="from_unit")

with col2:
    st.markdown("<div style='text-align: center; font-size: 30px; padding-top: 30px;'>=</div>", unsafe_allow_html=True)

with col3:
    to_unit = st.selectbox("**To**", units, key="to_unit")

# Step 5: Perform conversion
try:
    quantity = Q_(input_value, from_unit)
    result = quantity.to(to_unit).magnitude
    st.markdown("---")
    st.subheader("🔁 Converted Value")
    st.success(f"{input_value} {from_unit} = {result:.4f} {to_unit}")
except Exception as e:
    st.error(f"Conversion error: {e}")
