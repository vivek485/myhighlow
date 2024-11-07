

import pandas as pd


from datetime import datetime, timedelta
from datetime import date
import numpy as np
import time
import ta
from ta.momentum import stoch
import asyncio
import aiohttp
import io
import nest_asyncio
from ta.volatility import keltner_channel_hband , keltner_channel_lband, keltner_channel_mband
from ta.trend import macd, macd_diff
import streamlit as st

st.set_page_config(layout="wide")
st.title('Stock Trading Open High Low my version 200ma crossing')



s = ['CUMMINSIND',
     'ZEEL',
     'TRENT',
     'HAL',
     'PIIND',
     'TATACOMM',
     'TATAPOWER',
     'MFSL',
     'SBIN',
     'BANKBARODA',
     'ALKEM',
     'IOC',
     'BPCL',
     'OFSS',
     'CANBK',
     'POWERGRID',
     'CONCOR',
     'VOLTAS',
     'OBEROIRLTY',
     'BEL',
     'MCX',
     'NAUKRI',
     'COALINDIA',
     'PAGEIND',
     'HINDALCO',
     'ZYDUSLIFE',
     'PVRINOX',
     'TCS',
     'HCLTECH',
     'RELIANCE',
     'CUB',
     'LUPIN',
     'AUROPHARMA',
     'INDUSTOWER',
     'BAJAJ-AUTO',
     'GAIL',
     'ONGC',
     'APOLLOHOSP',
     'LICHSGFIN',
     'BOSCHLTD',
     'ACC',
     'BSOFT',
     'MPHASIS',
     'HINDPETRO',
     'DLF',
     'BHARTIARTL',
     'PNB',
     'NTPC',
     'NMDC',
     'HEROMOTOCO',
     'INDIGO',
     'COFORGE',
     'INDIAMART',
     'ESCORTS',
     'INDHOTEL',
     'SRF',
     'ABCAPITAL',
     'SUNPHARMA',
     'RECLTD',
     'LTTS',
     'DRREDDY',
     'MRF',
     'SBICARD',
     'BHARATFORG',
     'SUNTV',
     'HDFCAMC',
     'INFY',
     'HAVELLS',
     'BHEL',
     'NATIONALUM',
     'TORNTPHARM',
     'CROMPTON',
     'ICICIGI',
     'JUBLFOOD',
     'GUJGASLTD',
     'MCDOWELL-N',
     'JINDALSTEL',
     'PFC',
     'EXIDEIND',
     'BATAINDIA',
     'IEX',
     'TATASTEEL',
     'HINDUNILVR',
     'LTIM',
     'GMRINFRA',
     'NAVINFLUOR',
     'COROMANDEL',
     'PERSISTENT',
     'ASTRAL',
     'TITAN',
     'IPCALAB',
     'TECHM',
     'ADANIPORTS',
     'DABUR',
     'LAURUSLABS',
     'BANDHANBNK',
     'MARICO',
     'MGL',
     'IRCTC',
     'SIEMENS',
     'SBILIFE',
     'TATAMOTORS',
     'DIXON',
     'IDEA',
     'CIPLA',
     'INDIACEM',
     'ASHOKLEY',
     'AMBUJACEM',
     'DEEPAKNTR',
     'LT',
     'TVSMOTOR',
     'ABFRL',
     'DIVISLAB',
     'VEDL',
     'BAJAJFINSV',
     'BERGEPAINT',
     'WIPRO',
     'UBL',
     'POLYCAB',
     'FEDERALBNK',
     'L&TFH',
     'BIOCON',
     'BALKRISIND',
     'TATACHEM',
     'PETRONET',
     'M&MFIN',
     'ABBOTINDIA',
     'ADANIENT',
     'HDFCBANK',
     'GODREJCP',
     'ASIANPAINT',
     'RBLBANK',
     'M&M',
     'MARUTI',
     'JSWSTEEL',
     'ICICIPRULI',
     'ATUL',
     'COLPAL',
     'BAJFINANCE',
     'APOLLOTYRE',
     'MOTHERSON',
     'GRANULES',
     'RAMCOCEM',
     'IGL',
     'GRASIM',
     'IDFC',
     'ULTRACEMCO',
     'GLENMARK',
     'SYNGENE',
     'INDUSINDBK',
     'TATACONSUM',
     'HDFCLIFE',
     'HINDCOPPER',
     'SHREECEM',
     'SHRIRAMFIN',
     'CHOLAFIN',
     'GNFC',
     'PIDILITIND',
     'BALRAMCHIN',
     'IDFCFIRSTB',
     'DALBHARAT',
     'JKCEMENT',
     'ABB',
     'UPL',
     'SAIL',
     'ICICIBANK',
     'EICHERMOT',
     'NESTLEIND',
     'AXISBANK',
     'BRITANNIA',
     'GODREJPROP',
     'MANAPPURAM',
     'LALPATHLAB',
     'AUBANK',
     'KOTAKBANK',
     'PEL',
     'CHAMBLFERT',
     'CANFINHOME',
     'ITC',
     'MUTHOOTFIN',
     'AARTIIND',
     'DELTACORP',
     'METROPOLIS']

