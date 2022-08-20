# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 14:35:43 2022

@author: Asim
"""

import streamlit as st
import pandas as pd



def main():
    st.title("Air Passengers Analysis")
    data= pd.read_csv("AirPassengers.csv")
    data["Year"]=data["Month"].apply(lambda x:x.split('-')[0])
    year = st.selectbox('YEAR', data['Year'].unique())
    button=st.button('show results')
    if button :
        subset=data[data["Year"]== year]
        st.table(subset)
    
if __name__=="__main__":
    main()
