# 🚘 Car Price Predictor

A Machine Learning web application that predicts the **price of used cars** based on important factors such as company, model, manufacturing year, kilometers driven, and fuel type.

This project uses **Python, Scikit-Learn, Pandas, and Streamlit** to build an interactive web interface where users can estimate the market value of a car.

---

## 🌐 Live Application

👉 **Open the App:**
APP_LINK

*(Example: https://car-price-predictor.streamlit.app)*

---

## 📸 Application Screenshot

<img width="1468" height="777" alt="Screenshot 2026-03-08 180922" src="https://github.com/user-attachments/assets/81eb12db-88ef-47fc-b096-27e3901a2483" />



---

## 📌 Features

* Select **car company**
* Select **car model**
* Enter **manufacturing year**
* Enter **kilometers driven**
* Choose **fuel type**
* Get **instant predicted price**

---

## 🧠 Machine Learning Model

The application uses a **Linear Regression model** trained on a dataset of used cars.

### Workflow

1. Data cleaning and preprocessing
2. Removing invalid or missing entries
3. Feature selection
4. Encoding categorical variables
5. Training the **Linear Regression model**
6. Saving the trained model using **Pickle**

---

## 🛠️ Tech Stack

**Programming Language**

* Python

**Libraries**

* Pandas
* NumPy
* Scikit-Learn
* Streamlit

**Tools**

* Jupyter Notebook
* GitHub

---

## 📂 Project Structure

```
Car-Price-Predictor
│
├── application.py                # Streamlit web application
├── LinearRegressionModel.pkl     # Trained machine learning model
├── Cleaned Car.csv               # Cleaned dataset
├── quikr_car.csv                 # Original dataset
├── Car Price Predictor.ipynb     # Model training notebook
├── screenshot.png                # Application screenshot
└── README.md                     # Project documentation
```

---

## 📊 Dataset

The dataset contains information about used cars including:

* Car name
* Company
* Manufacturing year
* Kilometers driven
* Fuel type
* Price

After preprocessing, the dataset is used to train the regression model that predicts car prices.

---

## 🚀 Future Improvements

* Improve prediction accuracy
* Add more features for prediction
* Enhance user interface design
* Add car price comparison charts

---

## 👨‍💻 Author

**Swarnadip Patra**

---

⭐ If you found this project useful, consider **starring the repository**.
