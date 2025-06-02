import praw
import os
from dotenv import load_dotenv
load_dotenv(dotenv_path='keys.env')
reddit = praw.Reddit(
    client_id=os.getenv('reddit_url'),
    client_secret=os.getenv('reddit_key'),
    user_agent=os.getenv('reddit_u_agent')
)
r_count = int(reddit.subreddit('datascience').active_user_count)
print(r_count)

import supabase
from supabase import create_client, Client
url = os.getenv('supabase_url')
key = os.getenv('supabase_key')
client = create_client(url, key)
client.table('r_ds').insert({'highest_users': r_count}).execute()