# import requests
# import os
# from dotenv import load_dotenv
# import pandas as pd
# load_dotenv('keys.env')
# id=os.getenv('ADZUNA_ID')
# url=os.getenv('ADZUNA_URL')
# key = os.getenv('ADZUNA_KEY')
# title = "data analyst"
# # exclude = 'annotator'
# country="India"
# params = {
#     "app_id":id,
#     "app_key":key,
#     "what":title,
#     # "what_exclude":exclude,
#     "where":country,
#     "max_days_old":30
# }
# response = requests.get(url,params)
# data = response.json()
# print(data)  # Shows full JSON response
# print("Count:", data.get("count"))
# print("Results length:", len(data.get("results", [])))
# print(response.status_code)
# # if response.status_code==200:
# #     data = response.json()
# #     results = data.get("results", [])

# # jobs_list = []
# # for job in results:
# #     jobs_list.append({
# #         'title': job.get('title', ""),
# #         'description': job.get('description',"")
# # })

# # df_jobs = pd.DataFrame(jobs_list)
# # print(df_jobs.head())