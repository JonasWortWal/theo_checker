from youtube_transcript_api import YouTubeTranscriptApi
import re

def fetch_transcript(url):
    try:
        video_id = extract_video_id(url)
        transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
        print("🟢 Transkriptliste geladen:", transcript_list._manually_created_transcripts + transcript_list._generated_transcripts)

        transcript = transcript_list.find_transcript(['de', 'en']).fetch()
        full_text = " ".join([entry['text'] for entry in transcript])
        return full_text
    except Exception as e:
        return f"[Fehler intern: {str(e)}]"

def extract_video_id(url):
    match = re.search(r"(?:v=|\/)([0-9A-Za-z_-]{11})", url)
    return match.group(1) if match else None
