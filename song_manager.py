from song import Song

class SongManager:
    def __init__(self):
        self.song_pool = []

    def load_song_pool(self, file_name):
        with open(file_name, "r") as file:
            for line in file:
                song = Song.from_string(line)
                self.song_pool.append(song)

    def update_song_pool(self):
        with open("AllSongs.txt", "w") as file:
            for song in self.song_pool:
                file.write(f"{song}\n")

    def get_most_liked_song(self):
        if self.song_pool:
            most_liked_song = max(self.song_pool, key=lambda song: song.likes)
            return most_liked_song
        else:
            return None
