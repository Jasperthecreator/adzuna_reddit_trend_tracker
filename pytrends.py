from pytrends.request import TrendReq
trends = TrendReq()
trends.build_payload(kw_list = ['Data Science'], geo='IN', timeframe= 'now 7-d')
df7 = trends.interest_over_time()
trend_7d = int(df7.iloc[-1,0])
trends.build_payload(kw_list = ['Data Science'], geo='IN', timeframe= 'today 1-m')
df30 = trends.interest_over_time()
trend_30d = int(df30.iloc[-1,0])
from supabase import create_client, Client
url = ${{supabase_url}}
key = ${{supabase_key}}
trend_agg = {"7d": trend_7d, "30d": trend_30d}
client = create_client(url, key)
client.table("Pytrends - DS").insert(trend_agg).execute()

import pandas as pd
import numpy as np