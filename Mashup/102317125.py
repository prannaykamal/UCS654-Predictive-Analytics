import sys
import os
import yt_dlp
from pydub import AudioSegment

def main():
    try:
        if len(sys.argv) != 5:
            sys.exit(1)

        singer_name = sys.argv[1]
        n_vids = int(sys.argv[2])
        duration = int(sys.argv[3])
        file_out = sys.argv[4]

        if n_vids <= 10:
            print("Number of videos should be greater than 10")
            sys.exit(1)

        if duration <= 20:
            print("Duration must be greater than 20 seconds")
            sys.exit(1)

        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': 'temp_vid_%(autonumber)s.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'quiet': True
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([f"ytsearch{n_vids}:{singer_name}"])

        mashup = AudioSegment.empty()
        
        for f in os.listdir("."):
            if f.startswith("temp_vid_") and f.endswith(".mp3"):
                audio = AudioSegment.from_mp3(f)
                cut = audio[:duration * 1000]
                mashup += cut
                os.remove(f)

        mashup.export(file_out, format="mp3")
        print(f"Mashup created: {file_out}")

    except ValueError:
        print("Number of videos and duration must be valid integers")
    except Exception as e:
        print(f"Unexpected error occurred: {e}")

if __name__ == "__main__":
    main()