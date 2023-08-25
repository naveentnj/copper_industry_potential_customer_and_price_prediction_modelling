import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import LabelBinarizer
import streamlit as st
import re
import config

st.set_page_config(
    layout="wide",
    page_title="Copper_Industry_Price_Prediction",
    page_icon="📈",
)


st.write(config.title, unsafe_allow_html=True)
st.subheader("Prediction of Copper Price Per Ton")

#tab1 = st.tabs(["PREDICT SELLING PRICE"]) 
#with tab1:    
        # Define the possible values for the dropdown menus


# Define the widgets for user input
with st.form("my_form"):
    col1,col2,col3=st.columns([5,2,5])
    with col1:
        st.write(' ')
        status = st.selectbox("Status", config.status_options,key=1)
        item_type = st.selectbox("Item Type", config.item_type_options,key=2)
        country = st.selectbox("Country", sorted(config.country_options),key=3)
        application = st.selectbox("Application", sorted(config.application_options),key=4)
        product_ref = st.selectbox("Product Reference", config.product,key=5)
    with col3:               
        text = "NOTE: Min & Max given for reference, you can enter any value"
        st.write( f'<h5 style="color:rgb(0, 153, 153,0.4);">{text}', unsafe_allow_html=True )
        quantity_tons = st.text_input("Enter Quantity Tons (Min:611728 & Max:1722207579)")
        thickness = st.text_input("Enter thickness (Min:0.18 & Max:400)")
        width = st.text_input("Enter width (Min:1, Max:2990)")
        customer = st.text_input("customer ID (Min:12458, Max:30408185)")
        submit_button = st.form_submit_button(label="PREDICT SELLING PRICE")
        st.markdown("""
            <style>
            div.stButton > button:first-child {
                background-color: #009999;
                color: white;
                width: 100%;
            }
            </style>
        """, unsafe_allow_html=True)

    flag=0 
    pattern = "^(?:\d+|\d*\.\d+)$"
    for i in [quantity_tons,thickness,width,customer]:             
        if re.match(pattern, i):
            pass
        else:                    
            flag=1  
            break
    
if submit_button and flag==1:
    if len(i)==0:
        st.write("please enter a valid number space not allowed")
    else:
        st.write("You have entered an invalid value: ",i)  
        
if submit_button and flag==0:
    
    import pickle
    with open(config.REGRESSION_MODEL_PATH, 'rb') as file:
        loaded_model = pickle.load(file)
    with open(config.REGRESSION_SCALER, 'rb') as f:
        scaler_loaded = pickle.load(f)

    with open(config.REGRESSION_DATA_TRANSFORM, 'rb') as f:
        one_hot_enc_loaded = pickle.load(f)

    with open(config.REGRESSION_BINARY_ENC, 'rb') as f:
        binary_enc_loaded = pickle.load(f)

    new_sample = np.array([[np.log(float(quantity_tons)),application,np.log(float(thickness)), \
                 float(width),country,float(customer),int(product_ref),item_type,status]])
    new_sample_ohe = one_hot_enc_loaded.transform(new_sample[:, [7]]).toarray()
    new_sample_be = binary_enc_loaded.transform(new_sample[:, [8]]).toarray()
    new_sample = np.concatenate((new_sample[:, [0,1,2, 3, 4, 5, 6,]], new_sample_ohe, new_sample_be), axis=1)
    new_sample1 = scaler_loaded.transform(new_sample)
    new_pred = loaded_model.predict(new_sample1)[0]
    st.write('## :green[Predicted selling price:] ', np.exp(new_pred))
