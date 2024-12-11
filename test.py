

MENUS = {
    "main": {
        1: "Play Library",
        2: "Add Track to Music Library",
        3: "Search Track from Music Library",
        4: "View Track from Music Library",
        5: "Manage Playlists",
        6: "Manage Queues",
        7: "Exit"
    },
    
    "playlist": {
        1: "Create Playlist",
        2: "View Playlists",
        3: "Delete Playlist",
        4: "Add Track to Playlist",
        5: "Remove Track from Playlist",
        6: "Return to Main Menu"
    },
    
    "queue" : {
        1: "Play Playlist",
        2: "Add Playlist to Queue",
        3: "Shuffle Queue",
        4: "Enable/Disable Repeat Mode",
        5: "Next Track",
        6: "Previous Track",
        7: "View Current Queue",
        8: "Clear Queue",
        9: "Save Queue and Exit"
    }
}

def displayMenu(menu):
    """
    Display the specified menu
    Args:
        menu (dict): The menu to display.
    """
    print("===================================")
    for key, value in menu.items():
        print(f"[{key}] {value}")
    print("===================================")


def mainMenu():
    """
    Main function to run the menu system
    """
    while True:
        displayMenu(MENUS["main"])
        choice = input("Enter your choice: ")
        if choice == "1":
            play_track_from_library()
        elif choice == "2":
            add_track_to_library()
        elif choice == "3":
            search_track_from_library()
        elif choice == "4":
            view_Library()
        elif choice == "5":
            playlist_menu()
        elif choice == "6":
            queue_menu()  # Calls the queue menu
        elif choice == "7":
            exit()
        else:
            print("Invalid choice. Please try again.")

def play_track_from_library():
    track = Track()
    track.play_library()
    
def add_track_to_library():
    """
        Add a track to the music library
    """
    track = Track()  # You can add track details here
    track.add_track()

def search_track_from_library():
    """
        Search a track in the music library
        Displays multiple tracks with the same title
    """
    track = Track()  
    title = input("Enter track title:")
    track.search_track(title)

def view_Library():
    """
        View the music library
    """
    track = Track()  
    track.view_tracks()

def playlist_menu():
    """
        Menu for playlist 
    """
    playlist = Playlist()  
    while True:
        displayMenu(MENUS["playlist"])
        choice = input("Enter your choice: ")
        if choice == "1":
            play_playlist()
        elif choice == "2":
            create_playlist()
        elif choice == "3":
            view_playlist_library()
        elif choice == "4":
            delete_playlist()
        elif choice == "5":
            add_track_to_playlist()
        elif choice == "6":
            playlist.remove_track_from_playlist()
        elif choice == "7":
            break
        else:
            print("Invalid choice. Please try again.")

def play_playlist():
    """ Play a playlist """
    playlist = Playlist()
    playlist.play_playlist()

def create_playlist():
    """ Create a playlist """
    playlist = Playlist()
    playlist.create_playlist()

def view_playlist_library():
    """ View playlist """
    playlist = Playlist()
    playlist.view_playlist()

def delete_playlist():
    """ Delete a playlist """
    playlist = Playlist()
    playlist.delete_playlist()

def add_track_to_playlist():
    """ Add a track to a playlist """
    playlist = Playlist()
    playlist.add_track_to_playlist()

def queue_menu():
    """
    Menu for queue
    """
    while True:
 # Display the current queue status
        displayMenu(MENUS["queue"])
        choice = input("Enter your choice: ")
        if choice == "1":
            play_playlist()
        elif choice == "2":
            add_playlist_to_queue() 
        elif choice == "3":
            shuffle_queue() 
        elif choice == "4":
            repeat_mode()  
        elif choice == "5":
            next_track()  
        elif choice == "6":
            previous_track()
        elif choice == "7":
            view_queue() 
        elif choice == "8":
            clear_queue() 
        elif choice == "9":
            save_queue()  # Savea and Exit option
        else:
            print("Invalid choice. Please try again.")

playback = Playback()
def play_playlist():
    playback.play_queue()

def add_playlist_to_queue():
    """Add a playlist to the queue."""
    playback.display_playlist()
    playlist_name = input("Enter the playlist name to add to queue: ")
    playback.add_playlist_to_queue(playlist_name)

def shuffle_queue():
    """ Shuffle the queue """
    playback.shuffle_tracks()

def repeat_mode():
    """ Enable or disable repeat mode """
    track_name = input("Enter the track name to repeat: ")
    playback.repeat_tracks(track_name)

def next_track():
    """ Play the next track """
    playback.play_next_track()

def previous_track():
    """ Play the previous track """
    playback.play_previous_track()

def view_queue():
    """ View the current queue """
    playback.list_queue()

def clear_queue():
    """ Clear the queue """
    playback.clear_queue()

def save_queue():
    """ Save the queue and exit """
    mainMenu()

if __name__ == "__main__":
    mainMenu()
