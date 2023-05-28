from song import Song

class FileManager:
    @staticmethod
    def load_song_pool(file_name):
        song_pool = []
        with open(file_name, "r") as file:
            for line in file:
                song = Song.from_string(line)
                song_pool.append(song)
        return song_pool

    @staticmethod
    def update_song_pool(file_name, song_pool):
        with open(file_name, "w") as file:
            for song in song_pool:
                file.write(f"{song}\n")

    @staticmethod
    def save_comment_to_file(song, comment):
        with open("maviduvar.txt", "a") as file:
            file.write(f"{song.name} - {comment}\n")

