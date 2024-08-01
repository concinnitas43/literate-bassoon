import yt_dlp
from pydub import AudioSegment
import os


class Song:
    def __init__(self, link, title) -> None:
        self.link = link
        self.title = title

download_queue = [ 
    Song("https://www.youtube.com/watch?v=Ov2lpIuLFF8", "Chopin prelude No. 20"),
    Song("https://www.youtube.com/watch?v=wy_g6UllbQI", "Bach Invention no. 8"),
]
def download_audio(song):
    try:
        # Set the output filename using song title
        output_filename = f"{song.title}.mp3"
        yt_opts['outtmpl'] = output_filename
        
        print(f"Downloading: {song.title}")
        # Download audio using yt-dlp
        with yt_dlp.YoutubeDL(yt_opts) as ydl:
            ydl.download([song.link])
        
        # Convert the downloaded file to WAV
        print("Converting to WAV format...")
        wav_filename = f"{song.title}.wav"
        audio = AudioSegment.from_file(output_filename, format="mp3")
        audio.export(wav_filename, format="wav")
        
        # Clean up the temporary downloaded mp3 file
        os.remove(output_filename)
        
        print(f"Audio successfully saved as '{wav_filename}'\n")
        
    except yt_dlp.utils.DownloadError as e:
        print(f"Failed to download {song.title}: {e}\n")
    except Exception as e:
        print(f"An error occurred while processing {song.title}: {e}\n")

if __name__ == "__main__":
    for song in download_queue:
        download_audio(song)