# Core Pkgs
import streamlit as st 
from JobRecommendation.side_logo import add_logo
from JobRecommendation.sidebar import sidebar
import altair as alt

from streamlit_extras.switch_page_button import switch_page
from JobRecommendation.lottie_animation import load_lottieurl
# EDA Pkgs
import pandas as pd 
import numpy as np 
from datetime import datetime
from streamlit_lottie import st_lottie


st.set_page_config(layout="centered", page_icon='logo/logo2.png', page_title="HOMEPAGE")



url = load_lottieurl("https://assets5.lottiefiles.com/private_files/lf30_m075yjya.json")

add_logo()
sidebar()


st.markdown("<h1 style='text-align: center; font-family: Verdana, sans-serif; padding: 20px; border: 2px solid #758283; border-radius: 5px;'>Welcome to MMCOE Resume Score !</h1>", unsafe_allow_html=True)

st.markdown("<div style='background-color: rgba(255, 0, 0, 0); padding: 10px;'>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; font-family: Verdana, sans-serif; padding: 20px;'>Pune </h2>", unsafe_allow_html=True)

s1,s2, s3,s4 = st.columns(4)


with s1:
        analyzer = st.button("Resume Analyzer")
        if analyzer:
            switch_page("resume analyzer")
        st.balloons()

with s2:
        candidate = st.button("ASK GEMINI")
        if candidate:
            switch_page("gemini")
        st.balloons()

st.markdown("</div>", unsafe_allow_html=True)
st_lottie(url)

# Project Description Section

footer_container = st.container()

# Add content to the footer container
