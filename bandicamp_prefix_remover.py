from pathlib import Path  # How did I not know of this awesome module earlier?
from os import system


def main():
    while True:
        home_path = Path.home() / "Music/"
        if not home_path.exists():
            print("Error: Music folder doesn't exist.")
            break
        
        print("NOTE: Some characters may be dashes due to bandcamp's formatting.")
        print("In order to prevent issues, rename the folder to the song prefix!")
        
        get_music = "The Caretaker - Everywhere, an empty bliss"

        album_path = home_path / f"{get_music}/"

        if not album_path.exists():
            print("Error: Album not found, try again later.")
            break

        # Iterate through each file and remove the prefix.

        times_converted = 0

        system("clear")
        for file in album_path.iterdir():
            if get_music in str(file.relative_to(album_path)):  # Prevent doing operations on non-prefixed files.
                removed_prefix = str(file.relative_to(album_path))[len(str(get_music)) + 3:]
                print(removed_prefix)
                print(f"{file.relative_to(album_path)} -> {removed_prefix}")
                file.rename(album_path / removed_prefix)
                times_converted += 1
            else:
                continue
        
        if times_converted > 0:
            print(f"Operation complete, {times_converted} files were converted!")
        else:
            print("No files were converted!")
        break


if __name__ == "__main__":
    main()
