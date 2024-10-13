!pip install yt-dlp
import yt_dlp

def download_songs(singer, number_of_songs):
    search_query = f"{singer} songs"
    
    ydl_opts = {
        'format': 'bestaudio/best',  
        'outtmpl': 'songdwl/%(title)s.%(ext)s', 
        'noplaylist': True, 
        'extractaudio': True,  
        'audioformat': 'mp3'  
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.extract_info(f"ytsearch{number_of_songs}:{search_query}", download=True)

singer = "BTS"
number_of_songs = 6

download_songs(singer, number_of_songs)
