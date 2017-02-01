#!/usr/bin/env python3
import sqlite3
import subprocess as sb
from random import randint

#Connect to the db and get a list of all songs (inefficient, but...)
db = sqlite3.connect('/var/www/dj/data/songs.db')
c = db.cursor()
def get_songs(songs):
    songs = [song[0] for song in c.execute("select * from songs;").fetchall()]
    return songs
def select_song(songs):
    #Shuffle!
    song_id = 0
    if songs == []:
        return ''
    elif len(songs) <= 2:
        song_id = 1
    else:
        song_id = randint(0,len(songs)-1)

    #Remove the song from the list
    song_name = songs[song_id]
    c.execute("delete from songs where link=(?);", (song_name,))
    db.commit()
    return song_name

#gogogogo
def main():
    songs_list = []
    while True:
        songs_list = get_songs(songs_list)
        if len(songs_list) < 1:
            continue
        else:
            songname = select_song(songs_list)
            proc = sb.Popen(['/usr/bin/mpsyt', 'playurl', songname])
            proc.communicate()
            proc.wait()
    db.close()

if __name__ == '__main__':
    main()
