import streamlit
import pandas as pd
from PIL import Image
streamlit.write("""
# Stock market web application
""")

streamlit.header('**Visually** show data on a stock. Date from 23.03.2020 - 22.03.2021')
streamlit.write('List of available stocks: APPL, AMZN, TSLA' )


image = Image.open("/path/to/img")
streamlit.image(image, use_column_width=True)

#Creating a sidebar header
streamlit.sidebar.header('User Input: ')

#Creating a function to get the users input
def get_input():

    stock_symbol = streamlit.sidebar.text_input("Stock symbol: ", "AMZN")
    return stock_symbol

#Creating a function to get the company name
def get_company_name(symbol):
    """
    
    """
    if symbol == 'AMZN':
        return 'Amazon'
    elif symbol == 'TSLA':
        return 'Tesla'
    elif symbol == 'AAPL':
        return 'Apple'
    else:
        'None'

#Creating a function to get the proper company data and the proper timeframe from
# the user start date to the users end date
def get_data(symbol):
    """
    
    """
    
    #Loading the data
    if symbol.upper() == 'AMZN':
        df = pd.read_csv("/path/to/img")
    elif symbol.upper() == 'TSLA':
        df = pd.read_csv("/path/to/img")
    elif symbol.upper() == 'AAPL':
        df = pd.read_csv("/path/to/img")
    else:
        df = pd.DataFrame(columns = ['Date', 'Close', 'Open', 'Volume', 'Adj Close', 'High', 'Low'])

    # Getting the data range

    #start['Date'] = pd.to_datetime(start)
    #end['Date'] = pd.to_datatime(df)

    # Setting the start and end index rows both to 0
    #start_row = 0
    #end_row = 0

    # Start the date from the top of the data set and go down to see if the users start date is
    # less than or equal to the date in the data set
    #for i in range(0, len(df)):
    #    if start < pd.to_datetime(df['Date'][i]):
    #        start_row = i
    #        break

    # Starting from the bottom of the dataset and go up to see if the users end date
    # is greater than or equal to the date in the dataset
    #for j in range(0, len(df)):
    #    if end >= pd.to_datetime(df['Date'][len(df)-1-j]):
    #        end_row = len(df) -1 -j
    #        break

    # Setting the index to be the date
    df = df.set_index(pd.DatetimeIndex(df['Date'].values))

    return df.iloc[:]

# Getting the users input
symbol = get_input()

# Getting the data
df = get_data(symbol)

# Getting the company name
company_name = get_company_name(symbol.upper())

# Displaying the close price
streamlit.header(company_name + " Close Price\n")
streamlit.line_chart(df['Close'])

# Displaying the volume
streamlit.header(company_name + " Volume\n")
streamlit.line_chart(df['Volume'])

# Getting statistics on the data
streamlit.header("Data Statistics")
streamlit.write(df.describe())

