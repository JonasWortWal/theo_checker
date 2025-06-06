from youtube_transcript_api import YouTubeTranscriptApi
import re

def fetch_transcript(url):
    try:
        video_id = extract_video_id(url)
        transcript = (
            YouTubeTranscriptApi
            .list_transcripts(video_id)
            .find_transcript(['de', 'en'])
            .fetch()
        )
        full_text = " ".join([entry['text'] for entry in transcript])
        return full_text
    except Exception:
        return None

def extract_video_id(url):
    match = re.search(r"(?:v=|\/)([0-9A-Za-z_-]{11})", url)
    return match.group(1) if match else None
