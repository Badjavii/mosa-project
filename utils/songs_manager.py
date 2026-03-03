# ./utils/songs_manager

class download_manager:
    def __init__(destiny):
        self.__destiny = destiny

    def __show_menu():
        while True:
            os.system("clear")
            print("\n== 1. Song Downloader ==")
            print("-" * 30)
            print(f"Current path: {self.__destiny}")
            print("-" * 30)
            print("1. Download song by Youtube URL")
            print("2. Download list of songs by reading a file")
            print("3. Delete song")


def show_menu(): 

    while True:
        os.system("clear")
        print("\n== Music Manager v1.0 ==")
        print
        print("1. Show all music")
        print("2. Download song")
        print("3. Find for a song")
        print("4. Delete song")
        print("5. Edit song metadata")
        print("6. Edit song position on playlist")
        print("0. Exit")
    
    option = input("\n> Select an option (0-6): ")
    
    if option.isdigit():
        opt = int(option)
        if (opt > 6) or (opt < 0):
            print("[!] Error: option does not exist")
            return -1
        else: 
            return opt
    else:
        print("[!] Error: Only numbers")
        return -1
