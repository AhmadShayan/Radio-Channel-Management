class Song:
    def __init__(self, name, composer, likes=0, duration=0, playback_effects="", comments=None):
        self.name = name
        self.composer = composer
        self.likes = likes
        self.duration = duration
        self.playback_effects = playback_effects
        self.comments = comments or []

    def like(self):
        self.likes += 1

    def add_comment(self, comment):
        self.comments.append(comment)

    def __str__(self):
        return f"{self.name} - {self.composer} - {self.likes} - {self.duration} - {self.playback_effects}"

    @classmethod
    def from_string(cls, song_string):
        name, composer, likes, duration, playback_effects = song_string.strip().split(" - ")
        return cls(name, composer, int(likes), int(duration), playback_effects)
    
    
# #TESTING
# # Create a song object
# song1 = Song("Song 1", "Composer 1", duration=180)

# # Print the initial details of the song
# print(song1)

# # Like the song
# song1.like()

# # Print the updated details of the song
# print(song1)
