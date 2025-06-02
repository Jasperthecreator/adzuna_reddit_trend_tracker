from pytrends.request import TrendReq
trends = TrendReq()
trends.build_payload(kw_list = ['Data Science'], geo='IN', timeframe= 'now 7-d')
df7 = trends.interest_over_time()
trend_7d = int(df7.iloc[-1,0])
trends.build_payload(kw_list = ['Data Science'], geo='IN', timeframe= 'today 1-m')
df30 = trends.interest_over_time()
trend_30d = int(df30.iloc[-1,0])
from supabase import create_client, Client
url = 'https://jdusjoogssiwjcrfkcux.supabase.co'
key = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImpkdXNqb29nc3Npd2pjcmZrY3V4Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDg0MzA2NjksImV4cCI6MjA2NDAwNjY2OX0.TXq9SWyg_rGntuGO15shlL6SB_mxK6PBSz68sECl140'
trend_agg = {"7d": trend_7d, "30d": trend_30d}
client = create_client(url, key)
client.table("Pytrends - DS").insert(trend_agg).execute()