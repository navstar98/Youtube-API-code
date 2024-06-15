from googleapiclient.discovery import build
import pandas as pd

api_key='AIzaSyAfVREx1TQUg0SOZxFMDLtTDu0UOhhGhlw'

youtube=build('youtube','v3',developerKey=api_key)

# request=youtube.channels().list(
#     part='statistics',
#     # forUsername='navdeeprana8477',
#     # forUsername='sentdex')   # forusername means you channelname
#     forUsername='IndianMediaLatest')   # forusername means you channelname

request=youtube.commentThreads().list(
    part='snippet',
    videoId='daTWrT1YEPQ',# v=daTWrT1YEPQ(any videoID) in url
    maxResults=100
)
response=request.execute()

for item in response['items']:
   print(item['snippet']['topLevelComment']['snippet']['textDisplay']) 
# print(response)
