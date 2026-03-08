# 🚘 Car Price Predictor

A Machine Learning web application that predicts the **price of used cars** based on several features such as company, model, manufacturing year, kilometers driven, and fuel type.

The project uses **Python, Scikit-Learn, Pandas, and Streamlit** to build and deploy an interactive web interface where users can estimate the market value of a car.

---

# 🌐 Live Application

👉 **Open the App:**
APP_LINK

*(Example after deployment: https://car-price-predictor.streamlit.app)*

---

# 📸 Application Screenshot

<img width="1468" height="777" alt="Screenshot 2026-03-08 180922" src="https://github.com/user-attachments/assets/889f568e-dbca-45bc-a917-a28bce5bd42a" />


---

# 📌 Features

* Select **car company**
* Select **car model**
* Enter **manufacturing year**
* Enter **kilometers driven**
* Choose **fuel type**
* Get **instant predicted price**

---

# 🧠 Machine Learning Model

The application uses a **Linear Regression model** trained on a dataset of used cars.

### Steps involved:

1. Data cleaning
2. Removing invalid entries
3. Feature selection
4. One-Hot Encoding for categorical features
5. Training using **Scikit-Learn Linear Regression**
6. Exporting the trained model using **Pickle**

---

# 🛠️ Tech Stack

**Programming Language**

* Python

**Libraries**

* Pandas
* NumPy
* Scikit-Learn
* Streamlit

**Tools**

* Jupyter Notebook
* Git
* GitHub

---

# 📂 Project Structure

```
Car-Price-Predictor
│
├── application.py                # Streamlit web app
├── LinearRegressionModel.pkl     # Trained ML model
├── Cleaned Car.csv               # Cleaned dataset
├── quikr_car.csv                 # Original dataset
├── Car Price Predictor.ipynb     # Model training notebook
├── requirements.txt              # Project dependencies
└── README.md                     # Project documentation
```

---

# 📊 Dataset

The dataset contains information about used cars such as:

* Car name
* Company
* Manufacturing year
* Kilometers driven
* Fuel type
* Price

After preprocessing, the dataset is used to train the regression model.

---

# 🚀 Future Improvements

* Add more car features for better prediction
* Improve model accuracy
* Add car image preview
* Add price comparison charts
* Improve UI design

---

# 👨‍💻 Author

**Swarnadip Patra**

---

