from googleapiclient.discovery import build
import pandas as pd

comments=[]
api_key='AIzaSyAfVREx1TQUg0SOZxFMDLtTDu0UOhhGhlw'

youtube=build('youtube','v3',developerKey=api_key)

request=youtube.commentThreads().list(
    part='snippet',
    videoId='daTWrT1YEPQ',# v=daTWrT1YEPQ(any videoID) in url
    maxResults=300
)

response=request.execute()

for item in response['items']:
    comment=item['snippet']['topLevelComment']['snippet']
    comments.append([
        comment['authorDisplayName'],
        comment['publishedAt'],
        comment['updatedAt'],
        comment['likeCount'],
        comment['textDisplay']
    ])
    
df=pd.DataFrame(comments, columns=['author', 'published_at','updated_at','like_count','text']) 
df.to_csv("comments1.csv") 
# print(df) it will print 100 comments 
# print(df.head(10))    # print only 10 comments