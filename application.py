import streamlit as st
import pandas as pd
import pickle
import locale

locale.setlocale(locale.LC_ALL, 'en_IN')

# Load trained model
model = pickle.load(open("LinearRegressionModel.pkl", "rb"))

# Load dataset
car = pd.read_csv("Cleaned Car.csv")
car = car.dropna()

# Remove invalid company names
car = car[car['company'].astype(str).str.isalpha()]

# Lists for dropdown
company_list = sorted(car['company'].unique())
fuel_list = sorted(car['fuel_type'].unique())

st.title("🚘 Car Price Predictor")
st.write("Select car details to estimate price")

# Company selection
company = st.selectbox("Company", company_list)

# Filter car names based on selected company
filtered_names = car[car['company'] == company]['name'].unique()
name = st.selectbox("Car Model", sorted(filtered_names))

# Manufacturing year
year = st.number_input(
    "Manufacturing Year",
    min_value=1995,
    max_value=2024
)

# Kilometers driven
kms_driven = st.number_input(
    "Kilometers Driven",
    min_value=0,
    max_value=300000
)

# Fuel type
fuel_type = st.selectbox("Fuel Type", fuel_list)

# Prediction button
if st.button("Predict Price"):

    input_df = pd.DataFrame({
        "name":[name],
        "company":[company],
        "year":[year],
        "kms_driven":[kms_driven],
        "fuel_type":[fuel_type]
    })

    prediction = model.predict(input_df)
    price = int(prediction[0])

    st.markdown(
        f"""
        <div style="
            position:fixed;
            top:60%;
            right:30px;
            transform:translateY(-50%);
            background:linear-gradient(135deg,#FF9933,#FFFFFF,#138808);
            padding:30px;
            border-radius:18px;
            text-align:center;
            color:black;
            box-shadow:0 10px 30px rgba(0,0,0,0.35);
            width:320px;
            z-index:999;
            font-family:Arial, sans-serif;
        ">
            <h3 style="margin-bottom:10px;">🚗 Predicted Price</h3>
            <h1 style="font-size:42px;margin:10px 0;">{locale.currency(price, grouping=True)}</h1>
            <p style="opacity:0.9;">Estimated Market Value</p>
        </div>
        """,
        unsafe_allow_html=True
    )
