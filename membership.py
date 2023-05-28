class NormalMember:
    def __init__(self, name, registration_date):
        self.name = name
        self.registration_date = registration_date

    def like_song(self, song):
        song.like()
        # Update the AllSongs.txt file with the new like 
        
    def request_song(self, song_name, radio_channel):
        print("Sorry, you don't have permissions to request a song, change you membership though.")


class GoldMember(NormalMember):
    def __init__(self, name, registration_date):
        super().__init__(name, registration_date)
        self.comments = []

    def comment_song(self, song, comment):
        song.add_comment(comment)
        self.comments.append(comment)
        # Update the song's comment file
        with open("maviduvar.txt", "a") as file:
            file.write(f"{song.name} - {comment}\n")


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
                
class Membership:
    def __init__(self, membership_type, max_requests=0):
        self.membership_type = membership_type
        self.max_requests = max_requests

    def can_make_request(self, num_requests):
        if self.max_requests == 0:
            return True
        return num_requests < self.max_requests

    def request_song(self, song_name, radio_channel):
        if self.can_make_request(len(self.requests)):
            requested_song = radio_channel.get_song_by_name(song_name)
            if requested_song:
                radio_channel.play_requested_song(requested_song)
                self.requests.append(song_name)
            else:
                print("Sorry, the requested song is not available.")
        else:
            print("Sorry, you have reached the maximum number of requests.")