symbol200 = ['BDL',
             'CUMMINSIND',
             'ZEEL',
             'LICI',
             'TRENT',
             'OIL',
             'MANKIND',
             'HAL',
             'MAXHEALTH',
             'TORNTPOWER',
             'PIIND',
             'TATACOMM',
             'TATAPOWER',
             'MFSL',
             'SBIN',
             'BANKBARODA',
             'ALKEM',
             'IOC',
             'BPCL',
             'BANKINDIA',
             'CANBK',
             'KPITTECH',
             'JSWENERGY',
             'POWERGRID',
             'CONCOR',
             'VOLTAS',
             'OBEROIRLTY',
             'VBL',
             'UNIONBANK',
             'MSUMI',
             'BEL',
             'NAUKRI',
             'COALINDIA',
             'PAGEIND',
             'PATANJALI',
             'HINDALCO',
             'ZYDUSLIFE',
             'INDIANB',
             'MAZDOCK',
             'TCS',
             'HCLTECH',
             'ZOMATO',
             'RELIANCE',
             'LUPIN',
             'AUROPHARMA',
             'INDUSTOWER',
             'BAJAJ-AUTO',
             'GAIL',
             'APOLLOHOSP',
             'ONGC',
             'LICHSGFIN',
             'BOSCHLTD',
             'ACC',
             'BAJAJHLDNG',
             'MPHASIS',
             'YESBANK',
             'HINDPETRO',
             'DLF',
             'BHARTIARTL',
             'PNB',
             'NTPC',
             'NMDC',
             'HEROMOTOCO',
             'INDIGO',
             'DMART',
             'COFORGE',
             'INDHOTEL',
             'ESCORTS',
             'ABCAPITAL',
             'SRF',
             'SUNPHARMA',
             'RECLTD',
             'LTTS',
             'DRREDDY',
             'MRF',
             'SUNTV',
             'RVNL',
             'BHARATFORG',
             'SBICARD',
             'HDFCAMC',
             'INFY',
             'APLAPOLLO',
             'POLICYBZR',
             'HAVELLS',
             'BHEL',
             'TORNTPHARM',
             'CROMPTON',
             'ICICIGI',
             'JUBLFOOD',
             'GUJGASLTD',
             'IRFC',
             'MCDOWELL-N',
             'JINDALSTEL',
             'NHPC',
             'PFC',
             'BATAINDIA',
             'TATASTEEL',
             'HINDUNILVR',
             'LTIM',
             'NAVINFLUOR',
             'COROMANDEL',
             'PERSISTENT',
             'ASTRAL',
             'TITAN',
             'TECHM',
             'IPCALAB',
             'ADANIPORTS',
             'DABUR',
             'LAURUSLABS',
             'BANDHANBNK',
             'MARICO',
             'TATAELXSI',
             'IRCTC',
             'SIEMENS',
             'SBILIFE',
             'PGHH',
             'PRESTIGE',
             'TATAMOTORS',
             'DIXON',
             'FACT',
             'IDEA',
             'ADANIPOWER',
             'CIPLA',
             'ASHOKLEY',
             'TATAMTRDVR',
             'DEEPAKNTR',
             'AMBUJACEM',
             'LT',
             'TVSMOTOR',
             'DEVYANI',
             'ABFRL',
             'DIVISLAB',
             'VEDL',
             'BAJAJFINSV',
             'POONAWALLA',
             'BERGEPAINT',
             'WIPRO',
             'UBL',
             'POLYCAB',
             'FEDERALBNK',
             'L&TFH',
             'BIOCON',
             'BALKRISIND',
             'ATGL',
             'TATACHEM',
             'M&MFIN',
             'PETRONET',
             'CGPOWER',
             'ADANIENT',
             'HDFCBANK',
             'ASIANPAINT',
             'GODREJCP',
             'AWL',
             'M&M',
             'MARUTI',
             'JSWSTEEL',
             'ADANIENSOL',
             'ICICIPRULI',
             'COLPAL',
             'APOLLOTYRE',
             'BAJFINANCE',
             'FORTIS',
             'DELHIVERY',
             'MOTHERSON',
             'RAMCOCEM',
             'ADANIGREEN',
             'IGL',
             'GRASIM',
             'ULTRACEMCO',
             'GLAND',
             'SYNGENE',
             'INDUSINDBK',
             'TATACONSUM',
             'SHREECEM',
             'HDFCLIFE',
             'SHRIRAMFIN',
             'CHOLAFIN',
             'PIDILITIND',
             'IDFCFIRSTB',
             'ITC',
             'DALBHARAT',
             'LODHA',
             'ABB',
             'UPL',
             'TIINDIA',
             'SONACOMS',
             'SAIL',
             'NYKAA',
             'ICICIBANK',
             'EICHERMOT',
             'NESTLEIND',
             'AXISBANK',
             'FLUOROCHEM',
             'BRITANNIA',
             'GODREJPROP',
             'LALPATHLAB',
             'AUBANK',
             'KOTAKBANK',
             'PEL',
             'MUTHOOTFIN',
             'PAYTM']














