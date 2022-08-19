from http.cookies import Morsel
import streamlit as st
import pandas as pd
st.header('THE SILVERSTREAM ACADEMY')
st.image('st 1.jpeg')

st.text_area('LOCATED WITHIN THE HIGHLANDS OF EMBU COUNTY IS A PRODUCTIVE ENVIRONMENT SUITABLE AND FRIENDLY ENVIRONMENT THAT ENABLES YUR CHILD TO GROW AND BECOME PRODUCTIVE IN MANY AREAS')

st.write('LOCATED WITHIN THE HIGHLANDS OF EMBU COUNTY IS A PRODUCTIVE ENVIRONMENT SUITABLE AND FRIENDLY ENVIRONMENT THAT ENABLES YUR CHILD TO GROW AND BECOME PRODUCTIVE IN MANY AREAS')

locations= {"lat":[-0.467277], 
            "lon":[37.450611]}
df = pd.DataFrame(data=locations)
st.map(df) 
st.title('BEEF ANALYTICS')
st.header('school info')
if st.button('more info'):
    st.write('contact')
st.sidebar.write('hi')
