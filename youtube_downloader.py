import os
import yt_dlp

DOWNLOAD_PATH = 'downloads'
os.makedirs(DOWNLOAD_PATH, exist_ok=True)

def download_video(url, save_path=DOWNLOAD_PATH):
    try:
        ydl_opts = {
            'format': 'bestvideo+bestaudio/best',
            'merge_output_format': 'mp4',
            'outtmpl': os.path.join(save_path, '%(title)s-%(id)s.%(ext)s'),
            'noplaylist': True,
            'cachedir': False,
            'ignoreerrors': True,
            'postprocessors': [
                {
                    'key': 'FFmpegVideoConvertor',
                    'preferedformat': 'mp4',  # force .mp4
                },
                {
                    'key': 'FFmpegVideoRemuxer',  # ensure QuickTime-compatible mp4
                    'preferedformat': 'mp4',
                }
            ]
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            print(f"✅ Download Complete! Saved as: {info_dict.get('title')}")

    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    link = input("Enter YouTube video URL: ").strip()
    download_video(link)