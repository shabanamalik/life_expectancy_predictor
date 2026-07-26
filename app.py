import streamlit as st
import joblib
import pandas as pd

model = joblib.load('life_expectancy_pipeline.pkl')

st.title("🌍 Life Expectancy Predictor")
st.write("Country ke health/economic indicators daalo, model predict karega average life expectancy")

col1, col2 = st.columns(2)

with col1:
    year = st.number_input("Year", 2000, 2015, 2010)
    status = st.selectbox("Status", ["Developing", "Developed"])
    adult_mortality = st.slider("Adult Mortality (per 1000)", 0, 750, 150)
    infant_deaths = st.slider("Infant Deaths (per 1000)", 0, 150, 20)
    alcohol = st.slider("Alcohol Consumption (litres)", 0.0, 20.0, 5.0)
    percentage_expenditure = st.number_input("Health Expenditure (% of GDP-based)", 0.0, 20000.0, 500.0)
    hepatitis_b = st.slider("Hepatitis B Immunization (%)", 0, 100, 80)
    measles = st.number_input("Measles Cases", 0, 20000, 100)
    bmi = st.slider("Average BMI", 1.0, 80.0, 25.0)
    under_five_deaths = st.slider("Under-Five Deaths (per 1000)", 0, 250, 30)

with col2:
    polio = st.slider("Polio Immunization (%)", 0, 100, 80)
    total_expenditure = st.slider("Total Health Expenditure (% of GDP)", 0.0, 20.0, 6.0)
    diphtheria = st.slider("Diphtheria Immunization (%)", 0, 100, 80)
    hiv_aids = st.slider("HIV/AIDS Deaths (per 1000 births)", 0.0, 50.0, 0.5)
    gdp = st.number_input("GDP per capita", 0.0, 120000.0, 5000.0)
    population = st.number_input("Population", 0.0, 1500000000.0, 10000000.0)
    thinness_1_19 = st.slider("Thinness (10-19 years) %", 0.0, 30.0, 5.0)
    thinness_5_9 = st.slider("Thinness (5-9 years) %", 0.0, 30.0, 5.0)
    income_composition = st.slider("Income Composition of Resources", 0.0, 1.0, 0.6)
    schooling = st.slider("Schooling (years)", 0.0, 22.0, 12.0)

if st.button("Predict Life Expectancy"):
    input_data = pd.DataFrame([[year, status, adult_mortality, infant_deaths, alcohol,
                                  percentage_expenditure, hepatitis_b, measles, bmi,
                                  under_five_deaths, polio, total_expenditure, diphtheria,
                                  hiv_aids, gdp, population, thinness_1_19, thinness_5_9,
                                  income_composition, schooling]],
                                columns=['Year', 'Status', 'Adult Mortality', 'infant deaths',
                                         'Alcohol', 'percentage expenditure', 'Hepatitis B',
                                         'Measles', 'BMI', 'under-five deaths', 'Polio',
                                         'Total expenditure', 'Diphtheria', 'HIV/AIDS', 'GDP',
                                         'Population', 'thinness  1-19 years', 'thinness 5-9 years',
                                         'Income composition of resources', 'Schooling'])

    prediction = model.predict(input_data)[0]
    st.success(f"Predicted Life Expectancy: **{prediction:.1f} years**")
