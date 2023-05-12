import pandas as pd
import numpy as np
import pickle
from sklearn import *
import streamlit as st

df = pickle.load(open('df.pkl','rb'))
model = pickle.load(open('rf.pkl','rb'))

st.title('Laptop Price Prediction')
st.header('Fill details to predict price of Laptop')

# Features
# ['Company', 'TypeName', 'Ram', 'Weight', 'Price', 'Touchscreen', 'Ips',
    #    'Cpu brand', 'HDD', 'SSD', 'Gpu brand', 'os']

# Features
company = st.selectbox('Company',df['Company'].unique())
typename  = st.selectbox('TypeName',df['TypeName'].unique())
ram = st.selectbox('RAM(in GB)', [8, 16,  4,  2, 12,  6, 32, 24, 64])
weight = st.number_input('Weight of the laptop')
touchscreen = st.selectbox('TouchScreen',['Yes','No'])
ips = st.selectbox('IPS',['Yes','No'])
cpu = st.selectbox('CPU brand',df['Cpu brand'].unique())
hdd = st.selectbox('HDD',[0,500,1000,2000,32, 128])
ssd = st.selectbox('SSD',[128, 0, 256, 512, 32, 64,1000, 1024, 16, 768,180,240,8])
gpu = st.selectbox('GPU brand',df['Gpu brand'].unique())
os = st.selectbox('OS',df['os'].unique())


if st.button('Predict Laptop Price'):
    if touchscreen=="Yes":
        touchscreen=1
    else:
        touchscreen=0
    if ips=="Yes":
        ips=1
    else:
        ips=0
    test_data = np.array([company,typename,ram,weight,touchscreen,ips,cpu,hdd,ssd,gpu,os])
    test_data = test_data.reshape([1,11])

    st.success(model.predict(test_data)[0])