buystock = []
sellstock = []

interval = 5 # enter 15,60,240,1440,10080,43800
dayback = 15
ed = datetime.now()
stdate = ed - timedelta(dayback)


def conunix(ed):
    ed1 = str(round(time.mktime(ed.timetuple())))
    ed1 = (ed1[:-1])
    ed1 = (ed1 + '0000')
    return ed1


fromdate = conunix(stdate)
todate = conunix(ed)
stt = time.time()



async def getdata(session, stock):


    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:96.0) Gecko/20100101 Firefox/96.0',
        'Accept': 'application/json',
        'Accept-Language': 'en-US,en;q=0.5',
        #'Accept-Encoding': 'gzip, deflate, br'
    }
    url = f'https://groww.in/v1/api/charting_service/v2/chart/exchange/NSE/segment/CASH/{stock}?endTimeInMillis={todate}&intervalInMinutes={interval}&startTimeInMillis={fromdate}'
    async with session.get(url, headers=headers) as response:
        try:
            resp = await response.json()
            candle = resp['candles']
            dt = pd.DataFrame(candle)
            fd = dt.rename(columns={0: 'time', 1: 'Open', 2: 'High', 3: 'Low', 4: 'Close', 5: 'Volume'})
            tim = []
            for each in fd['time']:
                a = each
                a = datetime.fromtimestamp(a).strftime('%Y-%m-%d %H:%M:%S')
                tim.append(a)
            dt = pd.DataFrame(tim)
            fd = pd.concat([dt, fd['time'], fd['Open'], fd['High'], fd['Low'], fd['Close'], fd['Volume']],
                           axis=1).rename(columns={0: 'datetime'})
            fd['symbol'] = stock
            pd.options.mode.chained_assignment = None
            final_df = fd

            final_df['Open'] = final_df['Open'].astype(float)
            final_df['Close'] = final_df['Close'].astype(float)
            final_df['High'] = final_df['High'].astype(float)
            final_df['Low'] = final_df['Low'].astype(float)
            final_df['Volume'] = final_df['Volume'].astype(float)
            final_df['datetime'] = pd.to_datetime(final_df.datetime)  # final_df['datetime']#.astype('datetime64[ns]')
            

            final_df.set_index(final_df.datetime, inplace=True)

            final_df['prevopen'] = final_df['Open'].shift(1)
            final_df['prevhigh'] = final_df['High'].shift(1)
            final_df['prevlow1'] = final_df['Low'].shift(2)
            final_df['prevhigh1'] = final_df['High'].shift(2)
            final_df['prevlow2'] = final_df['Low'].shift(3)
            final_df['prevhigh2'] = final_df['High'].shift(3)
            final_df['prevclose'] = final_df['Close'].shift(1)
            final_df['time_column'] = final_df['datetime'].dt.time
            
            time_string = "09:15:00"

