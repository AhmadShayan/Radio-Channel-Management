class NormalMember:
    def __init__(self, name, registration_date):
        self.name = name
        self.registration_date = registration_date

    def like_song(self, song):
        song.like()
        # Update the AllSongs.txt file with the new like count


class GoldMember(NormalMember):
    def __init__(self, name, registration_date):
        super().__init__(name, registration_date)
        self.comments = []

    def comment_song(self, song, comment):
        song.add_comment(comment)
        self.comments.append(comment)
        # Update the song's comment file


class VIPMember(GoldMember):
    def __init__(self, name, registration_date):
        super().__init__(name, registration_date)
        self.requests = []

    def request_song(self, song_name, radio_channel):
        if len(self.requests) >= 3:
            print("Sorry, you have reached the maximum number of requests.")
        else:
            requested_song = radio_channel.get_song_by_name(song_name)
            if requested_song:
                radio_channel.play_requested_song(requested_song)
                self.requests.append(song_name)
            else:
                print("Sorry, the requested song is not available.")


class VIPPlusMember(VIPMember):
    def __init__(self, name, registration_date):
        super().__init__(name, registration_date)

    def request_song(self, song_name, radio_channel):
        if len(self.requests) >= 10:
            print("Sorry, you have reached the maximum number of requests.")
        else:
            requested_song = radio_channel.get_song_by_name(song_name)
            if requested_song:
                radio_channel.play_requested_song(requested_song)
                self.requests.append(song_name)
            else:
                print("Sorry, the requested song is not available.")
