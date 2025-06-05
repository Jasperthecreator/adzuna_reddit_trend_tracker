import requests
import os
from dotenv import load_dotenv
import pandas as pd
from supabase import create_client
load_dotenv('keys.env')
id=os.getenv('ADZUNA_ID')
url=os.getenv('ADZUNA_URL')
key = os.getenv('ADZUNA_KEY')
title = "data analyst"

#opening empty list and cycling going through pages in search results to get all eligible jobs extended into the listt
all_jobs = []
for page in range (1,100):
    full_url = f"{url}{page}"
    params = {
    "app_id":id,
    "app_key":key,
    "what":title,
    "max_days_old":1
    }
    response = requests.get(full_url,params)
    data = response.json()
    all_jobs.extend(data.get("results", []))

filt_jobs = []
for job in all_jobs:
    filt_jobs.append({
        "title": job.get("title"),
        "description": job.get("description")
    })
df_jobs = pd.DataFrame(filt_jobs)

supabase_url = os.getenv('SUPABASE_URL')
supabase_key = os.getenv('SUPABASE_KEY')

client = create_client(supabase_url, supabase_key)

for record in df_jobs.to_dict(orient='records'):
    client.table('adzuna').insert(record).execute()