# Define the format matching the string
            time_format = "%H:%M:%S"

# Convert to datetime.time object
            time_obj = datetime.strptime(time_string, time_format).time()
               

            


             
#----------------------
            st.write(time_obj
            final_df['ma200'] = round(ta.momentum._ema(series=final_df['Close'],periods=200))
            newdf = final_df
            diff = 5
            newdf['sig']= np.where(newdf['Open'] > newdf['ma200'],1,0)
            newdf['sig1']= np.where(newdf['Close'] < newdf['ma200'],1,0)
            newdf['sig2']= newdf['sig1'] + newdf['sig']
            newdf['sigfinal']= np.where(newdf['sig2'] == 2,1,0)
            newdf['o-h'] = np.where((newdf['Open'] == newdf['High']),1,0)
           
           
            newdf['seller'] = newdf['sigfinal'] + newdf['o-h']
            newdf = final_df[final_df['time_column']== time_obj].reset_index(drop=True)
            
            last_candle = newdf.iloc[-1]
            st.write(last_candle)
            if last_candle['seller'] == 2:
                
                sellstock.append(last_candle['symbol'])
            # if last_candle['buyer'] == 3:
            #     print('buy lst')
            #     print(last_candle['symbol'])
            #     buystock.append(last_candle['symbol'])


            







            return
        except:
            print('no data')
            pass


async def main():
    async with aiohttp.ClientSession() as session:

        tasks = []
        for stocks in s:
            try:
                stock = stocks

                task = asyncio.ensure_future(getdata(session, stock))

                tasks.append(task)
            except:
                pass
        df = await asyncio.gather(*tasks)
        # print(df)


nest_asyncio.apply()
asyncio.run(main())
















interval = 5 # enter 15,60,240,1440,10080,43800
dayback = 15
ed = datetime.now()
stdate = ed - timedelta(dayback)


def conunix(ed):
    ed1 = str(round(time.mktime(ed.timetuple())))
    ed1 = (ed1[:-1])
    ed1 = (ed1 + '0000')
    return ed1


fromdate = conunix(stdate)
todate = conunix(ed)
stt = time.time()



async def getdata(session, stock):


    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:96.0) Gecko/20100101 Firefox/96.0',
        'Accept': 'application/json',
        'Accept-Language': 'en-US,en;q=0.5',
        #'Accept-Encoding': 'gzip, deflate, br'
    }
    url = f'https://groww.in/v1/api/charting_service/v2/chart/exchange/NSE/segment/CASH/{stock}?endTimeInMillis={todate}&intervalInMinutes={interval}&startTimeInMillis={fromdate}'
    async with session.get(url, headers=headers) as response:
        try:
            resp = await response.json()
            candle = resp['candles']
            dt = pd.DataFrame(candle)
            fd = dt.rename(columns={0: 'time', 1: 'Open', 2: 'High', 3: 'Low', 4: 'Close', 5: 'Volume'})
            tim = []
            for each in fd['time']:
                a = each
                a = datetime.fromtimestamp(a).strftime('%Y-%m-%d %H:%M:%S')
                tim.append(a)
            dt = pd.DataFrame(tim)
            fd = pd.concat([dt, fd['time'], fd['Open'], fd['High'], fd['Low'], fd['Close'], fd['Volume']],
                           axis=1).rename(columns={0: 'datetime'})
            fd['symbol'] = stock
            pd.options.mode.chained_assignment = None
            final_df = fd

            final_df['Open'] = final_df['Open'].astype(float)
            final_df['Close'] = final_df['Close'].astype(float)
            final_df['High'] = final_df['High'].astype(float)
            final_df['Low'] = final_df['Low'].astype(float)
            final_df['Volume'] = final_df['Volume'].astype(float)
            final_df['datetime'] = pd.to_datetime(final_df.datetime)  # final_df['datetime']#.astype('datetime64[ns]')
            

            final_df.set_index(final_df.datetime, inplace=True)

            final_df['prevopen'] = final_df['Open'].shift(1)
            final_df['prevhigh'] = final_df['High'].shift(1)
            final_df['prevlow1'] = final_df['Low'].shift(2)
            final_df['prevhigh1'] = final_df['High'].shift(2)
            final_df['prevlow2'] = final_df['Low'].shift(3)
            final_df['prevhigh2'] = final_df['High'].shift(3)
            final_df['prevclose'] = final_df['Close'].shift(1)
            final_df['time_column'] = final_df['datetime'].dt.time
            
            time_string = "09:15:00"

