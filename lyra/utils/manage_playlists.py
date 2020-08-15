import utils.youtube_client

youtube_url = "https://www.youtube.com"
youtube_video_url = youtube_url + "/watch?v="
youtube_playlist_url = youtube_url + "/playlist?list="

#Returns users playlists
def list_playlists():
    youtube = utils.youtube_client.api_auth()

    request = youtube.playlists().list(part = "snippet, contentDetails", mine = True)
    
    response = request.execute()
    
    return response

#Creates a playlist with a given name and return playlist id
def create_playlist(playlist_name):
    youtube = utils.youtube_client.api_auth()
    
    playlist_id = []
    
    request = youtube.playlists().insert(
        part = "snippet, status",
        body = 
        {
          "snippet": 
          {
            "title": playlist_name,
            "defaultLanguage": "en"
          },
          "status": 
          {
            "privacyStatus": "private"
          }
        }
    )
    
    response = request.execute()
    
    playlist_id.append(response["id"])
    
    return "".join(playlist_id)
    
#Add videos to playlist    
def add_to_playlist(video_id):
    pass
    #youtube = utils.youtube_client.apie_auth()
    #
    #response = request.execute()
    #
    #return response


    