#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import nsepy as nse
import pandas as pd 
import pickle
from datetime import date

NSE_df= pd.read_csv(r'https://www1.nseindia.com/content/indices/ind_nifty500list.csv',index_col='Company Name')

NSE_df
df= pd.DataFrame(NSE_df)
len (NSE_df)
print (NSE_df)


# In[ ]:


Symbole_name_list = df["Symbol"].tolist()


# In[ ]:


num_of_days = 20

today = date.today()
from datetime import date
from dateutil.relativedelta import relativedelta
start_date = date.today() + relativedelta(days=-num_of_days)
print("Quering from "+str(start_date)+" to "+str(today))
rsi_map = dict()

for i in range(0,len(Symbole_name_list)):
    stock_price= nse.get_history(symbol=Symbole_name_list[i],index=False, start=start_date,end= today)
    if len(stock_price) == 0:
        print("skipping: "+Symbole_name_list[i])
        continue
    df= pd.DataFrame(stock_price)
    gain=(df['Close']- df['Open']).apply(lambda x:x if x>0 else 0)
    sum(gain)
    len(gain)
    averagegain =sum(gain) /len(gain)
    loss=(df['Open']- df['Close']).apply(lambda x:x if x>0 else 0)
    sum(loss)
    len(loss)
    averageloss =sum(loss) /len(loss)
    rs = averagegain/averageloss
    vs= rs+1
    zx = 100/vs
    unf_rsi = 100-zx
    rsioutput= "{:.2f}".format(unf_rsi)
    print(Symbole_name_list[i], ": ",rsioutput, ", days: ",len(stock_price))
    rsi_map[Symbole_name_list[i]] = rsioutput

