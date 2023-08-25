import pandas as pd
import streamlit as st
st.set_page_config(layout="wide")
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
import plotly.express as px
import numpy as np


if "df1" not in st.session_state:
    st.session_state['df1'] = False

if "df_ready" not in st.session_state:
    st.session_state['df_ready'] = 0
#st.write(config.title, unsafe_allow_html=True)
st.subheader("EDA on data")
# Quantify correlations between features
if st.button('Get the df', key='GetDF'):
    
    dataframe = pd.read_csv(r"data\final_df.csv", low_memory=False)
    st.session_state['df1'] = dataframe
    st.session_state['df_ready'] = 1
if  st.session_state['df_ready'] == 1 :
    dataframe = st.session_state['df1']

    tab1, tab2, tab3, tab4, tab5 = st.tabs(["Mean of the Selling price", "Selling Price Distribution", "Statistics of Continuous Variables", "Q 4", "Correlation variables"])
    with tab1:
        mean_price = dataframe["selling_price"].mean()
        st.markdown(f"""
        What is average Selling Price of Copper?
        {mean_price}
        """)
        fig = px.histogram(dataframe, x="selling_price", y="selling_price", color="item type", marginal="rug",
                    hover_data=dataframe.columns)
        st.plotly_chart(fig)

    with tab2:
        fig = px.violin(dataframe, y="selling_price")
        st.plotly_chart(fig)


    with tab3:
        st.markdown(f"""
        What is Statistics of Continuous Variables?
        {mean_price}
        """)
        dataframe_numbers = dataframe.select_dtypes(include = ['int64','float64'])
        dataframe_numbers.drop(['customer','application'], axis=1)
        dataframe_numbers.head()
        st.dataframe(dataframe_numbers.describe())

    with tab4:
        st.markdown(f"""
        What is Distribution of selling price?
        """)

        fig123, (ax4, ax5) = plt.subplots(1, 2, figsize=(6, 4))
        sns.histplot(
            data=dataframe, x="selling_price", hue="item type", multiple="stack", ax=ax4
        )
        sns.kdeplot(
            data=dataframe, x="selling_price", hue="item type", multiple="stack", ax=ax5
        )
        ax4.set_title("Selling Price Hist Plot")
        ax5.set_title("Selling Price KDE Plot")
        ax5.grid(True)

        fig123.set_tight_layout(True)
        st.pyplot(fig123)

    with tab5:
        st.markdown(f"""
        What is Correlation?
        """)
        x1=dataframe[['quantity tons_log','application','thickness_log','width','selling_price_log','country','customer','product_ref']].corr()
        fig = go.Figure(data=go.Heatmap(
                   x=x1,
                   y=x1,
                   hoverongaps = False))


        
