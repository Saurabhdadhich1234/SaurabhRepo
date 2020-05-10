# This program predicts stock prices by using machine learning tools
# Install the dependencies
import quandl
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
from sklearn.model_selection import train_test_split

# Get the stock data

df =quandl.get("WIKI/FB")
# Take a look at the data
print(df.head)

# Get the Adjusted close pricet  y 
df=df[['Adj.Close']]
#Take a look at the new data
print(df.head())

# A variable for predicting 'n' days out in future
forecast_out =1
# Cret another column(the target or dependent variable) shifted 'n' units up
df['Prediction']=df[['Adj.Close']].shift(-1)
#print the new data set
print(df.head())