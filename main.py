from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Sample data storage
songs = []

# Define the model
class Song(BaseModel):
    id: int
    title: str
    artist: str
    album: str

# CRUD Endpoints

# Create
@app.post("/songs/", response_model=Song)
def create_song(song: Song):
    for s in songs:
        if s.id == song.id:
            raise HTTPException(status_code=400, detail="Song ID already exists.")
    songs.append(song)
    return song

# Read all
@app.get("/songs/", response_model=List[Song])
def read_songs():
    return songs

# Read one
@app.get("/songs/{song_id}", response_model=Song)
def read_song(song_id: int):
    for song in songs:
        if song.id == song_id:
            return song
    raise HTTPException(status_code=404, detail="Song not found.")

# Update
@app.put("/songs/{song_id}", response_model=Song)
def update_song(song_id: int, updated_song: Song):
    for i, song in enumerate(songs):
        if song.id == song_id:
            songs[i] = updated_song
            return updated_song
    raise HTTPException(status_code=404, detail="Song not found.")

# Delete
@app.delete("/songs/{song_id}")
def delete_song(song_id: int):
    for i, song in enumerate(songs):
        if song.id == song_id:
            del songs[i]
            return {"message": "Song deleted successfully."}
    raise HTTPException(status_code=404, detail="Song not found.")
