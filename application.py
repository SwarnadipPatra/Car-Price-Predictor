import streamlit as st
import pandas as pd
import pickle

model = pickle.load(open("LinearRegressionModel.pkl", "rb"))

car = pd.read_csv("Cleaned Car.csv")
car = car.dropna()

car = car[car['company'].astype(str).str.isalpha()]

company_list = sorted(car['company'].unique())
fuel_list = sorted(car['fuel_type'].unique())

st.title("🚘 Car Price Predictor")
st.write("Select car details to estimate price")

company = st.selectbox("Company", company_list)

filtered_names = car[car['company'] == company]['name'].unique()
name = st.selectbox("Car Model", sorted(filtered_names))

year = st.number_input("Manufacturing Year", min_value=1995, max_value=2026)

kms_driven = st.number_input("Kilometers Driven", min_value=0, max_value=300000)

fuel_type = st.selectbox("Fuel Type", fuel_list)

def format_price(price):
    price = float(price)
    if price >= 10000000:
        return f"{price/10000000:.2f} Cr"
    elif price >= 100000:
        return f"{price/100000:.2f} Lakh"
    else:
        return f"{price:,.0f}"

# Prediction
if st.button("Predict Price"):

    input_df = pd.DataFrame({
        "name": [name],
        "company": [company],
        "year": [year],
        "kms_driven": [kms_driven],
        "fuel_type": [fuel_type]
    })

    prediction = model.predict(input_df)
    price = format_price(prediction[0])

    st.write(f"Estimated Price: ₹ {price}")

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
            <h1 style="font-size:42px;margin:10px 0;">₹ {price}</h1>
            <p style="opacity:0.9;">Estimated Market Value</p>
        </div>
        """,
        unsafe_allow_html=True
    )