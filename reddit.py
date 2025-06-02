import praw
import os
from dotenv import load_dotenv
load_dotenv(dotenv_path='keys.env')
reddit = praw.Reddit(
    client_id=${{secrets.reddit_id}},
    client_secret=${{secrets.reddit_secret}},
    user_agent=${{secrets.reddit_u_agent}}
)
r_count = int(reddit.subreddit('datascience').active_user_count)
print(r_count)

import supabase
from supabase import create_client, Client
url = ${{secrets.supabase_url}}
key = ${{secrets.supabase_key}}
client = create_client(url, key)
client.table('r_ds').insert({'highest_users': r_count}).execute()
