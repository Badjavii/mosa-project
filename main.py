# downloader.py
import yt_dlp as downloader 
import os
from mutagen.easyid3 import EasyID3

def delete_song(destiny):
    files = [f for f in os.listdir(destiny) if f.endswith('.mp3')]
    files.sort()
    
    if not files:
        print("[!] Nothing to delete.")
        return

    list_music(destiny)
    
    try:
        idx = int(input("\n> Enter the number of the song to delete (0 to cancel): "))
        if idx == 0:
            return
        
        if 1 <= idx <= len(files):
            file_to_remove = os.path.join(destiny, files[idx-1])
            os.remove(file_to_remove)
            print(f"[+] Deleted: {files[idx-1]}")
        else:
            print("[!] Invalid number.")
    except ValueError:
        print("[!] Please enter a valid number.")
    except Exception as e:
        print(f"[!] Error: {e}")

# Show all songs in the destiny
def list_music(destiny):
    print(f"\nContent in {destiny}")
    print("-" * 30)
    
    files = [f for f in os.listdir(destiny) if f.endswith('.mp3')]
    
    if not files:
        print("[!] No MP3 songs were found.")
    else:
        for i, file in enumerate(sorted(files), 1):
            try:
                audio = EasyID3(os.path.join(destiny, file))
                artist = audio.get('artist', ['Unknown'])[0]
                title = audio.get('title', [file])[0]
                print(f"{i}. {artist} - {title}")
            except:
                print(f"{i}. {file}")
    print("-" * 30)

def download_song(url, destiny):

    downloader_options = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': f'{destiny}/%(title)s.%(ext)s',
        'prefer_ffmpeg': True,
    }

    try:
        print(f"[+] Downloading in {destiny}...")
        with downloader.YoutubeDL(downloader_options) as ydl:
            ydl.download([url])
        print("[+] Download finished!")
    except Exception as e:
        print(f"[!] Error during download: {e}")

def main_menu(destiny):
    print("\n=== Music Manager v1.0 ===")
    print("-" * 30)
    print(f"Current path: {destiny}")
    print("-" * 30)
    print("1. Set working path")
    print("2. Manage of songs")
    print()


def show_menu(): 
    print("\n=== Music Manager v1.0 ===")
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

def exists_path(destiny):
    if not os.path.exists(destiny):
        return False
    else: 
        return True

def set_new_path():
    destiny = ""
    while True:
        dest = input("> Submit target path: ")
        if not os.path.exists(dest):
            print("[!] Error: The path does not exist.")
        else:
            print("[+] The route was set correctly")
            return destiny
    

# === main ===
if __name__ == "__main__":
    
    os.system("clear")
    print("Welcome!")
    dest = "/home/badjavii/Music"
    
    if (exists_path(dest) == False):
        dest = set_new_path()

    while True:
        os.system("clear")
        user_input = show_menu()
        
        match user_input:
            case 0:
                print("Closing program")
                break
            case 1:
                list_music(dest)
            case 2:
                songs_url = []
                while True:
                    nro_songs = int(input("> Submit the number of songs to download (1-20): "))
                    if (nro_songs > 0) and (nro_songs < 21):
                        break
                
                for i in range (nro_songs):
                    songs_url.append(input("> Submit song: "))
                
                for url in songs_url:
                    download_song(url, dest)
            case 3:
                pass
            case 4:
                delete_song(dest)
            case -1:
                pass

        input("\nPress [Enter] to continue...")

