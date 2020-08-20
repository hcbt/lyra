import os
import json

import yt.client

youtube_url = "https://www.youtube.com"
youtube_video_url = youtube_url + "/watch?v="
youtube_playlist_url = youtube_url + "/playlist?list="

class playlists:
    def results(self):        
        youtube = yt.client.api_auth()
        request = youtube.playlists().list(part = "snippet, contentDetails", mine = True)
        response = request.execute()
        return response
    
    #Returns users playlist ids
    def playlist_id(self):
        response = self.results()
        playlist_ids = []
        
        for i in response["items"]:
            playlist_ids.append(i["id"])
    
        return playlist_ids
    
    #Returns users playlist titles    
    def playlist_title(self):
        response = self.results()
        playlist_titles = []
        
        for i in response["items"]:
            playlist_titles.append(i["snippet"]["title"])
    
        return playlist_titles

    #Creates a playlist with a given name and return playlist id
    def create_playlist(self, playlist_name):
        youtube = yt.client.api_auth()
    
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

class playlistItems:
    def results(self, playlist_id): #used to make requests for playlist items
        youtube = yt.client.api_auth()
        response = youtube.playlistItems().list(part = "snippet", playlistId = playlist_id, maxResults = 50).execute()
        
        next_page_token = response.get("nextPageToken")

        #Adds results from other pages if there's more than 50 videos in playlist
        while ("nextPageToken" in response):
            next_page = youtube.playlistItems().list(part="snippet", playlistId = playlist_id, maxResults = 50, pageToken = next_page_token).execute()
            response["items"] = response["items"] + next_page["items"]

            if "nextPageToken" not in next_page:
                response.pop("nextPageToken", None)
            else:
                next_page_token = next_page["nextPageToken"]
         
        return response

    def video_id(self, playlist_id):
        response = self.results(playlist_id)
        video_ids = []

        for i in response["items"]:
            video_ids.append(i["snippet"]["resourceId"]["videoId"])
            
        return video_ids

    def video_title(self, playlist_id):
        response = self.results(playlist_id)
        video_titles = []

        for i in response["items"]:
            video_titles.append(i["snippet"]["title"])

        return video_titles
        
    #Add videos to playlist    
    def add_to_playlist(self, playlist_id, video_id):
        youtube = yt.client.api_auth()
        
        request = youtube.playlistItems().insert(
            part = "snippet",
            body = 
            {
                "snippet": 
                {
                    "playlistId": playlist_id,
                    "position": 0,
                    "resourceId": 
                    {
                        "kind": "youtube#video",
                        "videoId": video_id
                    }
                }
            }
        )
    
        response = request.execute()
        
        return response