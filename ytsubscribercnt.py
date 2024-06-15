from googleapiclient.discovery import build

api_key='AIzaSyAfVREx1TQUg0SOZxFMDLtTDu0UOhhGhlw'

youtube=build('youtube','v3',developerKey=api_key)

request=youtube.channels().list(
    part='statistics',
    # forUsername='navdeeprana8477',
    # forUsername='sentdex')   # forusername means you channelusernabe which starts with @navdeep8857
    forUsername='IndianMediaLatest')   # forusername means you channelname

response=request.execute()

print(response)