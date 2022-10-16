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


xls = pd.read_excel('https://github.com/sandy1597/CMSE_830/blob/main/nutrition_1.xlsx')
xls_1=xls.loc[:, ['iso3', 'country','disaggregation','disagg.value','region','adult_anaemia_2000','adult_anaemia_2005','adult_anaemia_2010','adult_anaemia_2019']]
xls_1=xls_1.where(xls_1['disaggregation']=='pregnancy').dropna()
#print(xls_2)

obes=xls.iloc[:,0:24]
obes=obes.where(obes['disaggregation']=='sex').dropna()
obes_male  =obes.where(obes['disagg.value']=='Male').dropna()
obes_female=obes.where(obes['disagg.value']=='Female').dropna()

years_obes=['adult_obesity_2000', 'adult_obesity_2001',
'adult_obesity_2002', 'adult_obesity_2003', 'adult_obesity_2004',
'adult_obesity_2005', 'adult_obesity_2006', 'adult_obesity_2007',
'adult_obesity_2008', 'adult_obesity_2009', 'adult_obesity_2010',
'adult_obesity_2011', 'adult_obesity_2012', 'adult_obesity_2013',
'adult_obesity_2014', 'adult_obesity_2015', 'adult_obesity_2016']

years = [2000,2001,2003,2004,2004,2005,2006,
         2007,2008,2009,2010,2011,2012,2013,
         2014,2015,2016]
years_pd=pd.DataFrame(years,columns=['year'])

countries = obes_male['country'].unique()
#choosing option-1 from the dropdown
# =============================================================================
disease_plots = st.radio(
    "Select the type of disease plot:",
    ('Obesity','Anaemia','Diabetes'))

if(disease_plots=='Anaemia'):
     print(xls_1)
     selected_option_1= st.selectbox("Which attribute do you want to select for x?", xls_1.columns)
     st.write('You selected:', selected_option_1)

# # #choosing option-2 from the dropdown
# =============================================================================
     selected_option_2= st.selectbox("Which attribute do you want to select for y?", xls_1.columns)


     bp_chart=alt.Chart(xls_1).mark_point().encode(
     x=selected_option_1,
     y=selected_option_2,
     color='region',
     ).interactive()

     fig1=st.altair_chart((bp_chart).interactive(),use_container_width=True)


elif(disease_plots=='Obesity'):
    print(obes)
    disease_obesity = st.radio(
        "Select the type of gender:",
        ('Male','Female'))
    if(disease_obesity=='Male'):
      selected_option_3= st.selectbox("Which Country do you want to select for x?",countries)
      st.write('You selected:', selected_option_3)
      new_data =obes_male.where(obes_male["country"]==selected_option_3).dropna()
      print(new_data[years_obes].iloc[0].values)
      k = new_data[years_obes]
      k = k.T
      k["year"] =years
      k.rename(columns={k.columns[0]:"vals"}, inplace=True)
      #selected_option_4= st.selectbox("Which attribute do you want to select for y?", obes.columns)
      bp_chart_1=alt.Chart(k).mark_point().encode(
      x= 'year:N',
      y='vals:Q',
      ).interactive()

      fig2=st.altair_chart((bp_chart_1).interactive(),use_container_width=True)
    
    else:
        selected_option_4= st.selectbox("Which Country do you want to select for x?",countries)
        st.write('You selected:', selected_option_4)
        new_data =obes_female.where(obes_female["country"]==selected_option_4).dropna()
        print(new_data[years_obes].iloc[0].values)
        k = new_data[years_obes]
        k = k.T
        k["year"] =years
        k.rename(columns={k.columns[0]:"vals"}, inplace=True)
        #selected_option_4= st.selectbox("Which attribute do you want to select for y?", obes.columns)
        bp_chart_3=alt.Chart(k).mark_point().encode(
        x= 'year:N',
        y='vals:Q',
        ).interactive()
    
        fig3=st.altair_chart((bp_chart_3).interactive(),use_container_width=True)
    
    
