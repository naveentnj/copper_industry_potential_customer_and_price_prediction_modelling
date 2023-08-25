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
st.set_page_config(layout="wide")

st.write(config.title, unsafe_allow_html=True)
st.subheader("Leads Conversion Prediction")

tab1 = st.tabs(["PREDICT STATUS"]) 
item_type_options = ['W', 'WI', 'S', 'Others', 'PL', 'IPL', 'SLAWR']

            
#with tab1: 
    
with st.form("my_form1"):
    col1,col2,col3=st.columns([5,1,5])
    with col1:
        cquantity_tons = st.text_input("Enter Quantity Tons (Min:611728 & Max:1722207579)")
        cthickness = st.text_input("Enter thickness (Min:0.18 & Max:400)")
        cwidth = st.text_input("Enter width (Min:1, Max:2990)")
        ccustomer = st.text_input("customer ID (Min:12458, Max:30408185)")
        cselling = st.text_input("Selling Price (Min:1, Max:100001015)") 
        
    with col3:    
        st.write(' ')
        citem_type = st.selectbox("Item Type", item_type_options,key=21)
        ccountry = st.selectbox("Country", sorted(config.country_options),key=31)
        capplication = st.selectbox("Application", sorted(config.application_options),key=41)  
        cproduct_ref = st.selectbox("Product Reference", config.product,key=51)           
        csubmit_button = st.form_submit_button(label="PREDICT STATUS")

    cflag=0 
    pattern = "^(?:\d+|\d*\.\d+)$"
    for k in [cquantity_tons,cthickness,cwidth,ccustomer,cselling]:             
        if re.match(pattern, k):
            pass
        else:                    
            cflag=1  
            break
    
if csubmit_button and cflag==1:
    if len(k)==0:
        st.write("please enter a valid number space not allowed")
    else:
        st.write("You have entered an invalid value: ",k)  
        
if csubmit_button and cflag==0:
    import pickle
    with open(config.CLASSIFICATION_MODEL_PATH, 'rb') as file:
        cloaded_model = pickle.load(file)

    with open(config.CLASSIFICATION_SCALER, 'rb') as f:
        cscaler_loaded = pickle.load(f)

    with open(config.CLASSIFICATION_DATA_TRANSFORM, 'rb') as f:
        ct_loaded = pickle.load(f)

    # Predict the status for a new sample
    # 'quantity tons_log', 'selling_price_log','application', 'thickness_log', 'width','country','customer','product_ref']].values, X_ohe
    new_sample = np.array([[np.log(float(cquantity_tons)), np.log(float(cselling)), capplication, np.log(float(cthickness)),float(cwidth),ccountry,int(ccustomer),int(cproduct_ref),citem_type]])
    new_sample_ohe = ct_loaded.transform(new_sample[:, [8]]).toarray()
    new_sample = np.concatenate((new_sample[:, [0,1,2, 3, 4, 5, 6,7]], new_sample_ohe), axis=1)
    new_sample = cscaler_loaded.transform(new_sample)
    new_pred = cloaded_model.predict(new_sample)
    if new_pred==1:
        st.write('## :green[The Status is Won] ')
    else:
        st.write('## :red[The status is Lost] ')
        

