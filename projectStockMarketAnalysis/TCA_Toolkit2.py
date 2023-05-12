import pandas as pd

def read_data(ticker):
    df = pd.read_csv(ticker)
    df.columns = ['Date', 'Price', 'Open', 'High', 'Low', 'Volume', 'Change %']
    df['Open'] = df['Open'].str.replace(',','')
    df['Open'] = pd.to_numeric(df['Open'], downcast='float')
    df['Date'] = pd.to_datetime(df['Date'])
    df = df.sort_values("Date", ascending= True)
    df = df.set_index("Date")
    return df