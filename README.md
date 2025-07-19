This is a project I ran (and am currently running) to check the "saturation rate" of the job market in the filed of data science. 

This was just an excercise for me in terms of getting familiar with APIs and database interactions through Python.

This repo runs automatically on a near-regular basis using Github Actions, and interacts with three different APIs - PRAW (for Reddit), Adzuna API, and Supabase.py to interact with my database in Supabase. 

Due to unavailability of accurate data through legal means, a rounabout way had to be devised to keep track of the "hype" factor and the job market. As such, what we are tracking is the active users on Reddit and fresh job postings being posted to Adzuna everyday. Though this won't give us the most accurate picture, I believe this serves as a good overall picture of job space and the people getting interested in the field.

The script which captures the reddit data is run every 10 mins and averaged out at the end of the day to get a clearer abstract of the footfall to the subreddit, r/datascience, while adzuna API is ran at the end of the day to get how many new postings with related keywords were posted to the boards in the last 24 hours. 

While I did also write the scripts to get data from Google Trends, I unfortunately got rate-limited. You can give it a try though! thanks for visiting!

If you would like to, you can also take a look at the supabase table at: https://supabase.com/dashboard/project/jdusjoogssiwjcrfkcux in the table named "Lake fedou".

Built using the Adzuna Job Search API and PRAW (Python Reddit API Wrapper) ❤️:
Adzuna API: https://developer.adzuna.com/
PRAW: https://praw.readthedocs.io/
