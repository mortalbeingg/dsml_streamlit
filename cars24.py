import streamlit as st
import pandas as pd
import datetime
import pickle
 
carsdf= pd.read_csv('cars24price.csv')
st.dataframe(carsdf.head(5))

col1,col2= st.columns(2)
fuel_type= col1.selectbox('Select the fuel type',
                          ['Diesel','Petrol','CNG','LPG','Electric'])

seller_type= col1.selectbox('Select the seller type',
                            ['Dealer','Individual'])

engine= col1.slider('Select the enginer power',
                    500,5000,step=100)

transmission_type= col2.selectbox("Select the type of transmission",
                                  ['Manual','Automatic'])

seats= col2.selectbox('Select the number of seats',
                      [4,5,6,7])


encodedict= {
    "fuel_type":{'Diesel':1, 'Petrol':2,'CNG':3, 'LPG':4, 'Electric':5},
    "seller_type":{'Dealer':1,'Individual':2},
    "transmission_type":{'Manual':1, 'Automatic':2}
}

def modelpredict(fuel_type, transmission_type, engine, seats):

    ##loading the model
    with open(".\car_pred",'rb') as file:
        model=pickle.load(file)
    
    ipfeatures=[[2018.0,seller_type,40000,fuel_type, transmission_type,19.70, engine, 86, seats]]
    return model.predict(ipfeatures)


if (st.button('Predict price of the car')):
    seller_type=encodedict['seller_type'][seller_type]
    fuel_type=encodedict['fuel_type'][fuel_type]
    transmission_type=encodedict['transmission_type'][transmission_type]

    price= modelpredict(seller_type,fuel_type,transmission_type, seats)
    st.text('Predited price of the car is'+str(price))
