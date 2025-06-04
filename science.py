from pytrends.request import TrendReq
import time
from dotenv import load_dotenv
import os
load_dotenv('keys.env')
trends = TrendReq()
trends.build_payload(
    kw_list=['/g/11g8vtqdjz'],
    geo='IN',
    timeframe='today 1-m'
)
df = trends.interest_over_time()
data_science_30d = int(df['/g/11g8vtqdjz'].iloc[-1])
from supabase import create_client, Client
url = os.getenv('SUPABASE_URL')
key = os.getenv('SUPABASE_KEY')
trend_agg = {"data_science_30d": data_science_30d}
client = create_client(url, key)
client.table("ds_trends_gg").insert(trend_agg).execute()
