import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn')


st.title('Houses')
df = pd.read_csv('housing.csv')

# note that you have to use 0.0 and 40.0 given that the data type of value is float
value_filter = st.slider('median_house_value:', 0,500001, 100000)  # min, max, default

# create a multi select
location_filter = st.sidebar.multiselect(
     'Choose the location type',
     df.ocean_proximity.unique(),  # options
     df.ocean_proximity.unique())  # defaults


# filter by value
df = df[df.median_house_value <= value_filter]

# filter by capital

income_filter = st.sidebar.radio('Choose income level',(
'Low',
'Medium',
'High'
))
df = df[df.ocean_proximity.isin(location_filter)]
if income_filter == 'Low':
    df = df[df.median_income<=2.5]
elif income_filter == 'Medium':
    df = df[(df.median_income>=2.5)&(df.median_income<=4.5)]
else:
    df = df[df.median_income>=4.5]
st.subheader('See more filters in the sidebar :')


# show on map
st.map(df)

# show the plot
st.subheader('histogram of the median house value')
fig, ax = plt.subplots(figsize=(10, 6))
a = df
a.median_house_value.hist(bins = 30)
st.pyplot(fig)
