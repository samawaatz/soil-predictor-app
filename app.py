# Soil Category Predictor App
import streamlit as st
import pickle
import numpy as np

# Load the model
with open("soil_model.pkl", "rb") as f:
    model = pickle.load(f)

# App title and description
st.set_page_config(page_title="Soil Category Predictor", layout="centered")
st.image("Soil Particles.png", use_column_width=True)
st.title("\U0001F331 Soil Category Predictor")
st.markdown("""
    ### Enter Soil Test Values Below:
""")

# Sidebar info
st.sidebar.image("Soil Particles.png")
st.sidebar.markdown("""
**About This App**

This app predicts **Soil Category** based on user input features:
- pH
- Moisture
- Organic Matter
- Nitrogen
- Phosphorus
- Potassium
""")

# Input fields
pH = st.number_input("pH", min_value=0.0, max_value=14.0, step=0.01)
moisture = st.number_input("Moisture", min_value=0.0, step=0.01)
organic_matter = st.number_input("Organic Matter", min_value=0.0, step=0.01)
nitrogen = st.number_input("Nitrogen", min_value=0.0, step=0.01)
phosphorus = st.number_input("Phosphorus", min_value=0.0, step=0.01)
potassium = st.number_input("Potassium", min_value=0.0, step=0.01)

# Prediction button
if st.button("Predict Soil Category"):
    input_data = np.array([[pH, moisture, organic_matter, nitrogen, phosphorus, potassium]])
    prediction = model.predict(input_data)[0]
    st.success(f"Predicted Soil Category: **{prediction}**")
