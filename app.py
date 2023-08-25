import streamlit as st

st.set_page_config(
    page_title="Copper_Industry_App_Intro",
    page_icon="👋",
)

st.markdown(r"""
    
    # Industrial Copper Modelling Prediction and Leeds Classifcation as Win or Lost 
    # Predictive and Classification of Data

    # 1. Overview
    ---

    The design outlines the development of a web application for price prediction and classification of leads using Copper Industry Dataset. The application will utilize machine learning models that:
    - Predictics the price of the copper per ton based on the paramaters such as thickness, quantity and the application of the copper
    - Classification model predicts whether given order details will turn into company customer future leads convertion won or lost based on the application, selling price, quantity ordered such parameters

    # 2. Motivation
    ---
    Predictive selling price can help company to reduce the shortage of stock and allocate resources according for the production
    
    Classifying the leads conversion will help to get more customers with better negotiation powers for the company with statistical data

    # 3. Success Metrics
    ---
    The success of the price prediction project will be measured based on the following metrics:
    - Precision, recall, lower Mean Squared Error and R Squared Value
    - Better Negotiation of price as per the application and requirement

    The success of the leads classification project will be measured based on the following metrics:
    - Precision, recall, ROC and AUC values
    - More leads conversion as the customer and reduce unnescery resource 

    # 4. Requirements and Constraints
    ---
    ## 4.1 Requirements
    ### 4.1.1. Prediction
    - Get RMSE and R_squared value should have high precision
    ### 4.1.1. Classification
    - Get ROC and AUC should have high value for better classification
    ## 4.2 Constraints
    - The cost of the deployment should be minimal and efficient

    # 5. Methodology
    ---
    ## Data Processing Statistical Analysis
    ---
    - EDA has been done on the data to remove outliers and removing null values
    - OneHotEncoder and Binary Encoder has been used to transform the data
    
    ## Modeling
    ---
    ### Prediction
    - Explored various Machine Learning Models and got better results in XGBoost Regressor with 93 % accuracy
    - 
    ### Classification of Leads in Copper Industry Base on the input data
    - For classification used the Random Forest classifier model
"""
)

