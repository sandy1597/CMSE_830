#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 23:07:48 2022

@author: sandeepvemulapalli
"""

import streamlit as st
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import altair as alt


siteHeader = st.container()
dataExploration = st.container()
newFeatures = st.container()

with siteHeader:
    st.title('Welcome to the Awesome Web App!')

with dataExploration:
    st.header('Dataset: Adult Nutrition Country Wise')
    st.text('I found this dataset at GlobalNutrition.org ')

df_data = pd.read_excel('/Users/sandeepvemulapalli/Desktop/CMSE_830/2020_Global_Nutrition_Report_Dataset.xlsx', sheet_name="Country adult")
xls_1   = df_data.iloc[:,0:24]
xls_1   = xls_1.where(xls_1['disaggregation']=='pregnancy').dropna()
xls_2   = xls_1.drop(['iso3','section'],axis=1)
#print(xls_2)

#choosing option-1 from the dropdown

#=============================================================================
# =============================================================================
selected_option_1= st.selectbox("Which attribute do you want to select for x?", xls_2.columns)
st.write('You selected:', selected_option_1)

# # #choosing option-2 from the dropdown
# # 
# =============================================================================
selected_option_2= st.selectbox("Which attribute do you want to select for y?", xls_2.columns)
# st.write('You selected:', selected_option_2)
# # 
# # #selected_option_2= st.selectbox("Which attribute do you want to select for y?", xls_1.columns.iloc[:,0:5])
# # 
# st.header("Joint plot")
# fig=plt.figure(figsize=(9,7))
# # 
# sns.jointplot(data=xls_2,x=xls_2[selected_option_1],y=xls_2[selected_option_2],hue="region")
# # # sns.scatterplot(data=df_data, x=selected_option_1, y=selected_option_2, hue="diagnosis")
# st.pyplot(fig)
# =============================================================================


bp_chart=alt.Chart(xls_2).mark_point().encode(
    x=selected_option_1,
    y=selected_option_2,
    color='region',
).interactive()

st.altair_chart((bp_chart).interactive(),use_container_width=True)



# =============================================================================
# 
# 
# #fig_2=plt.figure(figsize=(11,8))
# st.header("This is a Displot")
# sns.displot(data=df_data,x=selected_option_2,hue="diagnosis",multiple="stack",kind="kde")
# st.pyplot(plt.gcf())
# 
# st.header("This is a Jointplot")
# sns.jointplot(data=df_data,x=selected_option_1,y=selected_option_2,hue="diagnosis")
# st.pyplot(plt.gcf())
# 
# st.header("This is a Jointplot")
# sns.catplot(data=df_data, x=selected_option_1, y="diagnosis",
#     kind="violin", split=True,)
# st.pyplot(plt.gcf())
# =============================================================================
