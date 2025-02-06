#  Used Car Price Prediction & Market Analysis

##  Project Overview
In this project, we assumed the role of **Data Analysts** and **Data Scientists** to develop a strategic solution for optimizing used car sales. Using real-world data from second-hand car listings in Spain, we built a **predictive pricing model** with **Azure ML Automated** to estimate the optimal market price of a vehicle based on key attributes such as:

- **Brand**
- **Model**
- **Mileage**
- **Horsepower**
- **Year of manufacture**
- **Location**

Additionally, we conducted **data extraction, preprocessing, exploratory analysis, and visualization** to provide valuable insights into market trends and pricing strategies.

---

## 🔑 Key Project Components

### 1️ ETL & Data Preprocessing
- Cleaned and transformed raw data for accurate analysis.
- Most of the steps in "Model Development Pipeline" where also tested in this process using Python.

### 2️ Exploratory Data Analysis (EDA)
Identified key insights and pricing patterns using:
- **Scatter Plots**
- **Boxplots**
- **Histograms**
- **Hexagonal Diagrams**
- **Line Charts**
- **Correlation Maps**
- **Outlier Analysis & Treatment**

### 3️ Predictive Pricing Model (Azure ML Automated)
Developed a **machine learning model** to estimate vehicle prices based on historical market data.

#### 🔹 Model Development Pipeline: 
- **Upload Data Asset** in Azure ML Studio.
- **Selecting Columns**
- **Clean Missing Data**
- **Normalize Data and Feature Transformation**
  - **OneHotEncoder:** Applied to car brands, converting categorical values into binary representation (resulting in 500 columns).
  - **LabelEncoder:** Used for fuel type and transmission. Assigned unique values (e.g., `1` for **manual**, `2` for **automatic**).
  - **CharGramCountVectorizer:** Split brand names into small character fragments (n-grams) to capture internal patterns.
- **Split Data (Train, Test)**
- **Selecting Regressor**
- **Evaluate Model**

📌 Note: Although we designed and executed the data processing pipeline in Azure ML, all these steps were also developed and tested in Python using libraries such as pandas, scikit-learn, and numpy. This allowed us to validate the results and ensure consistency in preprocessing before integrating it into Azure ML.

![image](https://github.com/user-attachments/assets/853f1ce2-ba0d-4a81-9c26-b375682beb2d)


### 4️ Power BI Dashboard
Designed interactive **visualizations** to support strategic decision-making.
📌 **(Dashboard included in Streamlit App)**

### 5️ Streamlit App (Final Report)
Developed an interactive web application using **Streamlit**, integrating Power BI for visual insights. <br/>
***Deploy URL***: https://secondhandcars-priceprediction-6unveathrc59ywyzqcrhz9.streamlit.app/

---

## 🚀 Technologies Used
- **Python** (Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn)
- **Azure ML Studio** (Automated Machine Learning)
- **Power BI** (Data Visualization)
- **Streamlit** (Web App Development)

---

## 📂 Project Structure
```
├── data/                 # Raw and processed datasets
├── notebooks/            # Jupyter Notebooks for EDA & modeling
├── README.md             # Project documentation
```

---

⚡ *Optimizing used car sales with data-driven insights!*

