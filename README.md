# life_expectancy_predictor
# 🌍 Life Expectancy Predictor

A machine learning web app that predicts a country's average life expectancy based on its health and economic indicators, built using the WHO Life Expectancy dataset.

## 📊 About the Project

This project trains and compares multiple regression models to predict life expectancy, then deploys the best-performing model as an interactive Streamlit web app. Users can input various health and economic indicators (like adult mortality, immunization rates, GDP, schooling, etc.) and get an instant life expectancy prediction.

## 🧠 Models Compared

Three regression models were trained and evaluated using MAE, RMSE, and R² score:

- Linear Regression
- Ridge Regression
- Random Forest Regressor

The best-performing model (based on R² score) was selected and saved as the final prediction pipeline.

## 🛠️ Tech Stack

- **Python**
- **scikit-learn** — preprocessing pipeline (imputation, scaling, one-hot encoding) and modeling
- **pandas / numpy** — data handling
- **Streamlit** — web app interface
- **joblib** — model serialization

## 📁 Project Structure

```
├── life_expectancy_pipeline.pkl   # Trained model pipeline
├── app.py                         # Streamlit web app
├── requirements.txt               # Project dependencies
└── README.md
```

## ⚙️ How It Works

1. **Data Cleaning** — Column names stripped, `Country` dropped (193 categories, impractical for one-hot encoding), rows with missing target values removed.
2. **Preprocessing Pipeline** — Numeric features are median-imputed and scaled; the categorical `Status` feature is imputed and one-hot encoded — all handled via `ColumnTransformer` inside a single `Pipeline`.
3. **Model Training** — Data split into train/test sets (80/20) *before* any cleaning is fit, to avoid data leakage.
4. **Model Selection** — All three models are evaluated on the test set, and the pipeline with the highest R² score is saved with `joblib`.
5. **Deployment** — The saved pipeline is loaded into a Streamlit app, where users input feature values through sliders and number inputs to get a live prediction.

## 📈 Input Features

The app takes 20 features as input, including:

- Year, Status (Developed/Developing)
- Adult Mortality, Infant Deaths, Under-Five Deaths
- Alcohol Consumption, BMI
- Immunization rates (Hepatitis B, Polio, Diphtheria)
- Health Expenditure (% and total)
- HIV/AIDS Deaths, Measles Cases
- GDP, Population
- Thinness (ages 5-9 and 10-19)
- Income Composition of Resources, Schooling

## 🚀 Running the App Locally

1. Clone this repository
```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Run the Streamlit app
```bash
streamlit run app.py
```

## 📦 Requirements

```
streamlit
scikit-learn
pandas
numpy
joblib
```

## 📚 Dataset

The model is trained on the [WHO Life Expectancy dataset](https://www.kaggle.com/datasets/kumarajarshi/life-expectancy-who), which contains health, economic, and demographic data for 193 countries from 2000-2015.

## 🙋‍♀️ Author

Shabana
