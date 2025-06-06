from youtube_transcript_api import YouTubeTranscriptApi
import re

def fetch_transcript(url):
    try:
        video_id = extract_video_id(url)
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['de', 'en'])
        full_text = " ".join([entry['text'] for entry in transcript])
        return full_text
    except Exception as e:
        return None

def extract_video_id(url):
    match = re.search(r"(?:v=|\/)([0-9A-Za-z_-]{11}).*", url)
    return match.group(1) if match else None