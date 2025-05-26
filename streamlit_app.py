import streamlit as st
import numpy as np
import pandas as pd
st.title('Hello World !')
st.header('say hello', divider='rainbow')

with st.sidebar:
    st.header("About app")
    st.write('this is my first app')
if st.button('say hello'):
    st.write('why hello there')
else:
    st.write('good bye!')

st.markdown('## :red[Objectifs] \n - :rainbow[Comprendre l’écosystème Streamlit.] \n - Savoir installer et lancer une app en quelques secondes. \
\n - Maîtriser les commandes de base pour afficher textes, données, graphiques, médias et widgets.\n - Structurer et optimiser son interface.\n - Déployer une application simple.')

st.subheader('st.columns')
col1, col2 = st.columns(2)
with col1:
    x = st.slider('select a value', 0, 100)
with col2:
    st.write('the value selected is',x) 
    
chart_data = pd.DataFrame(np.random.randn(200,3)*x, columns=['a','b','c'])
st.line_chart(chart_data)
