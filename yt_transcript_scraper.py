# YouTube Transcript Scraper
'''
This script will scrape the Given YouTube video url {title, description, transcript} --> output: json file
The json file will be saved in root/yt_scrapes directory. You can upload the file to your choice of ai
to summarize the video

Sample prompt: 
"Summarize the following video. Make it short and concise. Persist all the details and information mentioned
in the video. Follow and provide details of the workflows, steps, setups, etc. if any."
'''

#!/usr/bin/env python3
"""
youtube_scraper.py

Reads all YouTube video/playlist URLs from 'urls.txt' (one per line).
Fetches title, description, and transcript for every video.
Saves one JSON per video in the current directory.

Requirements:
    pip install pytube youtube-transcript-api
"""

import json
from pathlib import Path
from pytube import YouTube, Playlist
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled, NoTranscriptFound

def get_video_id(url: str) -> str:
    """Extract the YouTube video ID from any standard URL."""
    from urllib.parse import urlparse, parse_qs
    if "youtu.be" in url:
        return url.split("/")[-1].split("?")[0]
    if "/shorts/" in url:
        return url.split("/shorts/")[1].split("?")[0]
    qs = parse_qs(urlparse(url).query)
    return qs.get("v", [""])[0]

def clean_video_url(url: str) -> str:
    """Remove playlist and other parameters, keeping only the video URL."""
    video_id = get_video_id(url)
    if video_id:
        return f"https://www.youtube.com/watch?v={video_id}"
    return url

def fetch_video_details(url: str) -> dict:
    """Use pytube to fetch video metadata (title, description) with error handling."""
    try:
        # Try with different user agent and parameters
        yt = YouTube(url, use_oauth=False, allow_oauth_cache=False)
        return {
            "title": yt.title or "Title not available",
            "description": yt.description or "Description not available"
        }
    except Exception as e:
        print(f"Warning: Could not fetch metadata for {url}: {e}")
        # Fallback: extract basic info from URL
        video_id = get_video_id(url)
        return {
            "title": f"YouTube Video {video_id}",
            "description": "Metadata not available due to YouTube restrictions"
        }

def fetch_transcript(video_id: str) -> str:
    """Get the transcript in plain text. Fallback if unavailable."""
    try:
        # Create an instance of the API
        api = YouTubeTranscriptApi()
        # Fetch transcript with preferred languages
        transcript_data = api.fetch(video_id, languages=["en", "en-US", "en-GB"])
        return " ".join(entry.text for entry in transcript_data)
    except (TranscriptsDisabled, NoTranscriptFound):
        return "[Transcript not available for this video.]"
    except Exception as e:
        print(f"Warning: Could not fetch transcript for {video_id}: {e}")
        return "[Transcript not available for this video.]"

def process_video(url: str):
    # Clean the URL to remove playlist parameters
    clean_url = clean_video_url(url)
    video_id = get_video_id(clean_url)
    if not video_id:
        print(f"Could not parse a video ID from: {url}")
        return
    
    print(f"Processing video ID: {video_id}")
    
    # Fetch video metadata (with fallback)
    video_meta = fetch_video_details(clean_url)
    transcript = fetch_transcript(video_id)
    json_data = {
        "url": url,
        "title": video_meta["title"],
        "description": video_meta["description"],
        "transcript": transcript
    }
    # Ensure the yt_scrapes directory exists
    output_dir = Path("yt_scrapes")
    output_dir.mkdir(exist_ok=True)
    out_path = output_dir / f"{video_id}.json"
    out_path.write_text(json.dumps(json_data, ensure_ascii=False, indent=2))
    print(f"Saved → {out_path.resolve()}")

def main():
    urls_file = Path("urls.txt")
    if not urls_file.exists():
        print("ERROR: Please create a 'urls.txt' file in this directory, with one YouTube video or playlist URL per line.")
        return

    with urls_file.open(encoding='utf-8') as f:
        lines = [line.strip() for line in f if line.strip() and not line.strip().startswith("#")]

    all_video_urls = []
    for line in lines:
        if 'playlist?list=' in line:
            try:
                playlist = Playlist(line)
                playlist_urls = playlist.video_urls
                print(f"Found {len(playlist_urls)} videos in playlist: {line}")
                all_video_urls.extend(playlist_urls)
            except Exception as e:
                print(f"Error fetching playlist {line}: {e}")
        else:
            all_video_urls.append(line)

    print(f"Processing {len(all_video_urls)} videos in total...")
    for url in all_video_urls:
        process_video(url)

if __name__ == "__main__":
    main()


'''
Usage:
create a urls.txt file in the root directory and add the youtube urls to it.
Each line is a single YouTube video url.
'''
