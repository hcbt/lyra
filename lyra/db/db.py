import datetime
import pymongo

def add_entry(id, genre):
    client = pymongo.MongoClient()
    db = client["main"]

    track = {"_id": id,
             "genre": genre,
             "entry_date": datetime.datetime.utcnow()}

    tracks = db.youtube_tracks
    track_id = tracks.insert_one(track).inserted_id

def find_entry(id):
    client = pymongo.MongoClient()
    db = client["main"]

    return db.youtube_tracks.find_one(id)

def update_entry():
    pass

def delete_entry():
    pass

if __name__ == "__main__":
    #add_entry("aiAyUHKIwi0", "techno")
    find_entry("aiAyUHKIwi0")