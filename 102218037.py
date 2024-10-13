!pip install pytube moviepy
!pip install yt-dlp
import os
import yt_dlp
from moviepy.editor import concatenate_videoclips, VideoFileClip

video_urls = [
    "https://www.youtube.com/watch?v=VIDEO_ID_1",
    "https://www.youtube.com/watch?v=VIDEO_ID_2",
]

output_dir = "downloaded_clips"
os.makedirs(output_dir, exist_ok=True)

video_clips = []

for idx, url in enumerate(video_urls):
    try:
        print(f"Downloading video {idx + 1}: {url}")
        ydl_opts = {
            'format': 'best[ext=mp4]',
            'outtmpl': f"{output_dir}/video_{idx + 1}.mp4",
            'postprocessors': [{
                'key': 'FFmpegVideoFile',
                'options': {'-ss': '0', '-t': '30'},  
            }],
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        
        video_path = os.path.join(output_dir, f"video_{idx + 1}.mp4")
        print(f"Loading clip {video_path}")
        clip = VideoFileClip(video_path)
        video_clips.append(clip)

    except Exception as e:
        print(f"An error occurred while processing {url}: {e}")

if video_clips:
    mashup = concatenate_videoclips(video_clips, method="compose")
    output_file = "mashup_video.mp4"
    mashup.write_videofile(output_file, codec="libx264")
    print(f"Mashup video created successfully: {output_file}")
else:
    print("No valid video clips were downloaded.")

for clip in video_clips:
    clip.close()

for idx in range(len(video_urls)):
    try:
        os.remove(os.path.join(output_dir, f"video_{idx + 1}.mp4"))
    except Exception as e:
        print(f"Error removing file: {e}")
