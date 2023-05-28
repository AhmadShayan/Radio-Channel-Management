import random
import time

from song import Song

class RadioChannel:
    def __init__(self):
        self.song_pool = []
        self.vip_requests = []
        self.vip_plus_requests = []

    def load_song_pool(self, file_name):
        with open(file_name, "r") as file:
            for line in file:
                song = Song.from_string(line)
                self.song_pool.append(song)

    def play_random_song(self, user_membership):
        random_song = random.choice(self.song_pool)
        print("Now playing:")
        print(f"Song: {random_song.name}")
        print(f"Composer: {random_song.composer}")
        print(f"Likes: {random_song.likes}")

        # Apply playback effects based on membership type
        if user_membership == "gold":
            random_song.playback_effects = "Gold effects"
        elif user_membership == "vip":
            random_song.playback_effects = "VIP effects"
        elif user_membership == "vip+":
            random_song.playback_effects = "VIP+ effects"
        # No effects for normal membership

        print(f"Playback Effects: {random_song.playback_effects}")

        # Simulating the duration of the song
        # Replace this with your actual code to play the song
        time.sleep(random_song.duration)

        print("Song finished. Moving to the next song.")

        # Updating the likes of the played song
        random_song.like()
        self.update_song_pool()

        # Play the next song
        self.play_random_song(user_membership)

    def like_song(self, song_number):
        if 1 <= song_number <= len(self.song_pool):
            song = self.song_pool[song_number - 1]
            song.like()
            self.update_song_pool()
            print(f"You liked {song.name} by {song.composer}!")
        else:
            print("Invalid song number.")

    def comment_song(self, song_number, comment):
        if 1 <= song_number <= len(self.song_pool):
            song = self.song_pool[song_number - 1]
            song.add_comment(comment)
            with open(f"{song.name.replace(' ', '')}.txt", "a") as file:
                file.write(f"{comment}\n")
            print(f"You commented on {song.name}!")
        else:
            print("Invalid song number.")

    def request_song(self, song_name, membership_type):
        if membership_type == "vip" and len(self.vip_requests) >= 3:
            print("Sorry, you have reached the maximum number of requests.")
            return
        elif membership_type == "vip+" and len(self.vip_plus_requests) >= 10:
            print("Sorry, you have reached the maximum number of requests.")

    def update_song_pool(self):
        # Update the AllSongs.txt file with the updated song pool details
        with open("AllSongs.txt", "w") as file:
            for song in self.song_pool:
                file.write(f"{song}\n")
