import streamlit as st
import pandas as pd
import pickle

# Load model
with open("soil_model.pkl", "rb") as f:
    model = pickle.load(f)

# Sidebar
st.sidebar.image("Soil Particles.png", use_column_width=True)
st.sidebar.title("About This App")
st.sidebar.write("""
This app predicts **Soil Category** based on user input features:
- pH
- Moisture
- Organic Matter
- Nitrogen
- Phosphorus
- Potassium
""")

# Main Title
st.title("🌱 Soil Category Predictor")

st.markdown("---")
st.markdown("### Enter Soil Test Values Below:")

# Input Fields
ph = st.number_input("pH", min_value=0.0, help="Acidity or alkalinity of soil")
moisture = st.number_input("Moisture", min_value=0, help="Water content in soil (%)")
organic_matter = st.number_input("Organic Matter", min_value=0.0, help="Organic material in %")
nitrogen = st.number_input("Nitrogen", min_value=0.0, help="Nitrogen level in soil")
phosphorus = st.number_input("Phosphorus", min_value=0.0, help="Phosphorus content")
potassium = st.number_input("Potassium", min_value=0.0, help="Potassium content")

# Predict Button
if st.button("🔍 Predict Soil Category"):
    input_df = pd.DataFrame([[ph, moisture, organic_matter, nitrogen, phosphorus, potassium]],
                            columns=["pH", "Moisture", "Organic_Matter", "Nitrogen", "Phosphorus", "Potassium"])
    prediction = model.predict(input_df)
    st.success(f"🧪 Predicted Soil Category: **{prediction[0]}**")
