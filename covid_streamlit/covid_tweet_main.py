# -*- coding: utf-8 -*-

#https://www.hackerearth.com/practice/
#https://amueller.github.io/word_cloud/auto_examples/colored_by_group.html

import prediction
import mywordcloud
import heatmap
import dataframe
import sentiment
import home_page
import streamlit as st

#add home page

hide_menu = """
<style>
#MainMenu{
    visibility:hidden;
}

    
footer:before{
    content: 'Created by Team 68: Arianna Cooper, Yoseph Dawit, Funke Olaleye and Suzan Pham';
    display: block;
    position:relative;
    color: white;
}
    
</style>
"""


pages = {'About':home_page, 'DataFrame':dataframe, 'Sentiment':sentiment, 'WordCloud':mywordcloud, 'Heatmap':heatmap, 'Prediction':prediction}

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


st.sidebar.title('App Navigation')

selection = st.sidebar.selectbox('Options', list(pages.keys()))

page = pages[selection]
page.app()

st.markdown(hide_menu, unsafe_allow_html = True)
