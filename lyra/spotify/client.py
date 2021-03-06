import spotipy 

from spotipy.oauth2 import SpotifyClientCredentials

def main():
    #redirect_uri = "", scope = "user-library-read"
    sp = spotipy.Spotify(auth_manager = SpotifyClientCredentials(client_id = "", 
                                                                 client_secret = ""))

    results = sp.search(q = "Plastikman - Spastik", limit = 20)

    for idx, track in enumerate(results["tracks"]["items"]):
        print(idx, track["name"])

if __name__ == "__main__":
    main()