# Define the format matching the string
            time_format = "%H:%M:%S"

# Convert to datetime.time object
            time_obj = datetime.strptime(time_string, time_format).time()

            


             
#----------------------

            final_df['ma200'] = round(ta.momentum._ema(series=final_df['Close'],periods=200))
            newdf = final_df
            diff = 5
            
            newdf['sig']= np.where(newdf['Open'] < newdf['ma200'],1,0)
            newdf['sig1']= np.where(newdf['Close'] > newdf['ma200'],1,0)
            newdf['sig2']= newdf['sig1'] + newdf['sig']
            newdf['sigfinal']= np.where(newdf['sig2'] == 2,1,0)
            
            newdf['o-l'] = np.where((newdf['Open'] == newdf['Low']),2,0)
            newdf['buyer'] = newdf['sigfinal'] + newdf['o-l']
           
            newdf = final_df[final_df['time_column']== time_obj].reset_index(drop=True)
            
            last_candle = newdf.iloc[-1]
            #print(last_candle)
           
            # if last_candle['seller'] == 2:
            #     print('sell lst')
            #     print(last_candle['symbol'])
            #     sellstock.append(last_candle['symbol'])
            if last_candle['buyer'] == 3:
               
                buystock.append(last_candle['symbol'])


            







            return
        except:
            print('no data')
            pass


async def main():
    async with aiohttp.ClientSession() as session:

        tasks = []
        for stocks in s:
            try:
                stock = stocks

                task = asyncio.ensure_future(getdata(session, stock))

                tasks.append(task)
            except:
                pass
        df = await asyncio.gather(*tasks)
        # print(df)


nest_asyncio.apply()
asyncio.run(main())


























st.write('buy')
st.write(buystock)
st.write('sell')
st.write(sellstock)
