
#from lib2to3.pytree import _Resultd
from ast import If
from asyncore import write
from cgitb import text
from codecs import getencoder
from logging import info
from optparse import Values
from os import rename
from pkgutil import get_data
from unicodedata import name
from http.cookies import Morsel
from unittest import result
import streamlit as st
import pandas as pd
from pandas import ExcelFile
import plotly as px
import numpy as np
import plotly.figure_factory as ff
import matplotlib.pyplot as plp

#---Main Page---
st.set_page_config(page_title='THE SILVERSTREAM ACADEMY')
st.header('THE SILVERSTREAM ACADEMY')
st.title('KCPE results analysis')
st.image('st 1.jpeg')
st.write('The aplication shows and outputs the KCPE results of the students from the year 2018 to 2021.')
st.subheader('ABOUT')
st.write('The Silver Stream academy is a private primary school based in Embu, Kenya. It is a sole propreitorship ownership by Mr. Josphat K.Kathumi and family.')
### --- LOAD DATAFRAME

df_2018 = pd.read_excel('KCPE RESULTS.xlsx', sheet_name='2018')
df_2019 = pd.read_excel('KCPE RESULTS.xlsx', sheet_name='2019')
df_2020 = pd.read_excel('KCPE RESULTS.xlsx', sheet_name='2020')
df_2021 = pd.read_excel('KCPE RESULTS.xlsx', sheet_name='2021')


# Combining all datasets
pdList = [df_2018, df_2019,  df_2020, df_2021]
all_records = pd.concat(pdList)   
df = pdList

st.markdown(
    'The dashboard shows KCPE RESULTS as from 2018 to present')

st.write("They are as follows,")
#----SIDEBAR-----
st.sidebar.header('Filter Here')
#selectbox to select one option at a time
options = st.sidebar.selectbox("select the sheet:",[2018,2019,2020,2021, 'all'])

if options == 2018:
    st.write(df_2018)
elif options == 2019:
    st.write(df_2019)
elif options == 2020:
    st.write(df_2020)
elif options == 2021:
    st.write(df_2021)
else:
    st.write(all_records)
            
#---AVERAGE GENDER RESULTS---
st.write('the graph below shows the average number of the students who have sat for the exam based on their gender')
#gender data data
x1 = np.random.randn(200) - 2
x2 = np.random.randn(200)

# Group data together
hist_data = [x1, x2]

group_labels = ['MALE', 'FEMALE',]

# Create distplot with custom bin_size
fig = ff.create_distplot(
        hist_data, group_labels, bin_size=[.1, .25])

# Plot!
st.plotly_chart(fig, use_container_width=True)
