from radio_channel import RadioChannel
from membership import NormalMember, GoldMember, VIPMember, VIPPlusMember

def display_menu():
    # Display the menu options to the user
    print("==== Radio Management System ====")
    print("1. Play random song")
    print("2. Like a song")
    print("3. Comment on a song")
    print("4. Request a song")
    print("5. Exit")
    print("===============================")

def get_membership_type():
    # Get the membership type from the user
    membership_type = input("Enter your membership type (normal, gold, vip, vip+): ")
    return membership_type.lower()

def play_random_song(radio_channel, membership_type):
    # Play a random song from the radio channel
    radio_channel.play_random_song(membership_type)

def like_song(radio_channel):
    # Like a song by entering the song number
    song_number = int(input("Enter the song number to like: "))
    radio_channel.like_song(song_number)

def comment_on_song(radio_channel):
    # Comment on a song by entering the song number and comment
    song_number = int(input("Enter the song number to comment on: "))
    comment = input("Enter your comment: ")
    radio_channel.comment_song(song_number, comment)

def request_song(radio_channel, membership):
    # Request a song by entering the song name
    song_name = input("Enter the song name to request: ")
    membership.request_song(song_name, radio_channel)

def run_radio_management_system():
    radio_channel = RadioChannel()
    radio_channel.load_song_pool("AllSongs.txt")

    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            membership_type = get_membership_type()
            play_random_song(radio_channel, membership_type)
        elif choice == "2":
            like_song(radio_channel)
        elif choice == "3":
            comment_on_song(radio_channel)
        elif choice == "4":
            membership_type = get_membership_type()
            membership = get_membership_instance(membership_type)
            request_song(radio_channel, membership)
        elif choice == "5":
            print("Thank you for using the Radio Management System.")
            break
        else:
            print("Invalid choice. Please try again.")

def get_membership_instance(membership_type):
    # Return an instance of the membership class based on the membership type
    if membership_type == "normal":
        return NormalMember("John Doe", "2022-01-01")
    elif membership_type == "gold":
        return GoldMember("Jane Smith", "2022-02-01")
    elif membership_type == "vip":
        return VIPMember("David Johnson", "2022-03-01")
    elif membership_type == "vip+":
        return VIPPlusMember("Sarah Williams", "2022-04-01")
    else:
        print("Invalid membership type. Using normal membership.")
        return NormalMember("John Doe", "2022-01-01")

if __name__ == "__main__":
    run_radio_management_system()
