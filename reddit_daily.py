import praw
import os
from dotenv import load_dotenv
load_dotenv(dotenv_path='keys.env')
reddit = praw.Reddit(
    client_id= os.getenv('REDDIT_URL'),
    client_secret= os.getenv('REDDIT_SECRET'),
    user_agent=os.getenv('REDDIT_U_AGENT')
)
r_count = int(reddit.subreddit('datascience').active_user_count)
print(r_count)

import supabase
from supabase import create_client, Client
url = os.getenv('SUPABASE_URL')
key = os.getenv('SUPABASE_KEY')
client = create_client(url, key)
client.table('r_ds').insert({'active_users': r_count}).execute()
