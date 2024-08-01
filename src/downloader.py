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


yt_opts = {
    'format': 'bestaudio/best',  # Download the best available audio quality
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',  # Extract audio using ffmpeg
        'preferredcodec': 'mp3',      # Save as mp3 temporarily
        'preferredquality': '192',    # Specify quality for mp3
    }],
    'outtmpl': '%(title)s.%(ext)s',  # Template for output filename
    'quiet': True                    # Suppress yt-dlp output
}



def download_audio(song, audio_format="wav", directory="audio"):
    # Ensure the directory exists
    os.makedirs(directory, exist_ok=True)
    
    try:
        temp_mp3_path = os.path.join(directory, f"{song.title}.mp3") 
        temp_mp3_name = os.path.join(directory, f"{song.title}") 
        wav_filename = os.path.join(directory, f"{song.title}.wav")
        yt_opts['outtmpl'] = temp_mp3_name
        
        # Download audio using yt-dlp
        print(f"Downloading: {song.title}")
        with yt_dlp.YoutubeDL(yt_opts) as ydl:
            ydl.download([song.link])
        
        # Skip conversion if mp3 is the final format
        if audio_format == "mp3":
            print(f"Audio successfully saved as '{os.path.join(directory, song.title)}.mp3'\n")
            return
        
        # Convert the downloaded file to WAV
        print(f"Converting {temp_mp3_path} to WAV format...")
        audio = AudioSegment.from_file(temp_mp3_path, format="mp3")
        audio.export(wav_filename, format="wav")
        
        # Clean up the temporary downloaded mp3 file if converting to WAV
        if audio_format == "wav":
            os.remove(temp_mp3_path)
        
        print(f"Audio successfully saved as '{wav_filename}'\n")
        
    except yt_dlp.utils.DownloadError as e:
        print(f"Failed to download {song.title}: {e}\n")
    except Exception as e:
        print(f"An error occurred while processing {song.title}: {e}\n")


if __name__ == "__main__":
    for song in download_queue:
        download_audio(song, audio_format="both")