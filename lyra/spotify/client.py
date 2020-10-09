import spotipy 

from spotipy.oauth2 import SpotifyClientCredentials

def main():
    #redirect_uri = "", scope = "user-library-read"
    sp = spotipy.Spotify(auth_manager = SpotifyClientCredentials(client_id = "0aa44a85743746e899db22ea4bfc94c6", 
                                                                 client_secret = "616e94f39eff4f94a1648a9c77125220"))

    results = sp.search(q = "Plastikman - Spastik", limit = 20)

    for idx, track in enumerate(results["tracks"]["items"]):
        print(idx, track["name"])

if __name__ == "__main__":
    main()