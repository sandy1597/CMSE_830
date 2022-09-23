#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 09:30:02 2022

@author: sandeepvemulapalli
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 19:06:15 2022

@author: sandeepvemulapalli
"""

import streamlit as st
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


siteHeader = st.container()
dataExploration = st.container()
newFeatures = st.container()

with siteHeader:
    st.title('Welcome to the Awesome Web App!')

with dataExploration:
    st.header('Dataset: Wisconsin cancer dataset')
    st.text('I found this dataset at Kaggle ')

df_data = pd.read_csv("https://raw.githubusercontent.com/sandy1597/CMSE_830/main/data%202.csv")
print(df_data)
#choosing option-1 from the dropdown

selected_option_1= st.selectbox("Which attribute do you want to select for x?", df_data.columns)
st.write('You selected:', selected_option_1)
#choosing option-2 from the dropdown

selected_option_2= st.selectbox("Which attribute do you want to select for y?", df_data.columns)
st.write('You selected:', selected_option_2)
st.header("Scatter-plot")
fig=plt.figure(figsize=(9,7))
sns.scatterplot(data=df_data, x=selected_option_1, y=selected_option_2, hue="diagnosis")
st.pyplot(fig)


#fig_2=plt.figure(figsize=(11,8))
st.header("This is a Displot")
sns.displot(data=df_data,x=selected_option_2,hue="diagnosis",multiple="stack",kind="kde")
st.pyplot(plt.gcf())

st.header("This is a Jointplot")
sns.jointplot(data=df_data,x=selected_option_1,y=selected_option_2,hue="diagnosis")
st.pyplot(plt.gcf())

st.header("This is a Jointplot")
sns.catplot(data=df_data, x=selected_option_1, y="diagnosis",
    kind="violin", split=True,)
st.pyplot(plt.gcf())

