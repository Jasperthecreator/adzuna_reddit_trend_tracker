from supabase import create_client
import pandas as pd
import numpy as np
from dotenv import load_dotenv
import os
load_dotenv(dotenv_path='keys.env')
key = os.getenv('SUPABASE_KEY')
url = os.getenv('SUPABASE_URL')
client = create_client(url, key)
reddit_response = client.table('r_ds').select('active_users').execute()
reddit_user_count = []
for count in reddit_response.data:
    reddit_user_count.append(count['active_users'])

reddit_highest = max(reddit_user_count)
reddit_median = np.median(reddit_user_count)

adzuna_count = client.table('adzuna').select('title', count='exact', head=True)

mapping = {"reddit_highest": reddit_highest, "reddit_median": reddit_median, "adzuna_count": adzuna_count}
client.table('lake_fedou').insert(mapping).execute()  #inserting the data derived from branch tables 
                                                      #into main table

client.table('r_ds').delete().neq("id",0).execute() 
client.table('r_ds').delete().neq("id",0).execute() 
